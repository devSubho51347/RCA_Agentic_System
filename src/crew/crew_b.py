from pathlib import Path
from src.agents.data_architect import DataArchitectAgent
from src.agents.data_engineer import DataEngineerAgent

class CrewB:
    def __init__(self):
        self.architect = DataArchitectAgent()
        self.engineer = DataEngineerAgent()

    def run(self, subquestions: list[str], knowledge_dir: Path, plan_dir: Path, results_dir: Path):
        schema_md = (knowledge_dir / "data.md").read_text()
        viz_md = (knowledge_dir / "visualisation_best_practices.md").read_text()

        plan_dir.mkdir(parents=True, exist_ok=True)
        results_dir.mkdir(parents=True, exist_ok=True)

        for idx, subq in enumerate(subquestions, 1):
            plan_md, code = self.architect.create_plan(subq, schema_md, viz_md, "C:\\Users\\choud\\CascadeProjects\\RCA_Agentic_System\\data\\")
            subq_id = f"subq_{idx}"
            plan_path = plan_dir / f"{subq_id}_plan.md"
            plan_path.write_text(plan_md + "\n\n```python\n" + code + "\n```")

            # execute plan
            exec_result = self.engineer.execute_plan(code, results_dir / subq_id)
            # simple manifest
            manifest_path = results_dir / f"{subq_id}_manifest.md"
            manifest_path.write_text(str(exec_result))
