export async function connectKeplr(): Promise<string> {
  if (!window.keplr) throw new Error('Keplr not installed');
  try {
    await window.keplr.enable('cosmoshub-4');
    const key = await window.keplr.getKey('cosmoshub-4');
    return key.bech32Address;
  } catch (error) {
    logInfo(`Keplr connection failed: ${error.message}`);
    throw error;
  }
}
