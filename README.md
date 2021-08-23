# DevOps Course Deliverables

## setup

prerequisites: docker, python3.9

1. clone the repo: `git clone git@github.com:vadimkerr/devops-uni.git`
1. install pipenv: `python3.9 -m pip install --user pipenv`
1. initialize a virtual environment and install dependencies: `pipenv install` (in the `app_python` directory)
1. install pre-commit hooks: `pre-commit install` (in the root directory)

## running the server

### locally

`pipenv run uvicorn server.main:app --reload` (in `app_python` directory)

### using docker

`docker run -it --rm -p 8000:8000 vadimkerr/devops-uni:latest`
