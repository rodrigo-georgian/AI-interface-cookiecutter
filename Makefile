test:
	pip install -r requirements.txt
	pip install -r requirements-test.txt
	pytest -s tests.py

