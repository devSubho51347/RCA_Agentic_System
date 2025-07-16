from src.agents.rca_analyst import RCAAnalystAgent
from pathlib import Path

class CrewA:
    def __init__(self):
        self.agent = RCAAnalystAgent()

    def run(self, question: str, knowledge_dir: Path, output_dir: Path):
        schema_md = (knowledge_dir / "data.md").read_text()
        subs = self.agent.generate_subquestions(question, schema_md)
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "rca_subquestions.md").write_text("\n".join(f"- {s}" for s in subs))
        return subs
