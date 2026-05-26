# OpenRoute

A command-line interface utility to quickly search and interact with popular web services directly from the terminal.

## Requirements

- Python 3.14 or higher

## Installation

### 1. Install uv

If you do not have `uv` installed, install it using one of the following commands:

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Via pip:**
```bash
pip install uv
```

### 2. Install Project Dependencies

Sync the dependencies to create the virtual environment and install all packages:
```bash
uv sync
```

## Usage

Run the program with a service command and your search query:

```bash
uv run source/main.py <command> <query>
```

### Supported Commands

- `search` - Search DuckDuckGo
- `gpt` - Search ChatGPT
- `habr` - Search Habr
- `pacman` - Search Arch Linux package database
- `yay` - Search AUR packages
- `pypi` - Search PyPI
- `dockerhub` - Search Docker Hub
- `wiki` - Search Wikipedia
- `youtube` - Search YouTube
- `wb` / `wildberries` - Search Wildberries
- `t` / `translate` - Detect language and translate text between Russian and English

### Examples

```bash
uv run source/main.py search Python decorators
uv run source/main.py translate hello world
uv run source/main.py gpt write a quicksort in python
```
