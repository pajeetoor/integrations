# Log a task result on-chain
transaction_hash = blockchain.log_task(
    sender_keypair="path/to/solana_keypair.json",
    task_description="Attempted to analyze energy consumption data",
    task_result="Results inconclusive, but effort was made"
)
print(f"Task logged on blockchain with transaction hash: {transaction_hash}")
