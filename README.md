# Ubuntu Enterprise Hardening Framework

This repository provides an enterprise-grade Ansible framework for hardening Ubuntu 24.04 Desktop and Server environments with modular roles, backup-aware configuration management, AWX support, rollback workflows, reporting, and health verification.

## Included capabilities

- Ubuntu 24.04 Desktop and Server support
- CIS-oriented baseline hardening
- OpenSCAP and Lynis integration hooks
- AppArmor, AIDE, Auditd, Fail2Ban, SSH, firewall, kernel, sysctl, and service hardening
- Docker, containerd, Squid, SSSD, GDM, NetworkManager, ModemManager, CUPS, Bluetooth, and USBGuard roles
- AWX-ready inventory and playbooks
- Rollback playbook and backup directory handling
- HTML, JSON, CSV, and Markdown reporting
- GitHub Actions and GitLab CI examples

## Quick start

1. Install prerequisites:
   ```bash
   python3 -m pip install --user ansible ansible-lint yamllint
   ansible-galaxy collection install -r requirements.yml
   ```
2. Review inventory and variables:
   - [inventories/production/hosts.yml](inventories/production/hosts.yml)
   - [group_vars/all.yml](group_vars/all.yml)
3. Apply the hardening playbook:
   ```bash
   ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbooks/harden.yml -i inventories/production/hosts.yml
   ```
4. Review artifact outputs in [reports](reports).

## Common commands

### Install and bootstrap
```bash
python3 -m pip install --user ansible ansible-lint yamllint
ansible-galaxy collection install -r requirements.yml
```

### Dry run and syntax validation
```bash
ANSIBLE_CONFIG=ansible.cfg ansible-playbook --check playbooks/harden.yml -i inventories/production/hosts.yml
ANSIBLE_CONFIG=ansible.cfg ansible-playbook --syntax-check playbooks/harden.yml -i inventories/production/hosts.yml
```

### Apply hardening
```bash
ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbooks/harden.yml -i inventories/production/hosts.yml
```

### Roll back changes
```bash
ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbooks/rollback.yml -i inventories/production/hosts.yml
```

### Run tests
```bash
python3 -m unittest -v tests.test_generate_reports
python3 -m unittest -v tests.test_compliance_roles
```

### Generate reports manually
```bash
python3 scripts/generate_reports.py /tmp/hardening-summary.json reports
```

### Health checks
```bash
bash scripts/healthcheck.sh
```

### AWX / automation platform usage
```bash
ANSIBLE_CONFIG=ansible.cfg ansible-playbook playbooks/harden.yml -i inventories/awx/hosts.yml
```

## Documentation

- [docs/architecture.md](docs/architecture.md)
- [docs/upgrade-guide.md](docs/upgrade-guide.md)
- [docs/rollback-guide.md](docs/rollback-guide.md)
- [docs/awx-guide.md](docs/awx-guide.md)
- [docs/troubleshooting.md](docs/troubleshooting.md)
- [docs/service-matrix.md](docs/service-matrix.md)
- [docs/compatibility-matrix.md](docs/compatibility-matrix.md)
- [docs/awx-survey-examples.yml](docs/awx-survey-examples.yml)

## AWX support

The repository is prepared for AWX with:

- Inventory examples in [inventories/awx/hosts.yml](inventories/awx/hosts.yml)
- Job template playbook [playbooks/harden.yml](playbooks/harden.yml)
- Rollback playbook [playbooks/rollback.yml](playbooks/rollback.yml)
- Survey variables in [docs/awx-survey-examples.yml](docs/awx-survey-examples.yml)
