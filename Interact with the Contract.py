voting = w3.eth.contract(address=voting_address, abi=contract_interface['abi'])

# Vote for a candidate
voting.functions.voteForCandidate(w3.toBytes(text='Alice')).transact({'from': w3.eth.accounts[0]})

# Get votes
votes = voting.functions.totalVotesFor(w3.toBytes(text='Alice')).call()
print(f"Votes for Alice: {votes}")
