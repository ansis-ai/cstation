import yaml
from pathlib import Path
import configparser

def get_ansible_inventory():
    """Get inventory path from ansible.cfg"""
    config = configparser.ConfigParser()
    config_path = Path('/Users/wsloh/cstation/etc/ansible.cfg')
    if config_path.exists():
        config.read(config_path)
        if 'defaults' in config and 'inventory' in config['defaults']:
            inventory_path = Path(config['defaults']['inventory'])
            if not inventory_path.is_absolute():
                inventory_path = config_path.parent / inventory_path
            return inventory_path.expanduser()
    return None

def get_inventory_hosts():
    """Read hosts from inventory YAML files"""
    inventory_path = get_ansible_inventory()
    if not inventory_path:
        return {}
    
    hosts = {}
    inventory_dir = Path(inventory_path)
    if inventory_dir.is_dir():
        for file in inventory_dir.glob('*.yml'):
            try:
                with open(file, 'r') as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, dict):
                        for group, group_data in data.items():
                            if isinstance(group_data, dict) and 'hosts' in group_data:
                                group_hosts = {}
                                for host, host_data in group_data['hosts'].items():
                                    if host != 'vars':  # Skip vars section
                                        host_info = {}
                                        if isinstance(host_data, dict):
                                            # Only extract server-related information
                                            if 'ansible_host' in host_data:
                                                host_info['ansible_host'] = host_data['ansible_host']
                                            if 'ansible_user' in host_data:
                                                host_info['ansible_user'] = host_data['ansible_user']
                                            if 'ansible_port' in host_data:
                                                host_info['ansible_port'] = host_data['ansible_port']
                                        group_hosts[host] = host_info
                                if group_hosts:
                                    hosts[group] = group_hosts
            except Exception as e:
                print(f"Error reading {file}: {str(e)}")
    return hosts