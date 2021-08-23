FROM python:3.9-alpine

RUN apk add build-base
RUN pip install pipenv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system
RUN rm Pipfile Pipfile.lock

COPY src .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
