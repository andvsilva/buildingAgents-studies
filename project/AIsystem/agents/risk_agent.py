from agents.base_agent import BaseAgent

class RiskAgent(BaseAgent):
    def analyze(self, portfolio: str) -> str:
        return self.act(
            f"Analyze the risk of the following investment portfolio:\n{portfolio}"
        )
