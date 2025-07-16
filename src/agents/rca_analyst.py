from crewai import Agent

class RCAAnalystAgent(Agent):
    """Parses high-level RCA questions and generates sub-questions."""

    def generate_subquestions(self, question: str, schema_markdown: str, n_subq: int = 3):
        """Stub method – will call LLM via CrewAI later."""
        # TODO: integrate LLM chain here
        return [f"Sub-question {i+1} for: {question}" for i in range(n_subq)]
