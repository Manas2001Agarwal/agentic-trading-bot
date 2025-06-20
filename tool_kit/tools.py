from langchain import tool
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import LanceDB
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults
from lancedb.rerankers import LinearCombinationReranker
from data_models.models import RagToolSchema

@tool(args_schema = RagToolSchema)
def retriever_too(question):
    pass

