# API Reference

This document provides an overview of the Control Station (cstation) API, focusing on how to interact with its server management functionalities programmatically.

## Core Modules

### `server` Module

Handles server-related operations.

- **`server.main.list()`**:
  - **Description**: Retrieves and lists servers from the inventory.
  - **Usage**: Internally called by the `cstation server list` CLI command.
  - **Returns**: Prints server information to the console. Does not return a structured data object directly for external API use in its current form.

### `utils` Module

Contains utility functions used by cstation.

- **`utils.get_inventory_hosts()`**:

  - **Description**: Reads and parses server inventory files (e.g., `etc/inventory/ansis.yml`, `etc/inventory/syc.yml`).
  - **Returns**: A dictionary containing server groups and their respective host details.
  - **Example**:

    ```python
    from utils import get_inventory_hosts

    inventory = get_inventory_hosts()
    if inventory:
        for group, hosts in inventory.items():
            print(f"Group: {group}")
            for host_name, host_details in hosts.items():
                print(f"  {host_name}: {host_details.get('ansible_host', host_name)}")
    ```

## Command Execution

While cstation is primarily a CLI tool, its underlying functions (like `get_inventory_hosts`) can be imported and used in Python scripts if needed for custom automation.

## Error Handling

- Functions typically print error messages to standard output/error.
- For `get_inventory_hosts()`, ensure inventory files exist and are correctly formatted YAML.

## API Stability

- The internal structure and functions like `get_inventory_hosts()` are subject to change in future versions as the tool evolves. Direct programmatic use should be done with caution and an understanding that updates to cstation might require changes to your scripts.

## Future API Enhancements

As cstation grows, more structured APIs for programmatic access to its features (e.g., server information retrieval, command execution) may be developed.

For specific integration needs or API requests, please [open an issue](https://github.com/yourusername/cstation/issues).
