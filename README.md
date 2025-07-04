<div align="center">

# 🤖 4-in-1 AI Multi-Tool Assistant 🛠️

<p>
  <strong>An AI 'Swiss Army Knife' that learns from your documents, connects to the real world, and performs complex calculations—all within a sleek, interactive interface.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-LangChain-green?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/Interface-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License">
</p>

</div>

## 🚀 Key Features

This isn't just a chatbot. It's an intelligent agent with a toolkit of four powerful, distinct capabilities.

| Feature                               | Description                                                                                                                              | Icon |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | :--: |
| **Chat with Your Documents (RAG)** | Upload any `.txt` file and get instant, accurate answers based on its content. Perfect for querying reports, notes, or business data.      |  🛍️  |
| **Live Weather Reports** | Integrates with the OpenWeatherMap API to fetch real-time weather data for any city in the world.                                          |  🌦️  |
| **Wikipedia Search** | Taps into the vast knowledge base of Wikipedia to provide quick summaries on any topic you can think of.                                   |  📚  |
| **Python Code Execution** | A powerful computational engine that can run Python code to solve complex math problems, handle data, and perform calculations on the fly. |  🧮  |

---

## 🔧 Tech Stack & Architecture

This project leverages a modern AI stack to create a robust, modular, and intelligent application.

**Technologies Used:**

<p>
  <img src="https://img.shields.io/badge/LangChain-4682B4?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgdmlld0JveD0iMCAwIDI1NiAyNTYiPjxwYXRoIGZpbGw9IiM0Njg0YjQiIGQ9Ik0xMjggMjJDNjguMTEgMjIgMjIgNjguMTEgMjIgMTI4czQ2LjExIDEwNiAxMDYgMTA2YzM2LjMzIDAgNjkuMjItMTcuOTQgODkuODEtNDUuODdsLTIzLjEyLTE0LjQ1YTY5LjE5IDY5LjIgMCAwIDEtNjYuNjkgMjguMzJjLTM4LjMxIDAtNjkuMjctMzAuOTYtNjkuMjctNjkuMjdjMC0zOC4zMSAzMC45Ni02OS4yNyA2OS4yNy02OS4yN2ExMzguNDggMTM4LjQ4IDAgMCAxIDQyLjM3IDYuNjRsLTEyLjk0IDIwLjcxbDM5Ljc0IDI0Ljg0bDYuNTctMTA1LjE2bC0yNS4zNyAxNS44NkExMDYuMDIgMTA2LjAyIDAgMCAwIDEyOCAyMloiLz48cGF0aCBmaWxsPSIjNDY4NGI0IiBkPSJNMjA1LjY2IDE1MS4zYTEzOC4zMiAxMzguMzIgMCAwIDAtNi42NC00Mi4zN2wxMi45NC0yMC43MWwtMzkuNzQtMjQuODRsLTYuNTcgMTA1LjE2bDI1LjM3LTE1Ljg2YTEwNi4wMiAxMDYuMDIgMCAwIDEgMzQuNjQgMi42NGwyMy4xMiAxNC40NUE4Mi4xOSA4Mi4xOSAwIDAgMCAyMzQgMTI4YzAgOS4zNC0xLjgxIDE4LjI2LTQuOTQgMjYuNDlsLTIzLjQtMTMuMTZaIi8+PC9zdmc+" alt="LangChain">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Hugging Face-FFD21E?style=for-the-badge&logo=huggingface" alt="Hugging Face">
  <img src="https://img.shields.io/badge/Chroma-5A46E5?style=for-the-badge" alt="ChromaDB">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
</p>

**System Architecture:**

The application follows a simple but powerful agentic design pattern. The LangChain Agent acts as the central router, intelligently deciding which tool to use based on the user's input.

```mermaid
graph TD
    A[User] --> B{Streamlit UI};
    B --> C{LangChain Agent};
    C --> D{Tool Router};
    D -- "Shop/Doc Question" --> E[🛍️ RAG Tool];
    D -- "Weather Question" --> F[🌦️ Weather API];
    D -- "General Question" --> G[📚 Wikipedia API];
    D -- "Calculation/Code" --> H[🧮 Python REPL];
    E --> I[ChromaDB Vector Store];
    I --> E;
    E --> C;
    F --> C;
    G --> C;
    H --> C;
    C --> B;
    B --> A;

    style B fill:#FF4B4B,stroke:#333,stroke-width:2px;
    style C fill:#4682B4,stroke:#333,stroke-width:2px,color:#fff;
