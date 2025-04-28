package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type TreasuryRebalancer struct {
    apiUrl string
    logger *log.Logger
}

type AssetPrice struct {
    Symbol string  `json:"symbol"`
    Price  float64 `json:"price"`
}

func NewTreasuryRebalancer(apiUrl string) *TreasuryRebalancer {
    return &TreasuryRebalancer{
        apiUrl: apiUrl,
        logger: log.New(log.Default().Writer(), "TreasuryRebalancer: ", log.LstdFlags),
    }
}

func (r *TreasuryRebalancer) FetchPrice(symbol string) (float64, error) {
    resp, err := http.Get(r.apiUrl + "?symbol=" + symbol)
    if err != nil {
        r.logger.Printf("Error fetching price for %s: %v", symbol, err)
        return 0, err
    }
    defer resp.Body.Close()

    var price AssetPrice
    if err := json.NewDecoder(resp.Body).Decode(&price); err != nil {
        r.logger.Printf("Error decoding price: %v", err)
        return 0, err
    }
    return price.Price, nil
}

func (r *TreasuryRebalancer) Rebalance(assets map[string]float64, targetRatios map[string]float64) {
    totalValue := 0.0
    for symbol, amount := range assets {
        price, err := r.FetchPrice(symbol)
        if err != nil {
            r.logger.Printf("Skipping %s: %v", symbol, err)
            continue
        }
        totalValue += amount * price
    }
    for symbol, target := range targetRatios {
        currentValue := assets[symbol] * r.FetchPrice(symbol)
        targetValue := totalValue * target
        if currentValue > targetValue * 1.1 {
            // TODO: Swap excess to other assets
            r.logger.Printf("Rebalancing %s: reduce by %f", symbol, currentValue-targetValue)
        }
    }
}

func main() {
    rebalancer := NewTreasuryRebalancer("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest")
    assets := map[string]float64{"ETH": 10, "USDC": 5000}
    ratios := map[string]float64{"ETH": 0.3, "USDC": 0.7}
    rebalancer.Rebalance(assets, ratios)
}
