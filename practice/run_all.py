"""Run the checked no-key practice exercises in lesson order.

Run: python practice/run_all.py
Add --include-web for Classes 53 and 57, which start a local demo server.
"""

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "sources" / "pdfs" / "Langchain - class48.pdf"
OFFLINE = [
    ("Classes 30–33", "practice/class30_33_history.py", []),
    ("Class 48", "practice/class48_documents.py", []),
    ("Class 49", "practice/class49_text_loader.py", []),
    ("Classes 50–51", "practice/class50_51_pdf_loader.py", []),
    ("Class 52", "practice/class52_csv_loader.py", []),
    ("Class 54", "practice/class54_custom_text_loader.py", []),
    ("Class 55", "practice/class55_pdf_core.py", [str(PDF)]),
    ("Class 56", "practice/class56_csv_core.py", []),
    ("Class 58", "practice/class58_metadata.py", []),
    ("Class 60", "text-splitting/programs/class_60_five_programs.py", []),
    ("Class 62", "text-splitting/programs/class_62_eight_programs.py", []),
]
WEB = [
    ("Class 53", "practice/class53_web_loader.py", []),
    ("Class 57", "practice/class57_web_documents.py", []),
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-web", action="store_true")
    args = parser.parse_args()
    exercises = OFFLINE + (WEB if args.include_web else [])
    for label, script, arguments in exercises:
        print(f"\n=== {label}: {script} ===", flush=True)
        subprocess.run(
            [sys.executable, str(ROOT / script), *arguments],
            cwd=ROOT,
            check=True,
        )
    print(f"\nCompleted {len(exercises)} practice files.")
