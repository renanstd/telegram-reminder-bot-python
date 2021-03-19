FROM python:3.9

WORKDIR /app
COPY Pipfile /app
COPY Pipfile.lock /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install --system --deploy

COPY ./src /app

CMD ["python", "bot.py"]
