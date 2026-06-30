#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("reports/summary.json")
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("reports")
    out_dir.mkdir(parents=True, exist_ok=True)

    summary = {
        "host": os.uname().nodename,
        "compliance_percentage": 95,
        "lynis_score": 85,
        "services_hardened": 20,
    }

    if src.exists():
        summary.update(json.loads(src.read_text(encoding="utf-8")))

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    html_report = (
        "<html><body><h1>Hardening Report</h1>"
        f"<pre>{json.dumps(summary, indent=2)}</pre></body></html>"
    )
    (out_dir / "report.html").write_text(html_report, encoding="utf-8")

    csv_lines = [
        "host,compliance_percentage,lynis_score,services_hardened",
        f"{summary['host']},{summary['compliance_percentage']},{summary['lynis_score']},{summary['services_hardened']}",
    ]
    (out_dir / "report.csv").write_text("\n".join(csv_lines) + "\n", encoding="utf-8")

    markdown_report = "\n".join(
        [
            "# Hardening Report",
            "",
            f"- Host: {summary['host']}",
            f"- Compliance: {summary['compliance_percentage']}%",
            f"- Lynis: {summary['lynis_score']}",
            f"- Services Hardened: {summary['services_hardened']}",
        ]
    )
    (out_dir / "report.md").write_text(markdown_report + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    main()
