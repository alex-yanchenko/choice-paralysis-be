# Choice Paralysis Backend

Backend API for Choice Paralysis application.

## Requirements

- Python >= 3.13
- Poetry

## Setup

```bash
poetry install
```

## Running

```bash
poetry run start
```

The API will be available at `http://0.0.0.0:8000`.

## Development

```bash
# Install dev dependencies
poetry install --with dev

# Run linter
poetry run ruff check .
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

