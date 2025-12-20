setup:
		uv sync
		uv run pre-commit install

install:
		uv sync

sync:
		uv sync

typecheck:
		uv run ty check

start:
		echo "does not work right now"

lint:
		uv run ruff check .

format:
		uv run ruff format .

dev:
		uv run uvicorn choice_paralysis.src.main:app --reload --host 0.0.0.0 --port 8000
