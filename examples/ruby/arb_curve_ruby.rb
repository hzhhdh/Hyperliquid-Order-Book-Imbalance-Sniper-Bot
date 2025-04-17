require 'ethereum.rb'
client = Ethereum::HttpClient.new('http://localhost:8545')
contract = Ethereum::Contract.create(client: client, name: 'Curve', address: addr, abi: abi)
if contract.call.get_dy(0,1,1e18)/1e18 - 1 > 0.005 then puts "Arb!" end
