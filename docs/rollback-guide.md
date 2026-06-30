# Rollback Guide

1. Review the backup directory `/var/backups/ansible-harden`.
2. Run `ansible-playbook playbooks/rollback.yml -i inventories/production/hosts.yml`.
3. Reboot or restart impacted services if needed.
4. Re-run the hardening playbook after validation.
