from agents.risk_agent import RiskAgent
from agents.strategy_agent import StrategyAgent
from agents.report_agent import ReportAgent
from tools.data_loader import load_mock_returns
from memory.memory import SharedMemory

def run_pipeline():
    memory = SharedMemory()

    risk_agent = RiskAgent("Risk Analyst", "Analyze portfolio risk")
    strategy_agent = StrategyAgent("Strategy Advisor", "Suggest allocation")
    report_agent = ReportAgent("Report Writer", "Summarize insights")

    returns = load_mock_returns()

    risk_report = risk_agent.analyze(returns)
    memory.write("risk", risk_report)

    strategy = strategy_agent.recommend(risk_report)
    memory.write("strategy", strategy)

    report = report_agent.generate(risk_report, strategy)
    memory.write("final_report", report)

    return report
