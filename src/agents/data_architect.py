from crewai import Agent

class DataArchitectAgent(Agent):
    """Translates sub-questions into executable analysis plans."""

    def create_plan(self, subquestion: str, schema_markdown: str, viz_guidelines: str):
        """Stub plan generator."""
        # TODO: generate plan via LLM
        plan_md = f"## Plan for: {subquestion}\n- Step 1: Filter dataset\n- Step 2: Aggregate\n- Step 3: Plot bar chart"
        code = """python\n# placeholder code\nimport pandas as pd\n"""
        return plan_md, code
