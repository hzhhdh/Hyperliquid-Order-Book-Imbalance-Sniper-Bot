#include <chrono>
#include <unistd.h>

void snipe_token_listing() {
    auto start = std::chrono::high_resolution_clock::now();
    while(true) {
        // Poll API every 50μs
        if (new_listing_detected()) {
            execute_market_order();
            break;
        }
        usleep(50);
    }
}
