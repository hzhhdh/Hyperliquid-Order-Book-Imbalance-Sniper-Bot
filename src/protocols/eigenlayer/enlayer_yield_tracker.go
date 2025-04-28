package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type YieldData struct {
    Yield    float64 `json:"yield"`
    Timestamp int64   `json:"timestamp"`
}

type EigenLayerYieldTracker struct {
    apiUrl string
    logger *log.Logger
}

func NewEigenLayerYieldTracker(apiUrl string) *EigenLayerYieldTracker {
    return &EigenLayerYieldTracker{
        apiUrl: apiUrl,
        logger: log.New(log.Default().Writer(), "EigenLayer: ", log.LstdFlags),
    }
}

func (t *EigenLayerYieldTracker) FetchYield() (YieldData, error) {
    resp, err := http.Get(t.apiUrl)
    if err != nil {
        t.logger.Printf("Error fetching yield: %v", err)
        return YieldData{}, err
    }
    defer resp.Body.Close()

    var data YieldData
    if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
        t.logger.Printf("Error decoding yield: %v", err)
        return YieldData{}, err
    }
    return data, nil
}

func main() {
    tracker := NewEigenLayerYieldTracker("https://api.eigenlayer.io/yield")
    data, err := tracker.FetchYield()
    if err != nil {
        log.Fatal(err)
    }
    log.Printf("Current yield: %.2f%%", data.Yield)
}
