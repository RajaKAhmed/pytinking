from langchain import OpenAI
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

api_key = os.getenv('OPENAI_API_KEY')
llm = api_key

chat = ChatOpenAI(temperature=0)
x = chat.predict_messages([HumanMessage(content="How do you say I love you Melanie in French")])
print(x)
#llm = OpenAI(temperature=0.9)
#get_input = input(">>> ")
#x = llm.predict(get_input)
#print(x)

