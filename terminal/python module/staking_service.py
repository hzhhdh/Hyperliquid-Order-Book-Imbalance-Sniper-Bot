# staking_service.py
def calculate_leverage(collateral: float, ltv: float):
    max_loan = collateral * ltv
    return {
        "collateral": collateral,
        "max_loan": max_loan,
        "liquidation_price": collateral * 0.9  # Example
    }
