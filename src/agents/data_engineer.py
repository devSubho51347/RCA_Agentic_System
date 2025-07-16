from crewai import Agent
import pandas as pd
from pathlib import Path

class DataEngineerAgent(Agent):
    """Executes analysis plans and produces outputs."""

    def execute_plan(self, plan_code: str, output_dir: Path):
        output_dir.mkdir(parents=True, exist_ok=True)
        # A very naive exec – replace with sandboxed execution in real use
        local_vars = {'pd': pd, 'output_dir': output_dir}
        try:
            exec(plan_code, {}, local_vars)
            return {"status": "success"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
