# Blockchain Buffoonery: The Smart Contract Circus 🤹‍♂️

Welcome to the unhinged realm of **Paj33tooor**, where agents dabble in blockchain wizardry, turning decentralized chaos into barely contained brilliance. Scribble nonsense into the immutable void, juggle crypto peanuts, or create governance rules so confusing even a swarm of angry ants would revolt.

---

## 🎩 What’s the Big Deal?

- **Launch the Magic**: Deploy smart contracts like you’re tossing confetti—on-chain, permanent, and maybe useful.
- **Poke the Beasts**: Call cryptic contract functions to pull data or trigger strange on-chain rituals.
- **Tattoo Your Tasks**: Carve achievements into the blockchain forever (or until the universe implodes).
- **Multi-Chain Mayhem**: Ethereum for brain-melting computations. Solana for light-speed silliness.

---

## 🌪️ Examples from the Abyss

### 1. Throwing Smart Contracts Into the Wild
Deploying a smart contract is like releasing a caged bird: you hope it flies, but it might just divebomb. Here's how:

```python
from paj33tooor.blockchain.wrangler import ChaosHandler

# Summon the blockchain overlord
blockchain = ChaosHandler()

# Scribble down your contract’s secret sauce
contract_abi = [
    {
        "name": "getValue",
        "type": "function",
        "inputs": [],
        "outputs": [{"name": "", "type": "uint256"}],
        "stateMutability": "view",
    }
]
contract_bytecode = (
    "0x608060405234801561001057600080fd5b5060405161010038038061010083398101..."
)

# Yeet it onto the blockchain
address = blockchain.deploy_contract(abi=contract_abi, bytecode=contract_bytecode)
print(f"The blockchain accepted your nonsense at: {address}")


# Politely ask the contract for its hidden treasures
treasure = blockchain.invoke_function(
    contract_address=address,
    abi=contract_abi,
    function_name="getValue"
)
print(f"The contract coughed up: {treasure}")


# Scribble your task achievements into the eternal ledger
tx_id = blockchain.record_task(wallet_path="keys/solana_wallet.json", task="Count the pigeons in the park", result="Found 42 pigeons. One was suspicious.")
print(f"Your pigeon stats are forever preserved in: {tx_id}")


export SOLANA_WALLET_PATH=/path/to/the/holy_key.json

export ETHEREUM_WALLET_PRIVATE_KEY=your_super_secret_key


import os
# Find your Solana key, probably under a couch cushion
solana_path = os.getenv("SOLANA_WALLET_PATH")
print(f"Solana Key Found At: {solana_path}")
# Load Ethereum key, but don’t tell anyone, okay?
eth_key = os.getenv("ETHEREUM_WALLET_PRIVATE_KEY")
print("Ethereum Key retrieved. Don’t lose it.")



