# --- IMPORTS ---
import os
import requests
import streamlit as st

# LangChain libraries
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_experimental.tools import PythonREPLTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from chromadb.config import Settings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- TOOL 1: GET WEATHER ---
@tool
def get_weather_detail(city: str):
    """Fetches real-time weather for a given city using OpenWeatherMap API."""
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return "Error: OpenWeatherMap API key not found."

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    except Exception as e:
        return f"An error occurred: {e}"

# --- RAG SETUP & TOOL 2: SHOP DATA ---
# Use Streamlit's caching to load and process the data only once.
@st.cache_resource
def get_rag_chain():
    """Creates a Retrieval-Augmented Generation (RAG) chain for answering shop questions."""
    # Load and process the document
    loader = TextLoader("shop_data.txt")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splitted_docs = text_splitter.split_documents(docs)
    
    # Create Chroma vector store
    vectorstore = Chroma.from_documents(
        documents=splitted_docs,
        embedding=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
        client_settings=Settings(anonymized_telemetry=False)
    )
    
    retriever = vectorstore.as_retriever()
    
    # Define the RAG chain
    template = """
    Answer the question based only on the following context.
    Context: {context}
    Question: {question}
    """
    rag_prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

# Create the RAG tool
@tool
def answer_question_from_shop_data(question: str) -> str:
    """Answers questions about shop products, inventory, and policies using local data."""
    rag_chain = get_rag_chain()
    return rag_chain.invoke(question)

# --- AGENT SETUP ---
# Use Streamlit's caching to set up the agent executor only once.
@st.cache_resource
def get_agent_executor():
    """Initializes and returns the main agent executor."""
    # Initialize other tools
    wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
    
    # List of all tools
    tools = [
        answer_question_from_shop_data,
        get_weather_detail,
        WikipediaQueryRun(api_wrapper=wiki_wrapper),
        PythonREPLTool()
    ]
    
    # Agent prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You're a helpful personal assistant. Be polite and concise."),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])

    # Initialize LLM and create the agent
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
    agent = create_openai_tools_agent(llm, tools, prompt)
    
    # Create the Agent Executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor