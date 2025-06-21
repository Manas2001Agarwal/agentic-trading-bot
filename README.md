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

![REACT_Agent](https://github.com/user-attachments/assets/35c49d3b-0f8b-45e0-a866-51d7d533da10)
