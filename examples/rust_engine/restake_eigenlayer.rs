use eigenlayer::*;
fn main() {
    if get_current_apr() > config.min_apr {
        restake(&wallet, config.pool).await.unwrap();
    }
}
