import { request, gql } from 'graphql-request';
import { Logger } from '../utils/logger';

interface PoolData {
    liquidity: string;
    feeGrowthGlobal0X128: string;
}

class UniswapPoolMonitor {
    private graphUrl: string = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3';
    private logger: Logger;

    constructor() {
        this.logger = new Logger('UniswapPoolMonitor');
    }

    async fetchPoolData(poolAddress: string): Promise<PoolData> {
        const query = gql`
            query pool($id: ID!) {
                pools(where: { id: $id }) {
                    liquidity
                    feeGrowthGlobal0X128
                }
            }
        `;
        try {
            const data = await request(this.graphUrl, query, { id: poolAddress });
            return data.pools[0];
        } catch (error) {
            this.logger.error(`Error fetching pool data: ${error}`);
            throw error;
        }
    }

    async monitorPool(poolAddress: string, threshold: number) {
        const data = await this.fetchPoolData(poolAddress);
        if (parseInt(data.liquidity) < threshold) {
            this.logger.warn(`Low liquidity detected for pool ${poolAddress}`);
        }
    }
}

export default UniswapPoolMonitor;
