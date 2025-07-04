import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from agent_setup import get_agent_executor

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Modular AI Assistant", layout="wide")
st.title("🤖 Your Personal AI Assistant")
st.markdown("---")

# --- AGENT CAPABILITIES IN BOXES ---
st.subheader("What I Can Do For You:")
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🛍️ Shop Q&A")
        st.write("Answer questions about products, inventory, and policies from local shop data.")

    with st.container(border=True):
        st.markdown("### 📚 Wikipedia Search")
        st.write("Look up information on any topic, person, or event.")

with col2:
    with st.container(border=True):
        st.markdown("### 🌦️ Real-time Weather")
        st.write("Get the current weather for any city in the world.")

    with st.container(border=True):
        st.markdown("### 🐍 Python Code Execution")
        st.write("Execute Python code for calculations or other tasks.")
st.markdown("---")


# --- AGENT & SESSION STATE INITIALIZATION ---
agent_executor = get_agent_executor()

# Initialize chat history in session state if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! How can I assist you today?"),
    ]

# --- CHAT INTERFACE ---
# Display chat messages from history
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# Get user input from the chat input box
if user_query := st.chat_input("Ask me something..."):
    # Add user message to history and display it
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message("Human"):
        st.write(user_query)
    
    # Get AI response
    with st.chat_message("AI"):
        with st.spinner("Thinking..."):
            # Invoke the agent to get the response
            response = agent_executor.invoke({
                "input": user_query,
                "chat_history": st.session_state.chat_history
            })
            
            # Display the final answer
            st.write(response["output"])

            # Add AI response to history
            st.session_state.chat_history.append(AIMessage(content=response["output"]))