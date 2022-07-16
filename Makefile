setup-backend:
	cd backend &&\
		python -m pip install --upgrade pip &&\
			pip install -r requirements_dev.txt

test-backend:
	cd backend &&\
		python -m pytest . && \
			python -m mypy main.py

setup-metrics-scheduler:
	cd metrics &&\
		python -m pip install --upgrade pip &&\
			pip install -r requirements_dev.txt

test-metrics-scheduler:
	cd metrics &&\
		python -m pytest . && \
			python -m mypy main.py

setup-frontend:
	cd frontend &&\
		npm install

test-frontend:
	cd frontend &&\
		npm run coverage

test-all: setup-backend test-backend setup-metrics-scheduler test-metrics-scheduler setup-frontend test-frontend