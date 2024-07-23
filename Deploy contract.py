from web3 import Web3
import json

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Compile the contract
with open('Voting.sol') as file:
    voting_contract_source = file.read()

compiled_sol = compile_source(voting_contract_source)
contract_interface = compiled_sol['<stdin>:Voting']

# Deploy the contract
Voting = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = Voting.constructor(['Alice', 'Bob', 'Charlie']).transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

voting_address = tx_receipt.contractAddress
