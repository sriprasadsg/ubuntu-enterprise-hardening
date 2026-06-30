from pathlib import Path
import unittest


class ComplianceRoleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(__file__).resolve().parents[1]

    def test_ssh_role_template_enforces_strong_defaults(self) -> None:
        template_path = self.repo_root / "roles" / "ssh" / "templates" / "sshd_config.j2"
        self.assertTrue(template_path.exists(), "SSH hardening template should exist")
        content = template_path.read_text(encoding="utf-8")
        self.assertIn("PermitRootLogin no", content)
        self.assertIn("PasswordAuthentication no", content)
        self.assertIn("KexAlgorithms", content)

    def test_firewall_role_template_enforces_default_deny(self) -> None:
        template_path = self.repo_root / "roles" / "firewall" / "templates" / "ufw.rules.j2"
        self.assertTrue(template_path.exists(), "Firewall template should exist")
        content = template_path.read_text(encoding="utf-8")
        self.assertIn("DEFAULT_FORWARD_POLICY=\"DROP\"", content)
        self.assertIn("DEFAULT_INPUT_POLICY=\"DROP\"", content)

    def test_sysctl_role_template_enforces_kernel_hardening(self) -> None:
        template_path = self.repo_root / "roles" / "sysctl" / "templates" / "99-hardening.conf.j2"
        self.assertTrue(template_path.exists(), "Sysctl template should exist")
        content = template_path.read_text(encoding="utf-8")
        self.assertIn("kernel.randomize_va_space", content)
        self.assertIn("net.ipv4.ip_forward", content)

    def test_apparmor_role_template_exists(self) -> None:
        template_path = self.repo_root / "roles" / "apparmor" / "templates" / "apparmor.conf.j2"
        self.assertTrue(template_path.exists(), "AppArmor template should exist")
        content = template_path.read_text(encoding="utf-8")
        self.assertIn("# Managed by Ansible", content)


if __name__ == "__main__":
    unittest.main()
