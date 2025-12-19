import numpy as np

def volatility(returns):
    return np.std(returns)

def value_at_risk(returns, confidence=0.95):
    return np.percentile(returns, (1 - confidence) * 100)
