import base64, hashlib
from cryptography.fernet import Fernet

def derive_key(master_password: str) -> bytes:
    hashed = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def get_cipher(master_password: str) -> Fernet:
    return Fernet(derive_key(master_password))
