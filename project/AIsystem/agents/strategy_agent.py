from agents.base_agent import BaseAgent

class StrategyAgent(BaseAgent):
    def recommend(self, risk_report: str) -> str:
        return self.act(
            f"Based on the following risk report, recommend a strategy:\n{risk_report}"
        )
