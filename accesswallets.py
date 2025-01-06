pythonCopy codeimport os

# Load Solana wallet path
solana_wallet_path = os.getenv("SOLANA_WALLET_PATH")
print(f"Solana Wallet Path: {solana_wallet_path}")

# Load Ethereum private key
ethereum_private_key = os.getenv("ETHEREUM_WALLET_PRIVATE_KEY")
print("Ethereum Private Key successfully loaded.")
