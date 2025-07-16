import argparse
from pathlib import Path
from src.crew.crew_a import CrewA
from src.crew.crew_b import CrewB

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
OUTPUT_PLAN_DIR = BASE_DIR / "output" / "plan"
OUTPUT_RESULTS_DIR = BASE_DIR / "output" / "results"


def main():
    parser = argparse.ArgumentParser(description="Run RCA Agent pipeline")
    parser.add_argument("question", nargs="?", default="Why has the reorder rate dropped in the snacks department over the last quarter?", help="High-level RCA question")
    args = parser.parse_args()

    crew_a = CrewA()
    crew_b = CrewB()

    print("Running Crew A – Generating sub-questions…")
    subs = crew_a.run(args.question, KNOWLEDGE_DIR, OUTPUT_PLAN_DIR)
    print("Generated sub-questions:")
    for s in subs:
        print(" -", s)

    print("\nRunning Crew B – Executing analysis plans…")
    crew_b.run(subs, KNOWLEDGE_DIR, OUTPUT_PLAN_DIR, OUTPUT_RESULTS_DIR)
    print("Done. Check output/ for results.")


if __name__ == "__main__":
    main()
