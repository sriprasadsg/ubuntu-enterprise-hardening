# Upgrade Guide

1. Pull the latest repository changes.
2. Review inventory and group variables.
3. Run `ansible-playbook playbooks/harden.yml -i inventories/production/hosts.yml`.
4. Review generated reports under `reports/`.
