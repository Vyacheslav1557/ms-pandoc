FROM python:3.10-slim as builder

RUN pip3 install poetry==1.8.2
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

ENV POETRY_NO_INTERACTION=1 \
POETRY_VIRTUALENVS_IN_PROJECT=1 \
POETRY_VIRTUALENVS_CREATE=true \
POETRY_CACHE_DIR=/tmp/poetry_cache

RUN --mount=type=cache,target=/tmp/poetry_cache poetry install --only main --no-root
RUN poetry install

FROM python:3.10-slim as runner

COPY . /app/
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

CMD ["/app/.venv/bin/python", "app/cmd/ms-pandoc/main.py"]