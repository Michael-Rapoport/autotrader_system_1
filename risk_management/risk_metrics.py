# risk_management/risk_metrics.py
import numpy as np
from scipy.stats import norm

def calculate_value_at_risk(returns, confidence_level=0.95):
    mean = returns.mean()
    std_dev = returns.std()
    value_at_risk = norm.ppf(confidence_level, mean, std_dev)
    return value_at_risk

def calculate_expected_shortfall(returns, confidence_level=0.95):
    mean = returns.mean()
    std_dev = returns.std()
    value_at_risk = calculate_value_at_risk(returns, confidence_level)
    expected_shortfall = (norm.pdf(value_at_risk, mean, std_dev) / (1 - confidence_level)) * (value_at_risk - mean)
    return expected_shortfall

