import time
from config import CONFIG

metrics = {
    "signals_triggered": 0,
    "orders_executed": 0,
    "execution_failures": 0,
    "average_detection_latency": [],
}

def log_signal_trigger(latency):
    metrics["signals_triggered"] += 1
    metrics["average_detection_latency"].append(latency)
    print(f"Signal triggered. Latency: {latency:.2f} ms.")

def log_order_execution(success: bool):
    if success:
        metrics["orders_executed"] += 1
    else:
        metrics["execution_failures"] += 1

def get_average_latency():
    if metrics["average_detection_latency"]:
        return sum(metrics["average_detection_latency"]) / len(metrics["average_detection_latency"])
    return 0

def display_metrics():
    print("=== Bot Performance Metrics ===")
    print(f"Signals Triggered: {metrics['signals_triggered']}")
    print(f"Orders Executed: {metrics['orders_executed']}")
    print(f"Execution Failures: {metrics['execution_failures']}")
    print(f"Average Detection Latency (ms): {get_average_latency():.2f}")
