FROM python:3.9-alpine

RUN apk --no-cache add build-base && pip --no-cache-dir install pipenv==2021.5.29

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system && rm Pipfile Pipfile.lock

COPY src .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
