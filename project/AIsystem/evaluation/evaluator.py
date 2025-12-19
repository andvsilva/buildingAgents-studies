def evaluate_report(report):
    checks = {
        "clarity": "clear" in report.lower(),
        "risk": "risk" in report.lower(),
        "strategy": "strategy" in report.lower()
    }
    return checks
