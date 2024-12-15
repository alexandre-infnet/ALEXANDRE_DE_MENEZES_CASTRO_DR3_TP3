import os

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferWindowMemory

from tools.weather_tool import get_weather_tool
from tools.restaurant_tool import get_restaurant_tool

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

memory = ConversationBufferWindowMemory(
    k=5, memory_key="chat_history", return_messages=True
)

agent = initialize_agent(
    tools=[get_weather_tool(), get_restaurant_tool()],
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
)