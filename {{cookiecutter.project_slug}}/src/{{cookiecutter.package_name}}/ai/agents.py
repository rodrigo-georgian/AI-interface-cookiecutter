from langchain.agents.agent_toolkits import create_python_agent
from langchain.llms.openai import OpenAI
from langchain.tools.python.tool import PythonREPLTool


def get_python_agent():
    return create_python_agent(
        llm=OpenAI(temperature=0, max_tokens=1000),
        tool=PythonREPLTool(),
        verbose=True
    )
