#include <map>
#include <vector>

struct OrderBook {
    std::map<double, double> bids;
    std::map<double, double> asks;
};

double find_arb_spread(const OrderBook& binance, const OrderBook& ftx) {
    auto best_bid = binance.bids.rbegin()->first;
    auto best_ask = ftx.asks.begin()->first;
    return best_ask - best_bid; // Positive = arbitrage
}
