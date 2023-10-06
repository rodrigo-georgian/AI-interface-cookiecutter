from typing import Callable

import pandas as pd
import streamlit as st

from {{cookiecutter.package_name}}.ai.agents import get_pandasai_df
from {{cookiecutter.package_name}}.streamlit.llm_blocks import pandasai_qa_st_block


@st.cache_resource
def get_pandasai_df_resource(df, model_name) -> Callable:
    return get_pandasai_df(df, model_name)


# Set page configuration
st.set_page_config(
    page_title="Pandas AI",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)
st.info(
    '''This page demos the Pandas AI agent. 
Upload a table and ask it questions or ask for plots!''',
    icon="ℹ️"
)

# Upload csv
if 'sdf' not in st.session_state:
    st.session_state.sdf = None

if st.session_state.sdf is None:
    file = st.file_uploader(
        "Upload a CSV file",
        type="csv",
    )
    if file is not None:
        df = pd.read_csv(file)
        st.session_state.sdf = get_pandasai_df_resource(df, model_name='gpt-3.5-turbo')


# run pandasai_qa_st_block
if st.session_state.sdf is not None:
    pandasai_qa_st_block(st.session_state.sdf)

    st.subheader("Current dataframe:")
    st.write(st.session_state.sdf.df)
