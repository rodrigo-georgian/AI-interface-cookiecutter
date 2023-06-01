from typing import Callable

def test_import():
    from {{cookiecutter.package_name}}.ai.agents import get_python_agent
    assert isinstance(get_python_agent, Callable)
    
