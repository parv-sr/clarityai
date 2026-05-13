FROM python:3.13-slim

RUN pip install --no-cache-dir uv

WORKDIR /clarityai

COPY pyproject.toml ./
COPY uv.lock ./

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]