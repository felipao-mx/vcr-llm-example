from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import logging
logging.getLogger("httpx").setLevel(logging.DEBUG)



def invoke_anthropic_model():
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!")
    ]

    return model.invoke(messages)

def invoke_openai_model():
    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
        SystemMessage("Translate the following from English into Italian"),
        HumanMessage("hi!")
    ]

    return model.invoke(messages)