import json, os
from utils import get_cipher

DATA_FILE = "data/vault.enc"

def save_passwords(master_password, passwords):
    cipher = get_cipher(master_password)
    encrypted = cipher.encrypt(json.dumps(passwords).encode())
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

def load_passwords(master_password):
    if not os.path.exists(DATA_FILE):
        return {}
    cipher = get_cipher(master_password)
    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()
    try:
        return json.loads(cipher.decrypt(encrypted).decode())
    except:
        print("❌ マスターパスワードが違います！")
        return None
