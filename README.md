# Choice Paralysis Backend

Backend API for Choice Paralysis application.

## Requirements

- Python >= 3.14
- [uv](https://github.com/astral-sh/uv) (install with: `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [just](https://github.com/casey/just) (optional, install with: `brew install just` on macOS)

## Setup

```bash
# Install dependencies and git hooks
just setup
```

## Running

```bash
# Using just (recommended)
just start

# Or directly with uv
uv run start
```

The API will be available at `http://0.0.0.0:8000`.

## Development Commands

Using `just` (run `just --list` to see all commands):

```bash
just sync         # Sync dependencies
just start        # Start the application
just dev          # Start with hot reload
just format       # Format code
just typecheck    # Run type checking
just lint         # Run linter
```

Or use `uv run` directly:

```bash
uv run ty check
uv run ruff check .
uv run ruff format .
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
