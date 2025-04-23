import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { fetchPortfolioData } from '../services/api';

export const fetchPortfolio = createAsyncThunk('portfolio/fetch', async () => {
  return await fetchPortfolioData();
});

const portfolioSlice = createSlice({
  name: 'portfolio',
  initialState: { history: [] as {value:number;time:string}[] },
  extraReducers: builder => {
    builder.addCase(fetchPortfolio.fulfilled, (state, action) => {
      state.history = action.payload.history;
    });
  },
});

export default portfolioSlice.reducer;
