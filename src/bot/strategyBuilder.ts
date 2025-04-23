export interface Strategy {
  name: string;
  config: Record<string, any>;
}
export function buildStrategy(name: string, config: any): Strategy {
  return { name, config };
}
