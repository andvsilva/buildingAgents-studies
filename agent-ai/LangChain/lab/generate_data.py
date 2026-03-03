import os
import random
from datetime import datetime, timezone

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

retention_periods = ["5 years", "7 years", "10 years"]
encryption_types = ["AES-256", "RSA-2048"]
monitoring_methods = ["rule-based engine", "machine learning risk model", "hybrid rules + ML"]
risk_levels = ["Low", "Medium", "High"]

def generate_financial_compliance_policy():

    encryption = random.choice(encryption_types)
    retention = random.choice(retention_periods)
    monitoring = random.choice(monitoring_methods)
    risk_level = random.choice(risk_levels)

    return f"""
FINANCIAL REGTECH COMPLIANCE POLICY
Organization: TechCorp Digital Bank
Department: Compliance & Risk
Created: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
Jurisdiction: Global Financial Operations

======================================================================
1. PURPOSE
======================================================================
This policy establishes regulatory compliance requirements for customer
data protection, Anti-Money Laundering (AML), Know Your Customer (KYC),
sanctions screening, transaction monitoring, and regulatory reporting.

The objective is to ensure full compliance with applicable financial
regulations and supervisory authorities.

======================================================================
2. REGULATORY FRAMEWORK
======================================================================
This policy aligns with:

- AML (Anti-Money Laundering) directives
- FATF Recommendations
- Basel III capital standards
- GDPR (Data Protection Regulation)
- SOC 2 Type II
- ISO 27001
- Local regulations issued by financial authorities
- Requirements established by Banco Central do Brasil (where applicable)

======================================================================
3. CUSTOMER DUE DILIGENCE (CDD)
======================================================================
All customers must undergo identity verification procedures including:

- KYC (Know Your Customer)
- Beneficial Ownership identification (UBO)
- Politically Exposed Person (PEP) screening
- Risk classification

Each customer is assigned a risk score categorized as: {risk_level}

Enhanced Due Diligence (EDD) must be performed for High-risk customers.

======================================================================
4. SANCTIONS & PEP SCREENING
======================================================================
Customer identities must be screened against:

- Global sanctions lists
- Terrorism watchlists
- Politically Exposed Person databases

Screening must occur:
- During onboarding
- On a continuous monitoring basis

All screening decisions must be documented and auditable.

======================================================================
5. DATA SECURITY & ENCRYPTION
======================================================================
All Confidential and Personally Identifiable Information (PII) must be:

- Encrypted at rest using {encryption}
- Encrypted in transit using TLS 1.3
- Stored in access-controlled environments

Access must follow Role-Based Access Control (RBAC) principles.
All access events must be logged and retained for audit purposes.

======================================================================
6. TRANSACTION MONITORING (AML)
======================================================================
All financial transactions must be analyzed using a {monitoring}.

Monitoring must detect:

- Structuring behavior
- Unusual transaction velocity
- High-risk geographies
- Behavioral anomalies

Alerts must be reviewed within defined SLA timelines.
False positives must be documented and analyzed.

======================================================================
7. SUSPICIOUS ACTIVITY REPORTING (SAR/STR)
======================================================================
If suspicious activity is confirmed:

- A formal SAR/STR must be filed
- Reporting deadlines must comply with regulatory timelines
- Case documentation must include investigation rationale

All reports must be securely archived for {retention}.

======================================================================
8. MODEL GOVERNANCE & EXPLAINABILITY
======================================================================
If machine learning models are used:

- Model logic must be explainable
- Risk factors must be documented
- Periodic validation must be performed
- Bias and fairness assessments must be conducted

Model performance metrics must be retained for audit review.

======================================================================
9. DATA RETENTION & PRIVACY
======================================================================
Customer financial data must be retained for {retention}.

Data deletion must follow regulatory and legal hold requirements.
All retention schedules must align with AML and data protection laws.

======================================================================
10. INCIDENT RESPONSE
======================================================================
In case of security or compliance breach:

- Notify Compliance Officer within 24 hours
- Initiate incident response procedures
- Notify regulator if required
- Notify affected customers within statutory deadlines

All incidents must be logged in the central compliance system.

======================================================================
11. GOVERNANCE & OVERSIGHT
======================================================================
The Chief Compliance Officer (CCO) is responsible for:

- Policy enforcement
- Regulatory liaison
- Internal audits
- Training programs
- Third-party risk management

Periodic independent audits must be conducted annually.

======================================================================
END OF POLICY DOCUMENT
======================================================================
"""

def generate_documents(n=30):
    for i in range(n):
        content = generate_financial_compliance_policy()
        filename = f"financial_compliance_policy_{i+1}.txt"

        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(content)

        print("Created:", filename)

if __name__ == "__main__":
    generate_documents(30)