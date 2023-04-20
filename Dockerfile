FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip && \
    pip install pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

# Checker =====================================================================
FROM base AS production
RUN pipenv install --system --deploy
COPY ./src /app
CMD ["python", "checker.py"]
