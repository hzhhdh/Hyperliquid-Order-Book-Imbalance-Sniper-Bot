"""Unit tests for mempool module."""
import pytest
from src.mempool import MempoolMonitor

@pytest.fixture
def mempool_monitor():
    config = {"node": {"url": "https://mempool.space/api"}}
    settings = {
        "mempool": {
            "filters": {"min_amount": 0.01, "fee_range": ["medium"], "address_type": ["segwit"]},
            "alerts": {"transaction_size": 10}
        }
    }
    return MempoolMonitor(config, settings)

def test_filter_transactions(mempool_monitor):
    transactions = [
        {"value": 1_000_000_000, "fee_rate": 10, "address_type": "segwit"},  # 1 BTC
        {"value": 500_000, "fee_rate": 5, "address_type": "legacy"}  # 0.005 BTC
    ]
    filtered = mempool_monitor.filter_transactions(transactions)
    assert len(filtered) == 1
    assert filtered[0]["value"] == 1_000_000_000

def test_check_alerts(mempool_monitor):
    transactions = [{"value": 2_000_000_000, "fee_rate": 10, "address_type": "segwit"}]  # 2 BTC
    alerts = mempool_monitor.check_alerts(transactions)
    assert len(alerts) == 0  # No alerts for 2 BTC (threshold is 10 BTC)
