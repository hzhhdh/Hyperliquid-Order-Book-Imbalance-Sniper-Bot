import axios from 'axios';
import { API_BASE } from '../config';

export async function fetchPortfolioData() {
  const resp = await axios.get(`${API_BASE}/portfolio`);
  return resp.data;
}

export async function getYieldOpportunities() {
  const resp = await axios.get(`${API_BASE}/yield`);
  return resp.data.apys as number[];
}
