from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms.openai import OpenAI
from langchain.tools.python.tool import PythonREPLTool
from pandasai import SmartDataframe


def get_python_agent():
    return create_python_agent(
        llm=OpenAI(temperature=0, max_tokens=1000),
        tool=PythonREPLTool(),
        verbose=True
    )


class FaultTolerantSmartDataframe:
    def __init__(self, df, config):
        self.df = df
        self.sdf = SmartDataframe(df, config=config)

    def __call__(self, prompt):
        try:
            return self.sdf.chat(prompt)
        except Exception as e:
            return f'Error: {e}'


def get_pandasai_df(df, model_name='gpt-3.5-turbo'):

    llm = ChatOpenAI(
        model_name=model_name,
        temperature=0,
    )
    sdf = FaultTolerantSmartDataframe(df, config={"llm": llm})
    return sdf
