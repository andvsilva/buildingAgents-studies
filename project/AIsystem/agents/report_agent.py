from agents.base_agent import BaseAgent

class ReportAgent(BaseAgent):
    def summarize(self, strategy: str) -> str:
        return self.act(
            f"Summarize the following strategy for stakeholders:\n{strategy}"
        )
