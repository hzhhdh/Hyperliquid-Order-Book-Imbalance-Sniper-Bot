impl FarmingBot {
    pub fn enter_pool(&self, pool: Pool) -> Result<Transaction, PoolError> {
        if pool.apr < self.min_apr || pool.tvl < self.min_tvl {
            return Err(PoolError::NotProfitable);
        }
        self.submit_tx(pool.entry_function())
    }
}
