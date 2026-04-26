"""
SPINE Framework — Generate All Documents
Generates all coaching documents:
  1. Intake & Welcome
  2. SPINE Self-Map Assessment
  3. Coach's Guide & Practice Catalog
  4. Retreat Agenda
"""

import os
import sys
import time


def main():
    output_dir = os.path.join(os.path.dirname(__file__), "documents")
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n{'='*50}")
    print("  SPINE Document Generator")
    print(f"{'='*50}\n")

    start = time.time()
    results = []

    # 1. Intake & Welcome
    print("[1/4] Intake & Welcome")
    try:
        from generate_intake import generate_intake
        path = generate_intake(output_dir)
        print(f"  [OK] {path}\n")
        results.append(("Intake & Welcome", True))
    except Exception as e:
        print(f"  [ERR] {e}\n")
        import traceback
        traceback.print_exc()
        results.append(("Intake & Welcome", False))

    # 2. SPINE Assessment
    print("[2/4] SPINE Self-Map Assessment")
    try:
        from generate_assessment import generate_assessment
        path = generate_assessment(output_dir)
        print(f"  [OK] {path}\n")
        results.append(("Assessment", True))
    except Exception as e:
        print(f"  [ERR] {e}\n")
        import traceback
        traceback.print_exc()
        results.append(("Assessment", False))

    # 3. Coach's Guide
    print("[3/4] Coach's Guide & Practice Catalog")
    try:
        from generate_coaches_guide import generate_coaches_guide
        path = generate_coaches_guide(output_dir)
        print(f"  [OK] {path}\n")
        results.append(("Coach's Guide", True))
    except Exception as e:
        print(f"  [ERR] {e}\n")
        import traceback
        traceback.print_exc()
        results.append(("Coach's Guide", False))

    # 4. Retreat Agenda
    print("[4/4] Retreat Agenda")
    try:
        from generate_retreat import generate_retreat
        path = generate_retreat(output_dir)
        print(f"  [OK] {path}\n")
        results.append(("Retreat Agenda", True))
    except Exception as e:
        print(f"  [ERR] {e}\n")
        import traceback
        traceback.print_exc()
        results.append(("Retreat Agenda", False))

    elapsed = time.time() - start

    print(f"{'='*50}")
    print(f"  Results:")
    for name, ok in results:
        status = "OK" if ok else "FAILED"
        print(f"    [{status}] {name}")
    print(f"\n  Generated in {elapsed:.1f}s")
    print(f"  Output: {os.path.abspath(output_dir)}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
