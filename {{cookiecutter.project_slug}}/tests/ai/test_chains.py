from typing import Callable

def test_import():
    from {{cookiecutter.package_name}}.ai.chains import get_basic_conversation_chain
    assert isinstance(get_basic_conversation_chain, Callable)
    