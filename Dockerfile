FROM python:3.9 AS base
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install --upgrade pip && \
    pip install pipenv
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

# Bot | Development ===========================================================
FROM base AS development
RUN pipenv install --dev --system --deploy
COPY ./src /app
CMD ["python", "bot.py"]

# Bot | Production ============================================================
FROM base AS production
RUN pipenv install --system --deploy
COPY ./src /app
CMD ["python", "bot.py"]

# Checker =====================================================================
FROM base as checker
RUN pipenv install --system --deploy
COPY ./src /app
CMD ["python", "checker.py"]
