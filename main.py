"""
    Generating cryptocurrecy keys that are post-quantum resistant using Dilithium, which is a signature scheme provided by the OQS library.
    Dilithium2 is a Lattice-based encryption scheme.
"""

import oqs
import binascii
import hashlib
import base58
import time
import json
import oqs.rand as oqsrand

# The signature algorithm
sigalg = 'Dilithium2'

# Generating the key pair (private and public key)
with oqs.Signature(sigalg) as signer:

    # Generating public/private key pair
    public_key = signer.generate_keypair()
    private_key = signer.export_secret_key()

    # Converting the public and private keys into hex format
    public_key_hex = binascii.hexlify(public_key).decode()
    private_key_hex = binascii.hexlify(private_key).decode()

print("\nPublic key in hex:", public_key_hex)
print("\nPrivate key in hex:", private_key_hex)

# Deriving the wallet address by hashing the public key using SHA-256 and then using RIPEMD-160 -> Simulating BitCoin addresses
sha256_hash = hashlib.sha256(public_key).digest()
ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

# Encoding the result of the hashing using Basse58 like BitCoin
wallet_address = base58.b58encode(ripemd160_hash).decode()

print("\nGenerated Wallet Address:", wallet_address)

# Generating a nonce value that is randomly generated using OQS random bytes
nonce = oqsrand.randombytes(8)
nonce_hex = binascii.hexlify(nonce).decode()
print("\nRandomly generated nonce value:", nonce_hex)

# Consider a sample BitCoin transaction
transaction = {
    'nonce': nonce_hex,
    'sender': wallet_address,
    'recipient': '3AgbInc1sL9hnHavv5IOcjuRFQEU', # Dummy recipient's public address
    'amount': 2,
    'transaction_id': 'aaa_001',
    'timestamp': int(time.time())
}

transaction_message = json.dumps(transaction, separators=(',', ':')).encode()

# Hashing the transaction message
transaction_message_hash = hashlib.sha256(transaction_message).digest()

# Signing the transaction with the private key
with oqs.Signature(sigalg, private_key) as signer:
    signature = signer.sign(transaction_message_hash)

print("\nSignature in hex:", signature.hex())

# Verifying the signature using the public key
with oqs.Signature(sigalg) as verifier:
    is_verified = verifier.verify(transaction_message_hash, signature, public_key)

if is_verified:
    print("\nTransaction valid since the signature is valid")
else:
    print("\nTransaction invalid")