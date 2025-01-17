import logging
from dotenv import load_dotenv

from langchain.agents import create_openai_tools_agent
from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

logging.getLogger("httpx").setLevel(logging.DEBUG)

load_dotenv()  # Load environment variables from .env file


def invoke_anthropic_model():
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]

    return model.invoke(messages)


def invoke_openai_model():
    model = ChatOpenAI(model="gpt-4")
    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!"),
    ]

    return model.invoke(messages)


def invoke_openai_agent():
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.7,
    )
    tools = [TavilySearchResults(max_results=1)]

    PROMPT = """You are a helpful AI assistant.

    Human: {input}
    Assistant: Let me help you with that. {agent_scratchpad}"""

    prompt = ChatPromptTemplate.from_template(PROMPT)

    agent = create_openai_tools_agent(llm, tools, prompt)
    return agent.invoke({
        "input": "What is the capital of France?",
        "agent_scratchpad": "",
        "intermediate_steps": [],
    })
