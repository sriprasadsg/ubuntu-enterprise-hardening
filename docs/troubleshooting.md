# Troubleshooting Guide

- Check service state with `systemctl status <service>`.
- Review backups under `/var/backups/ansible-harden`.
- Re-run the rollback playbook when service health fails.
- Inspect report artifacts under `reports/`.
