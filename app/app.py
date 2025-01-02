from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

# Generate a new private key
private_key = Ed25519PrivateKey.generate()

# Serialize the private key to PEM format
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Derive the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to PEM format
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Print the keys
print("Private Key:")
print(pem_private_key.decode())

print("\nPublic Key:")
print(pem_public_key.decode())

    
       
        
    
