import json
import subprocess
import tempfile
import unittest
from pathlib import Path


class GenerateReportsTest(unittest.TestCase):
    def test_generates_html_json_csv_and_markdown_reports(self):
        repo_root = Path(__file__).resolve().parents[1]
        script_path = repo_root / "scripts" / "generate_reports.py"

        with tempfile.TemporaryDirectory(dir=repo_root) as tmp_dir:
            tmp_path = Path(tmp_dir)
            summary_path = tmp_path / "summary.json"
            summary_path.write_text(json.dumps({"host": "test-host", "compliance_percentage": 98, "lynis_score": 88, "services_hardened": 25}), encoding="utf-8")

            result = subprocess.run(
                ["python3", str(script_path), str(summary_path), str(tmp_path / "reports")],
                cwd=repo_root,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, msg=result.stderr)
            self.assertTrue((tmp_path / "reports" / "report.html").exists())
            self.assertTrue((tmp_path / "reports" / "report.csv").exists())
            self.assertTrue((tmp_path / "reports" / "report.md").exists())
            self.assertTrue((tmp_path / "reports" / "summary.json").exists())

            html = (tmp_path / "reports" / "report.html").read_text(encoding="utf-8")
            csv_text = (tmp_path / "reports" / "report.csv").read_text(encoding="utf-8")
            markdown = (tmp_path / "reports" / "report.md").read_text(encoding="utf-8")

            self.assertIn("Hardening Report", html)
            self.assertIn("test-host", csv_text)
            self.assertIn("test-host", markdown)
            self.assertIn("98", csv_text)


if __name__ == "__main__":
    unittest.main()
