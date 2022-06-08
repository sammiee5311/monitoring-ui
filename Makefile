setup-backend:
	cd backend &&\
		python -m pip install --upgrade pip &&\
			pip install tox tox-gh-actions

test-backend:
	cd backend &&\
		tox

setup-frontend:
	cd frontend &&\
		npm install

test-frontend:
	cd frontend &&\
		npm run coverage

test-all: setup-backend test-backend setup-frontend test-frontend