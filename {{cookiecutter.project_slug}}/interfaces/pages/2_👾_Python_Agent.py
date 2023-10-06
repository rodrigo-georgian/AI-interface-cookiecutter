from typing import Callable

import dotenv
import streamlit as st

from {{cookiecutter.package_name}}.ai.agents import get_python_agent
from {{cookiecutter.package_name}}.streamlit.llm_blocks import llm_stdout_st_block

dotenv.load_dotenv(".env", override=True)


@st.cache_resource
def get_python_agent_resource() -> Callable:
    return get_python_agent()


def python_agent_run(*args, **kwargs):
    response = get_python_agent_resource().run(*args, **kwargs)
    return response


st.set_page_config(page_title="Python Agent Demo", page_icon="👾")
st.info(
    '''This page demos a simple Agent with a python interpreter. 
Ask it to write you a function and see it's thought process and final output, formatted as if on a terminal.''', 
    icon="ℹ️"
)
llm_stdout_st_block("Python AI Agent", python_agent_run)
