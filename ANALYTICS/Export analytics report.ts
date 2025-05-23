export function exportAnalyticsReport(data: any): string {
  return JSON.stringify(data, null, 2);
}
