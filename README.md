# DevOps Course Deliverables

## Setup

Prerequisites: docker, python3.9

1. Clone the repo: `git clone git@github.com:vadimkerr/devops-uni.git`
1. Install pipenv: `python3.9 -m pip install --user pipenv`
1. Initialize a virtual environment and install dependencies: `pipenv install` (in `app_python` directory)
1. Install pre-commit hooks: `pre-commit install` (in the root directory)

## Running the server

### Locally

`pipenv run "uvicorn main:app --reload"` (in `app_python` directory)

### Using docker

`docker run -it --rm -p 8000:8000 vadimkerr/devops-uni:latest`
