from core.strategy import Strategy

class TaxReportingStrategy(Strategy):
    """
    Generates jurisdiction‑specific tax forms
    (US‑IRS Form 8949, EU templates, etc.).
    """
    def __init__(self, jurisdiction: str, year: int):
        self.jurisdiction = jurisdiction
        self.year = year

    def execute(self, transactions: list) -> str:
        # Export CSV/PDF per jurisdiction rules
        pass
