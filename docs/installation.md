# Installation

This guide will walk you through the process of installing Control Station (cstation) on your system.

## Prerequisites

Before installing cstation, ensure you have the following prerequisites:

- Python 3.12 or higher
- pip or uv package manager

## Installation Methods

### From Source (Recommended for Development)

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cstation.git
   cd cstation
   ```

2. Install the package in development mode:

   ```bash
   # Using uv (recommended)
   uv pip install -e .

   # Or using pip
   pip install -e .
   ```

   This will install the package in "editable" mode, allowing you to make changes to the code and have them immediately reflected when you run the `cstation` command.

### From PyPI (Coming Soon)

In the future, you'll be able to install cstation directly from PyPI:

```bash
# Using uv
uv pip install cstation

# Or using pip
pip install cstation
```

## Verifying Installation

To verify that cstation has been installed correctly, run:

```bash
cstation --help
```

You should see the help message displaying all available commands.

## Dependencies

The following dependencies will be automatically installed:

- typer: For creating the CLI interface
- ruff: For code linting and formatting
- rich: For rich text and formatting in the terminal

## Troubleshooting

If you encounter any issues during installation, try the following:

1. Ensure you're using Python 3.12 or higher:

   ```bash
   python --version
   ```

2. Update pip to the latest version:

   ```bash
   pip install --upgrade pip
   ```

3. If you're using a virtual environment, ensure it's activated before installing.

4. Check for any error messages during installation and search for solutions in the project's issue tracker.

If you continue to experience issues, please [open an issue](https://github.com/yourusername/cstation/issues) with details about your environment and the error you're encountering.
