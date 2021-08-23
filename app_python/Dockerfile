FROM python:3.9-alpine
RUN pip install pipenv

WORKDIR /etc/app

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv lock -r > /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN rm Pipfile Pipfile.lock /tmp/requirements.txt

COPY app.py .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

CMD ["python", "-m", "flask", "run"]
