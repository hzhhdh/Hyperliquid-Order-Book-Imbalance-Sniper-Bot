export async function retryOperation<T>(operation: () => Promise<T>, maxAttempts: number = 3): Promise<T> {
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === maxAttempts) throw new Error(`Operation failed after ${maxAttempts} attempts: ${error.message}`);
      await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
    }
  }
  throw new Error('Retry operation failed');
}
