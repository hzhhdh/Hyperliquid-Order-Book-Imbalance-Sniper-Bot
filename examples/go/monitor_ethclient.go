package main
import ("fmt"; "github.com/ethereum/go-ethereum/ethclient")
func main(){
  client, _ := ethclient.Dial("https://localhost:8545")
  txs := make(chan *types.Transaction)
  client.SubscribePendingTransactions(context.Background(), txs)
  for tx := range txs { fmt.Println(tx.Hash().Hex()) }
}
