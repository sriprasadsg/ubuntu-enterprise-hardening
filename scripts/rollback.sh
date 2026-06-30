#!/usr/bin/env bash
set -euo pipefail
backup_dir="${1:-/var/backups/ansible-harden}"
find "$backup_dir" -type f | while read -r file; do
  target="${file#${backup_dir}/}"
  if [ -f "$file" ]; then
    install -m 0600 "$file" "$target"
  fi
done
