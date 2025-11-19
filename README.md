# Choice Paralysis Backend

Backend API for Choice Paralysis application.

## Requirements

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) (install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`)

## Setup

```bash
uv sync
```

## Running

```bash
uv run start
```

The API will be available at `http://0.0.0.0:8000`.

## Development

```bash
# Install dev dependencies (included by default)
uv sync

# Run linter
uv run ruff check .
```

## Project Structure

```
choice_paralysis/
  src/
    application/    # Application layer
    domain/         # Domain models
    infrastructure/ # Infrastructure (DB, logging, etc.)
    main.py         # FastAPI application entry point
    config.py       # Configuration settings
```
