from orchestrator.orchestrator import run_pipeline
from evaluation.evaluator import evaluate_report


if __name__ == "__main__":
    report = run_pipeline()
    evaluation = evaluate_report(report)

    print("\nFINAL REPORT\n")
    print(report)

    print("\nEVALUATION\n")
    print(evaluation)
