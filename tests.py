import os
import subprocess
import tempfile

import pytest


def run_package_tests(path):
    # Go to the given path
    os.chdir(path)

    # Create a temporary directory as the environment
    with tempfile.TemporaryDirectory() as temp_dir:

        # uncomment this line to debug
        from pathlib import Path
        input(f'Created temp baked folder: {Path(temp_dir).parent}. Press key to exit...')

        # Create a virtual environment
        subprocess.check_call(["python3", "-m", "venv", temp_dir])

        # Activate the virtual environment
        activate_script = os.path.join(temp_dir, 'bin', 'activate')

        # Install the Python package
        subprocess.check_call(["bash", "-c", f"source {activate_script} && poetry install"])

        # Run pytest
        subprocess.check_call(["bash", "-c", f"source {activate_script} && pytest ."])


@pytest.fixture
def baked_cookies(cookies):
    return cookies.bake(extra_context={"project_name": "GenAI Test Project"})


def test_bake_project(baked_cookies):

    assert baked_cookies.exit_code == 0
    assert baked_cookies.exception is None


def test_bake_project_tests(baked_cookies):
    run_package_tests(baked_cookies._project_dir)
