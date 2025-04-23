import { useEffect } from 'react';
import { useAppDispatch } from '../store';
import { fetchPortfolio } from '../store/portfolioSlice';

export function usePortfolio() {
  const dispatch = useAppDispatch();
  useEffect(() => { dispatch(fetchPortfolio()); }, [dispatch]);
}
