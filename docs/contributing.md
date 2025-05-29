# Contributing to Control Station

Thank you for your interest in contributing to Control Station (cstation)! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read it before contributing.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Git
- A GitHub account

### Setting Up Your Development Environment

1. Fork the repository on GitHub
2. Clone your fork locally:

   ```bash
   git clone https://github.com/your-username/cstation.git
   cd cstation
   ```

3. Set up a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install the package in development mode:

   ```bash
   uv pip install -e .
   ```

5. Install development dependencies:
   ```bash
   uv pip install -r requirements-dev.txt
   ```

### Development Workflow

1. Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and ensure they follow the project's coding standards

3. Write tests for your changes

4. Run the tests to ensure everything works:

   ```bash
   pytest
   ```

5. Run the linter and formatter:

   ```bash
   cstation lint .
   cstation format .
   ```

6. Commit your changes with a descriptive commit message:

   ```bash
   git commit -m "Add feature: your feature description"
   ```

7. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

8. Create a pull request from your fork to the main repository

## Pull Request Guidelines

- Fill in the required pull request template
- Include tests for any new functionality
- Update documentation for any changed functionality
- Ensure all tests pass and code is properly formatted
- Keep pull requests focused on a single topic
- Reference any related issues in your pull request

## Coding Standards

### Code Style

We follow PEP 8 with some modifications. The project uses `ruff` for linting and formatting. You can check and format your code using:

```bash
cstation lint . --fix
cstation format .
```

### Documentation

- Use docstrings for all public modules, functions, classes, and methods
- Follow the Google docstring style
- Keep documentation up to date with code changes

### Testing

- Write tests for all new functionality
- Aim for high test coverage
- Use pytest for writing and running tests

## Feature Requests and Bug Reports

- Use the GitHub issue tracker to report bugs or request features
- Check existing issues before creating a new one
- Provide detailed information when reporting bugs:
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
  - Environment details (OS, Python version, etc.)

## Release Process

1. Version numbers follow semantic versioning (MAJOR.MINOR.PATCH)
2. Changes are documented in CHANGELOG.md
3. Releases are tagged in Git and published to PyPI

## Project Structure

```
cstation/
├── server/       # Server-related functionality
├── utils/        # Utility functions
├── etc/          # Configuration files
├── docs/         # Documentation
├── tests/        # Test suite
└── scripts/      # Development and release scripts
```

## Communication

- GitHub Issues: Bug reports, feature requests, and discussions
- Pull Requests: Code review and discussion of implementations

## License

By contributing to this project, you agree that your contributions will be licensed under the project's license.

## Acknowledgements

Thank you to all contributors who help make this project better!
