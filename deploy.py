pythonCopy codefrom paj33tooor.blockchain.manager import ChaoticBlockchainManager

# Initialize the Blockchain Manager
blockchain = ChaoticBlockchainManager()

# Define contract ABI and Bytecode
abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "getValue",
        "outputs": [{"name": "", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]
bytecode = "0x608060405234801561001057600080fd5b5060405161010038038061010083398101806040528101908080518201929190505050806000819055505060d58061003e6000396000f3fe6080604052600080fdfea165627a7a723058202cfa2cf67d..."

# Deploy the smart contract
contract_address = blockchain.deploy_contract(abi, bytecode)
print(f"Contract deployed at: {contract_address}")
