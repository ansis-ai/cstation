# Control Station (cstation)

A CLI tool for code quality checks and formatting using Python and Typer.

## Features

- **Code Quality Checking**: Uses `ruff` to lint your Python code
- **Code Formatting**: Formats code using `ruff` formatter
- **File Scanning**: Scans directories for code files and provides statistics
- **Comprehensive Analysis**: Run all checks with a single command

## Installation

1. Clone this repository
2. Install the package:

   ```bash
   # Using uv (recommended)
   uv pip install -e .

   # Or using pip
   pip install -e .
   ```

## Requirements

- Python 3.12 or higher
- Dependencies will be automatically installed

## Usage

### Basic Commands

```bash
# Show help
cstation --help

# Check code quality
cstation check [path]
cstation check --fix  # Auto-fix issues

# Format code
cstation format [path]
cstation format --check  # Check formatting without changing files

# Scan directory for files
cstation scan [path]
cstation scan --ext py --ext js  # Multiple extensions
cstation scan --include-venv  # Include virtual environments

# Run all checks
cstation all [path]
cstation all --fix  # Run all with auto-fix
```

### Examples

```bash
# Check current directory
cstation check .

# Format a specific file
cstation format myfile.py

# Scan project and show statistics
cstation scan .

# Start a local server on port 8080
cstation server . --port 8080

# Start server and open browser automatically
cstation server . --open

# Run complete analysis on current directory
cstation all .
```

## Commands

### `check`

Run code quality checks using ruff linter.

```bash
cstation check [PATH] [OPTIONS]
```

**Options:**

- `--fix, -f`: Auto-fix issues when possible
- `--verbose, -v`: Verbose output

### `format`

Format code using ruff formatter.

```bash
cstation format [PATH] [OPTIONS]
```

**Options:**

- `--check`: Don't write back, just check if formatting is needed

### `scan`

Scan directory for code files and show statistics.

```bash
cstation scan [PATH] [OPTIONS]
```

**Options:**

- `--ext`: File extensions to scan (default: py)
- `--include-venv`: Include virtual environment directories

### `server`

Start a local HTTP server to serve files from a directory.

```bash
cstation server [PATH] [OPTIONS]
```

**Options:**

- `--port, -p`: Port to serve on (default: 8000)
- `--host, -h`: Host to bind to (default: localhost)
- `--open, -o`: Open browser automatically

### `all`

Run all checks: scan, check, and format in sequence.

```bash
cstation all [PATH] [OPTIONS]
```

**Options:**

- `--fix, -f`: Auto-fix issues when possible

## Dependencies

- `typer`: CLI framework
- `ruff`: Fast Python linter and formatter
- `pathlib`: Path handling (built-in)
- `subprocess`: Running external commands (built-in)

## Development

This tool is built with:

- Python 3.12+
- Typer for CLI interface
- Ruff for linting and formatting

### Development Setup

```bash
# Clone the repository
git clone <repository-url>
cd cstation

# Install in development mode
uv pip install -e .

# Run tests (if available)
pytest
```
