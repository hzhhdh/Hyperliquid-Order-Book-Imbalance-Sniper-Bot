from brownie import interface, network, accounts

def main():
    acct = accounts.load('deployer')
    # 1. Flash loan contract interface
    flash = interface.IFlashLoan("0xAAVE_LENDING_POOL_ADDRESS")
    # 2. Borrow 100 ETH
    flash.flashLoan(acct, [network.WETH], [w3.to_wei(100, 'ether')], [0], acct.address, b"", 0)
    # 3. Inside callback, swap ETH→stETH on Curve
    curve = interface.ICurvePool("0xCURVE_POOL_ADDRESS")
    curve.exchange(0, 1, w3.to_wei(100, 'ether'), 0, {'from': acct})
    # 4. Repay flash loan automatically when function ends
    print("Flash loan + swap complete")
