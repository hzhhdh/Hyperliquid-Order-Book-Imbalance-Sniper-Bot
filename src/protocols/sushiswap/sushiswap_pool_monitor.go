package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type PoolData struct {
    Liquidity float64 `json:"liquidity"`
    Volume    float64 `json:"volume"`
}

type SushiSwapPoolMonitor struct {
    apiUrl string
    logger *log.Logger
}

func NewSushiSwapPoolMonitor(apiUrl string) *SushiSwapPoolMonitor {
    return &SushiSwapPoolMonitor{
        apiUrl: apiUrl,
        logger: log.New(log.Default().Writer(), "SushiSwap: ", log.LstdFlags),
    }
}

func (m *SushiSwapPoolMonitor) FetchPoolData(poolId string) (PoolData, error) {
    resp, err := http.Get(m.apiUrl + "/pools/" + poolId)
    if err != nil {
        m.logger.Printf("Error fetching pool data: %v", err)
        return PoolData{}, err
    }
    defer resp.Body.Close()

    var data PoolData
    if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
        m.logger.Printf("Error decoding pool data: %v", err)
        return PoolData{}, err
    }
    return data, nil
}

func main() {
    monitor := NewSushiSwapPoolMonitor("https://api.sushiswap.fi")
    data, err := monitor.FetchPoolData("1")
    if err != nil {
        log.Fatal(err)
    }
    log.Printf("Pool liquidity: %.2f, volume: %.2f", data.Liquidity, data.Volume)
}
