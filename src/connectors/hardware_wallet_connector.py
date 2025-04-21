from walletconnect.node import NodeWalletConnect
from walletconnect.qrcode import WalletConnectQRCodeModal

class HardwareWalletConnector:
    """Connects to hardware wallets for offline signing."""
    def __init__(self):
        self.connector = NodeWalletConnect({}, {})

    def create_session(self):
        if not self.connector.connected:
            self.connector.create_session()
            WalletConnectQRCodeModal.open(self.connector.uri)
        return self.connector
