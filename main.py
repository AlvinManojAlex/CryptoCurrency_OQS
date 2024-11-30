"""
    Generating cryptocurrecy keys that are post-quantum resistant using Dilithium, which is a signature scheme provided by the OQS library.
    Dilithium2 is a Lattice-based encryption scheme.
"""


import oqs
import binascii
import hashlib
import base58

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

print("Public key in hex:", public_key_hex)
print("Private key in hex:", private_key_hex)

# Deriving the wallet address by hashing the public key using SHA-256 and then using RIPEMD-160 -> Simulating BitCoin addresses
sha256_hash = hashlib.sha256(public_key).digest()
ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()

# Encoding the result of the hashing using Basse58 like BitCoin
wallet_address = base58.b58encode(ripemd160_hash).decode()

print("Generated Wallet Address:", wallet_address)