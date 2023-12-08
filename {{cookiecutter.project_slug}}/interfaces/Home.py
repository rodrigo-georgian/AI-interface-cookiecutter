
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
