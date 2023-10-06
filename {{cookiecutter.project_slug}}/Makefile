.PHONY: run run-container gcloud-deploy

run:
	@streamlit run interfaces/Home.py --server.port=8080 --server.address=0.0.0.0

run-container:
	@docker build . -t genai_app_template_docker
	@docker run -p 8080:8080 genai_app_template_docker

gcloud-deploy:
	@gcloud app deploy app.yaml

demo:
	poetry run streamlit run interfaces/Home.py

demo-spaces:
	poetry run streamlit run interfaces/Home.py --server.enableCORS false --server.enableXsrfProtection false

deps:
	poetry export -f requirements.txt --output requirements.txt