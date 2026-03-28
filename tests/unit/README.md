# infra-terraform - Terraform Infrastructure as Code

"""
This repository contains Terraform configurations for the infrastructure of the project.
The configurations are organized by environment and module, with a clear separation of concerns.
"""

import os
import json

# Load environment variables
with open('config.json') as f:
    config = json.load(f)

# Define the Terraform workspace
workspace = os.environ.get('TF_WORKSPACE', 'default')

# Define the Terraform backend configuration
backend_config = {
    'backend': 'azurerm',
    'resource_group_name': config['resource_group_name'],
    'storage_account_name': config['storage_account_name'],
    'container_name': config['container_name'],
    'key': config['key']
}

# Print the Terraform backend configuration
print('Terraform backend configuration:')
print(json.dumps(backend_config, indent=4))

# Define the Terraform version
terraform_version = '1.2.3'

# Print the Terraform version
print(f'Terraform version: {terraform_version}')