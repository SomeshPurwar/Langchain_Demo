from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

# tavily =TavilyClient()
# @tool
# def search(query:str)-> str:
#     """_summary_

#     Args:
#         query (str): _description_

#     Returns:
#         str: _description_
#     """
#     print(f"Searching for{query}")
#     return tavily.search(query=query)

llm= ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
tools=[TavilySearch()]
agent= create_agent(model=llm, tools=tools)
def main():
    print("Hello from langchain-course!")
    result= agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")})
    print(result["messages"][-1].content)
    
if __name__=="__main__":
    main()
