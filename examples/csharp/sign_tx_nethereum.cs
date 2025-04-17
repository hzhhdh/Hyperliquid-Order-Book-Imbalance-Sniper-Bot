using Nethereum.Web3.Accounts;
var account = new Account(privateKey);
var web3 = new Web3(account, url);
var tx = await web3.Eth.GetEtherTransferService()
    .TransferEtherAndWaitForReceiptAsync(toAddress, 0.1m);
