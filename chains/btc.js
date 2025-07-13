const { Client } = require('bitcoin-rpc');
const config = require('../../config/config');

const bitcoinConnection = new Client({
  host: config.networks.bitcoin.rpc.host,
  port: config.networks.bitcoin.rpc.port,
  user: config.networks.bitcoin.rpc.user,
  pass: config.networks.bitcoin.rpc.pass,
  timeout: config.networks.bitcoin.rpc.timeout || 30000,
});

const bitcoinTestnetConnection = config.networks.bitcoin.testnetRpc ? new Client({
  host: config.networks.bitcoin.testnetRpc.host,
  port: config.networks.bitcoin.testnetRpc.port,
  user: config.networks.bitcoin.testnetRpc.user,
  pass: config.networks.bitcoin.testnetRpc.pass,
  timeout: config.networks.bitcoin.testnetRpc.timeout || 30000,
}) : null;

module.exports = { bitcoinConnection, bitcoinTestnetConnection };
