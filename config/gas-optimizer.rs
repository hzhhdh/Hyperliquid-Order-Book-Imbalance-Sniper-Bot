// Algorithm for predicting the optimal gas
pub async fn calculate_optimal_gas(
    provider: &Provider<Http>,
) -> Result<U256, ProviderError> {
    let block = provider.get_block(BlockNumber::Latest).await?;
    let base_fee = block.base_fee_per_gas.unwrap();
    
    let pending_block = provider.get_block(BlockNumber::Pending).await?;
    let mempool_txs = pending_block.transactions;
    
    let avg_priority: Vec<U256> = mempool_txs
        .iter()
        .map(|tx| tx.gas_price.unwrap_or_default())
        .collect();
    
    let median_gas = median(&avg_priority);
    Ok(base_fee + median_gas)
}

fn median(list: &[U256]) -> U256 {
    let mut sorted = list.to_vec();
    sorted.sort();
    let mid = sorted.len() / 2;
    sorted[mid]
}
