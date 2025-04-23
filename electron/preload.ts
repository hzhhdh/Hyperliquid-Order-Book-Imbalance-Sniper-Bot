import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electronAPI', {
  sendTrade: (order: any) => ipcRenderer.send('execute-trade', order),
  onPriceUpdate: (cb: Function) => ipcRenderer.on('price-update', (_, data) => cb(data)),
});
