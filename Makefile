setup-backend:
	cd backend &&\
		python -m pip install --upgrade pip &&\
			pip install -r requirements_dev.txt

test-backend:
	cd backend &&\
		python -m pytest . && \
			python -m mypy main.py

setup-frontend:
	cd frontend &&\
		npm install

test-frontend:
	cd frontend &&\
		npm run coverage

test-all: setup-backend test-backend setup-frontend test-frontend