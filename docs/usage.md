# Usage Guide

This guide covers the basic usage of Control Station (cstation) and its various commands.

## Command Overview

Cstation provides commands for server management:

```bash
cstation [COMMAND] [OPTIONS]
```

## Available Commands

### Help

To see all available commands and options:

```bash
cstation --help
```

To get help for a specific command:

```bash
cstation [COMMAND] --help
```

### Server Commands

Cstation includes server-related commands for managing your development environment:

#### List Servers

```bash
cstation server list
```

Lists all available servers from the inventory file (`etc/inventory/ansis.yml` or `etc/inventory/syc.yml`). It displays the server group, hostname, connection details (IP/hostname, user, port).

Example Output:

```
[Server Information]

Group: appserver
host1: 192.168.1.10  (user@22)

Group: dbserver
host2: 192.168.1.11  (user@22)
```

## Configuration

Server inventory is typically managed in YAML files located in the `etc/inventory/` directory. The `server list` command reads these files to display server information.

## Examples

### Listing Servers

```bash
# List all servers from the inventory
cstation server list
```

## Troubleshooting

If you encounter issues while using cstation, try the following:

1. Ensure you're using the latest version.
2. Check the logs for error messages if applicable.
3. Verify your inventory files in `etc/inventory/` are correctly formatted.

If problems persist, please [open an issue](https://github.com/yourusername/cstation/issues) with details about your environment and the error you're encountering.
