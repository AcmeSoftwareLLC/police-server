FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV PYDEVD_DISABLE_FILE_VALIDATION=1 UV_LINK_MODE=copy

WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-editable

ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

FROM python:3.12-slim-bookworm
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY . /app/

ENTRYPOINT [ "/app/.venv/bin/fastapi" ]
CMD ["run", "--host", "0.0.0.0", "--port", "8000"]