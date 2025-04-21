from connectors.wallet_connect_connector import WalletConnectConnector
from services.data_sync_service import DataSyncService

def main():
    wc = WalletConnectConnector()
    session = wc.connect()
    sync = DataSyncService([wc], interval=60)
    sync.start()

if __name__ == "__main__":
    main()
