from crewai import Agent
import os
from openai import OpenAI

class RCAAnalystAgent(Agent):
    """Parses high-level RCA questions and generates sub-questions via LLM."""

    def __init__(self, model: str = "gpt-3.5-turbo"):
        super().__init__(role="RCA Analyst", goal="Generate RCA sub-questions", backstory="Expert analyst breaking down complex business questions into actionable sub-questions.")
        # self.model = model

    def generate_subquestions(self, question: str, schema_markdown: str, n_subq: int = 2):
        """Generate sub-questions using the LLM."""
        prompt = (
            "You are an RCA analyst. Given the table schemas below and an RCA question, "
            "produce a bullet list of {} sub-questions that, when answered, collectively "
            "resolve the RCA.\n\nSchemas:\n{}\n\nRCA question: {}\n\nSub-questions:".format(n_subq, schema_markdown, question)
        )
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model= "gpt-4o-mini",
                messages=[{"role": "system", "content": "You are an expert data analyst."},
                          {"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=512
            )
            content = response.choices[0].message.content.strip()
            subs = [line.lstrip("- ") for line in content.splitlines() if line.strip()]
            return subs[:n_subq]
        except Exception:
            # Fallback to placeholder sub-questions
            return [f"Sub-question {i+1} for: {question}" for i in range(n_subq)]
