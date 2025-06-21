# Problem Statement
In this project we have created an agentic trading chatbot that will answer questions related to trading/stock prices etc.
Given that we want to invest our money in stock market, we will have questions for example - 
1) What is the current stock price of current stock of a particular company ?
2) Recent news regarding that company like any Product Launches, IPO, Events etc..
3) Info It's performance over the past quarter, year, previous 5 years and past 10 years

To get real time answers of such questions we aim to build an RAG based Agentic Trading Chatbot that will answer queries. 

# Agent Workflow
We have created a REACT type agent with three tools. LLM acts as Brain. Based on the users query LLM decides whether to make a tool call and if yes which tool to call. 
Here we basically utlize three tools to answer user queries.
1) Tavilly Search - To gather intelligence using Internet search
2) RAG pipeline - To refer to private (or proprietary) knowledge while giving answer to user queries.
3) Polygon API: To get real time stock prices, company details etc.

![REACT_Agent](https://github.com/user-attachments/assets/daf0055a-619c-4aaa-8f03-037cf0b83443)

# Component Used
1) Embedding LLM Model Used: Google-Gemini - "text-embedding-004"
2) Generating LLM Model Used: Groq - "meta-llama/llama-4-scout-17b-16e-instruct"
3) Vector DB Used: Pinecone Vector DB
   
# How to Launch the project
1) Clone the repo
   - git clone https://github.com/Manas2001Agarwal/agentic-trading-bot.git
   - cd agentic-trading-bot
2) Set Up Virtual Env
   - Use Conda : conda create --name agent_env python=3.10
   - conda activate agent_env
3) Install Dependencies
   - pip install -r requirements.txt
4) Set up .env file with below token
    - PINECONE_API_KEY = 
    - GOOGLE_API_KEY = 
    - HF_TOKEN = 
    - GROQ_API_KEY =  
    - TAVILY_API_KEY = 
5) Run main.py
   - uvicorn main:app --reload --port 8000
   - streamlit run streamli_ui.py

# Additional Info 
1) Created two endpoints using FastAPI
   - First to ingest the uploaded documents and load them into vector database. "\query" ==> Invoking langgraph workflow
   - Second to Agent (Graph) that will execute tools to get answers to question asked "\upload" ==> Invoking data ingestion pipeline
2) Created an Interactive UI components using Streamlit thay seeming integrated with both Fast API endpoints
3) Whether it is a .pdf or .docx we are accepting both file types and loading, chunking and storing them in Pinecone Vector DB
