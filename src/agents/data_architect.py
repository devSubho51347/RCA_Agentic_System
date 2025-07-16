from crewai import Agent
import os
from openai import OpenAI

class DataArchitectAgent(Agent):
    """Translates sub-questions into executable analysis plans."""

    def __init__(self, model: str = "gpt-3.5-turbo"):
        super().__init__(role="Lead Data Architect", goal="Translate RCA sub-questions into executable plans", backstory="Veteran data architect with expertise in analytics and visualization best practices.")
        # self.model = model

    def create_plan(self, subquestion: str, schema_markdown: str, viz_guidelines: str, data_path: str):
        """Generate analysis plan and Python code using LLM."""
        prompt = (
            "You are a senior data architect. Using the dataset schemas and viz guidelines below, "
            "create an analysis plan for the sub-question, then output executable Python code to implement it.\n\n"
            "Schemas:\n{}\n\nViz guidelines:\n{}\n\nData directory path: {}\n\nSub-question: {}\n\n"
            "Respond in Markdown. First section heading ## Plan with bullet steps, then a section heading ## Code with a valid Python code block.".format(
                schema_markdown, viz_guidelines, data_path, subquestion)
        )
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            response = client.chat.completions.create(
                model= "gpt-4o-mini",
                messages=[{"role": "system", "content": "You are an expert data architect."},
                          {"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1024
            )
            content = response.choices[0].message.content.strip()
            # crude split
            if "```python" in content:
                md_part, code_part = content.split("```python", 1)
                code =  code_part.split("```", 1)[0]
            else:
                md_part, code = content, "# No code returned"
            return md_part.strip(), code.strip()
        except Exception as e:
            plan_md = f"## Plan for: {subquestion}\n- LLm error: {e}"
            code = "# placeholder";
            return plan_md, code
