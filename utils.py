import os, json, base64, hashlib, shutil, datetime
from cryptography.fernet import Fernet
import pyperclip

# --- 暗号鍵生成 ---
def derive_key(master_password: str) -> bytes:
    hashed = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def get_cipher(master_password: str) -> Fernet:
    return Fernet(derive_key(master_password))

# --- 暗号化／復号 ---
def encrypt(data: str, key: str) -> str:
    return get_cipher(key).encrypt(data.encode()).decode()

def decrypt(token: str, key: str) -> str:
    return get_cipher(key).decrypt(token.encode()).decode()

# --- データ入出力 ---
def load_data(file_path: str, key: str) -> dict:
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r") as f:
        encrypted = f.read()
        if not encrypted.strip():
            return {}
    try:
        return json.loads(decrypt(encrypted, key))
    except Exception:
        print("⚠️ 復号に失敗しました。キーが違う可能性があります。")
        return {}

def save_data(file_path: str, data: dict, key: str):
    encrypted = encrypt(json.dumps(data), key)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(encrypted)

# --- バックアップ ---
def backup_file(file_path: str):
    if not os.path.exists(file_path):
        return
    backup_dir = "data/backup"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{timestamp}_{os.path.basename(file_path)}")
    shutil.copy2(file_path, backup_path)
    print(f"🗂 バックアップ作成: {backup_path}")

# --- クリップボード ---
def copy_to_clipboard(text: str):
    try:
        pyperclip.copy(text)
        print("📋 パスワードをクリップボードにコピーしました。")
    except pyperclip.PyperclipException:
        print("⚠️ クリップボードにアクセスできません。")

