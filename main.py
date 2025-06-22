"""Main entry point for Royen Bitcoin Analytic."""
import argparse
import logging
from src.mempool import MempoolMonitor
from src.onchain import OnChainAnalyzer
from src.visualizer import Visualizer
from src.notifier import Notifier
from src.config import load_config, load_settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    """Initialize and run Royen Bitcoin Analytic."""
    parser = argparse.ArgumentParser(description="Royen Bitcoin Analytic")
    parser.add_argument("--config", default="config.json", help="Path to config file")
    parser.add_argument("--settings", default="settings.yaml", help="Path to settings file")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        settings = load_settings(args.settings)
        logger.info("Configuration and settings loaded successfully")

        mempool = MempoolMonitor(config, settings)
        onchain = OnChainAnalyzer(config, settings)
        visualizer = Visualizer(settings)
        notifier = Notifier(config, settings)

        logger.info("Starting Royen Bitcoin Analytic")
        mempool.start_monitoring()
        onchain.start_analysis()
        visualizer.render_dashboard()
        notifier.send_welcome_message()

        # Main loop (simplified for demo)
        while True:
            pass  # Replace with async event loop in production

    except Exception as e:
        logger.error(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()
