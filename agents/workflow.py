from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt.tool_node import ToolNode, tools_condition
from langchain_core.messages import AIMessage, HumanMessage
from utils import model_loader
from tool_kit import *
from typing import Annotated, TypedDict

class State(TypedDict):
    messages: Annotated[list,add_messages]

class GraphBuilder:
    def __init__(self):
        pass
    
    def __chatbot_node(self,stake:State):
        pass
    
    def build(self):
        pass
    
    def get_graph(self):
        pass
    
    