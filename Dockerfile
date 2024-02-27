# Base ========================================================================
FROM python:3.9 AS base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

# Bot | Production ============================================================
FROM base AS production

RUN pipenv install --system --deploy
COPY ./src /app
CMD ["python", "bot.py"]
