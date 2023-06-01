import streamlit_mock


def test_add():
    sm = streamlit_mock.StreamlitMock()
    sm.run("simple_interface.py")
