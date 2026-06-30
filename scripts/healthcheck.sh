#!/usr/bin/env bash
set -euo pipefail
services=(ssh docker containerd squid NetworkManager auditd fail2ban ufw apparmor)
for svc in "${services[@]}"; do
  if systemctl list-unit-files | grep -q "^${svc}\.service"; then
    systemctl is-active --quiet "$svc" || echo "$svc is not active"
  fi
done
