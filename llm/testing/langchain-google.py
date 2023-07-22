from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
serpapi_api_key = os.getenv('SERPAPI_API_KEY')
llm = OpenAI(temperature=1)
tools = load_tools(["serpapi", "llm-math"], llm =llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)


get_input = input(">>> ")
output = agent.run(get_input)
print(output)

#python.langchain.com/docs/get_started/quickstart#environment-setup