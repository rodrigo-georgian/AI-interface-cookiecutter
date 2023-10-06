# from typing import Callable

# import dotenv
# import streamlit as st
# from langchain.chains import ConversationChain

# from {{cookiecutter.package_name}}.ai.agents import get_python_agent
# from {{cookiecutter.package_name}}.ai.chains import get_basic_conversation_chain
# from {{cookiecutter.package_name}}.streamlit.llm_blocks import (
#     llm_chatbot_st_block,
#     llm_stdout_st_block,
# )

# dotenv.load_dotenv(".env", override=True)


# @st.cache_resource
# def get_python_agent_resource() -> Callable:
#     return get_python_agent()


# @st.cache_resource
# def get_chatbot_resource() -> ConversationChain:
#     return get_basic_conversation_chain(model_name='gpt-3.5-turbo')

# def python_agent_run(*args, **kwargs):
#         response = get_python_agent_resource().run(*args, **kwargs)
#         return response


# # Streamlit App
# st.set_page_config(layout="wide")
# st.title('GenAI App Template Interface Example')

# llm_stdout_st_block("Python AI Agent", python_agent_run)

# llm_chatbot_st_block("ChatBot", get_chatbot_resource())


import streamlit as st

st.set_page_config(
    page_title="Demo Menu",
    page_icon="🌎",
    layout="wide"
)

st.write("# GenAI Interface Demos")

st.sidebar.success("Select a demo above")

st.markdown(
    """
    Congratulations! You successfully used 
    [this template](https://github.com/rodrigo-georgian/AI-interface-cookiecutter/tree/main)
    to get started with a Gen AI interfaces.
    
    **👈 Select a demo from the sidebar** to see some simple
    interfaces for various Gen AI application.

    ### Next steps
    - Go through the examples to find the components you'll need for your application
    - Delete anything you don't need
    - Checkout the streamlit [documentation](https://docs.streamlit.io) to learn about more components
    - Once you're happy with your app, go to [streamlit cloud](https://streamlit.io/cloud) 
    to deploy it and share with others
    
    ### Other Streamlit Resources
    - [Community forums](https://discuss.streamlit.io)
    - More complex streamlit demos
        - [Self-driving Car Image Dataset](https://github.com/streamlit/demo-self-driving)
        - [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
