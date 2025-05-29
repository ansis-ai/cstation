# Welcome to Control Station (cstation)

Control Station (cstation) is a command-line tool designed to help you manage your servers efficiently.

## Overview

Cstation provides a simple interface for listing servers defined in your inventory files. It aims to simplify common server management tasks.

## Key Features

- **Server Listing**: Quickly view all servers from your inventory, along with their group and connection details.
- **Inventory-Based**: Uses standard YAML inventory files (e.g., `etc/inventory/ansis.yml`, `etc/inventory/syc.yml`).

## Getting Started

1.  **Installation**: Follow the instructions in the [Installation Guide](installation.md).
2.  **Configuration**: Ensure your server inventory files are correctly set up in the `etc/inventory/` directory.
3.  **Usage**: Learn how to use the available commands in the [Usage Guide](usage.md).

## Project Structure

- `cstation/`: Main application code.
  - `server/`: Server management commands.
  - `utils/`: Utility functions.
- `docs/`: Documentation files (what you're reading now).
- `etc/`: Configuration files, including server inventories.
- `tests/`: (Future) Unit and integration tests.

## Contributing

We welcome contributions to cstation! Whether it's bug reports, feature requests, or code contributions, please check out our [Contributing Guide](contributing.md) to get started.

---

_For more information, explore the documentation sections using the navigation menu._
