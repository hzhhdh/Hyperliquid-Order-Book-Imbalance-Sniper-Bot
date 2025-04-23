import { configureStore } from '@reduxjs/toolkit';
import portfolioReducer from './portfolioSlice';

export const store = configureStore({
  reducer: { portfolio: portfolioReducer },
});
export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
