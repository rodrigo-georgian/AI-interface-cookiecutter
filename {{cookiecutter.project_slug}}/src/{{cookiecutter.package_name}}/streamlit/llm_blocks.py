
import io

import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory.chat_message_histories.in_memory import ChatMessageHistory
from langchain.schema import AIMessage, HumanMessage
from streamlit_chat import message

from genai_app_template.streamlit.utils import (
    catchtime,
    redirect_stdout_copy,
    render_stdout,
)


def save_stdout_to_state(name: str, func: callable, *args, **kwargs):
    with st.spinner(f"running {name}..."):
        with catchtime() as t:
            with io.StringIO() as buf, redirect_stdout_copy(buf):
                func(*args, **kwargs)
                st.session_state[name] = buf.getvalue()
        if t() > 0.05:
            print(f"{name} took {t():.2f}s")


def llm_stdout_st_block(name, func: callable, *args, **kwargs):
    name_var = name.lower().replace(" ", "_")
    std_out_var = f"{name_var}_std_output"
    st.header(f"{name}")
    input_text = st.text_area("Agent Input", key=f"{name_var}_input_text")
    button = st.button(f"Send to {name}", key=f"{name_var}_run_button")
    if button:
        print(f"{name} input:\n{input_text}")
        save_stdout_to_state(std_out_var, func, input_text, *args, **kwargs)
    else:
        pass
    if std_out_var in st.session_state:
        with st.expander(f"{name} Response", expanded=True):
            render_stdout(st.session_state[std_out_var])


def chat_memory_st_block(chat_memory: ChatMessageHistory):
    for i, _message in enumerate(chat_memory.messages):
        if isinstance(_message, HumanMessage):
            message(_message.content, is_user=True, key=str(i) + "_user")
        elif isinstance(_message, AIMessage):
            message(_message.content, key=str(i))


def llm_chatbot_st_block(name, chatbot: ConversationChain):
    name_var = name.lower().replace(" ", "_")

    st.header(f"{name}")

    user_input = st.text_area("Chatbot input", key=f"{name_var}_input_text")
    button = st.button(f"Send to {name}", key=f"{name_var}_run_button")
    if button:
        print(f"{name} input:\n{user_input}")
        output = chatbot.run(user_input)
        print(f"{name} output:\n{output}")

    if len(chatbot.memory.chat_memory.messages) > 0:
        with st.expander(f"{name} Response", expanded=True):
            chat_memory_st_block(chatbot.memory.chat_memory)
