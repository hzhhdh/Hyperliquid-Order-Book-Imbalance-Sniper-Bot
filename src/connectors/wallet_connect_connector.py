from walletconnect import WalletConnectClient

class WalletConnectConnector:
    """Handles WalletConnect sessions via QR code or deep link."""
    def __init__(self, bridge_url: str = "https://bridge.walletconnect.org"):
        self.client = WalletConnectClient(bridge=bridge_url)

    def connect(self):
        session = self.client.connect()
        return session.accounts, session.chain_id
