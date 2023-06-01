# {{cookiecutter.project_name}}

# Installation

1. Environment management options
   
    a)  Poetry: ```poetry shell```
    
    b) Conda: create and activate a conda env for this project:
```bash
conda create -n {{cookiecutter.project_slug}} python=3.9
conda activate {{cookiecutter.project_slug}}
```

2. Install package
```
poetry install
```
3. Check installation worked by running 
```
pytest .
```

4. Create private environment file (this will not be committed!)
```
cp .env-template .env
```
Add any necessary API keys there following the given format.

# Repo Info
## Poetry
We use [poetry](https://python-poetry.org/) as our dependency manager.
The link above has great documentation but there is a TL;DR.

- Install the package: `poetry install`
- Add a dependency: `poetry add <python-lib>`
- Where are dependencies specified? `pyproject.toml` include the high level requirements. The latests exact versions installed are in `poetry.lock`.

