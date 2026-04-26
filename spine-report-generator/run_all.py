"""
SPINE Framework — Generate Everything
Run this script to generate all PDF outputs:
  - Client reports (4 case studies)
  - Coaching documents (intake, assessment, guide, retreat)
"""

import os
import sys
import time
from clients_data import get_all_clients
from generate_report import generate_report


def generate_client_reports():
    """Generate all 4 client reports."""
    output_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(output_dir, exist_ok=True)

    clients = get_all_clients()
    print(f"\n  Client Reports ({len(clients)} clients)")
    print(f"  {'-'*40}")

    for name, data in clients.items():
        print(f"  [{name.upper()}]", end=" ")
        try:
            generate_report(data, output_dir)
            print("[OK]")
        except Exception as e:
            print(f"[ERR] {e}")
            import traceback
            traceback.print_exc()

    return output_dir


def generate_documents():
    """Generate all coaching documents."""
    output_dir = os.path.join(os.path.dirname(__file__), "documents")
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n  Coaching Documents")
    print(f"  {'-'*40}")

    docs = [
        ("Intake & Welcome", "generate_intake", "generate_intake"),
        ("SPINE Assessment", "generate_assessment", "generate_assessment"),
        ("Coach's Guide", "generate_coaches_guide", "generate_coaches_guide"),
        ("Retreat Agenda", "generate_retreat", "generate_retreat"),
    ]

    for label, module_name, func_name in docs:
        print(f"  [{label}]", end=" ")
        try:
            module = __import__(module_name)
            func = getattr(module, func_name)
            func(output_dir)
            print("[OK]")
        except Exception as e:
            print(f"[ERR] {e}")


def main():
    print(f"\n{'='*50}")
    print("  SPINE Framework — Full Generation")
    print(f"{'='*50}")

    start = time.time()

    # Parse args
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"

    if mode in ("all", "reports"):
        reports_dir = generate_client_reports()

    if mode in ("all", "documents", "docs"):
        generate_documents()

    elapsed = time.time() - start
    print(f"\n{'='*50}")
    print(f"  Complete in {elapsed:.1f}s")
    if mode in ("all", "reports"):
        print(f"  Reports: {os.path.abspath(reports_dir)}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
