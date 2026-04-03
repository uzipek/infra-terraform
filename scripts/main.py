import os
import sys
import argparse
from pathlib import Path
from terraform_runner import TerraformRunner

def parse_args():
    parser = argparse.ArgumentParser(description="Manage Terraform infrastructure.")
    parser.add_argument('action', choices=['plan', 'apply', 'destroy'], help="Action to perform.")
    parser.add_argument('--env', required=True, help="Environment to target.")
    parser.add_argument('--var-file', default='terraform.tfvars', help="Path to variables file.")
    return parser.parse_args()

def validate_env(env):
    valid_envs = ['dev', 'staging', 'prod']
    if env not in valid_envs:
        print(f"Error: Invalid environment '{env}'. Valid options are {valid_envs}.")
        sys.exit(1)

def main():
    args = parse_args()
    validate_env(args.env)

    tf_runner = TerraformRunner(env=args.env, var_file=args.var_file)

    if args.action == 'plan':
        tf_runner.plan()
    elif args.action == 'apply':
        tf_runner.apply()
    elif args.action == 'destroy':
        tf_runner.destroy()

if __name__ == "__main__":
    main()