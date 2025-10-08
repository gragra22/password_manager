import json
import os
import base64
import pyperclip
from cryptography.fernet import Fernet

DATA_FILE = "passwords.json"
KEY_FILE = "key.key"


def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)


def load_key():
    with open(KEY_FILE, "rb") as f:
        return f.read()


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def encrypt(fernet, text):
    return fernet.encrypt(text.encode()).decode()


def decrypt(fernet, text):
    return fernet.decrypt(text.encode()).decode()


def add_password(fernet, data):
    service = input("サービス名: ")
    username = input("ユーザー名: ")
    password = input("パスワード: ")
    data[service] = {
        "username": encrypt(fernet, username),
        "password": encrypt(fernet, password),
    }
    save_data(data)
    print(f"[+] {service} を登録しました。")


def view_passwords(fernet, data):
    if not data:
        print("登録されているサービスはありません。")
        return
    for service, info in data.items():
        username = decrypt(fernet, info["username"])
        print(f"- {service}: {username}")


def search_password(fernet, data):
    keyword = input("検索キーワード: ").lower()
    results = [s for s in data if keyword in s.lower()]
    if not results:
        print("該当するサービスがありません。")
        return
    for service in results:
        info = data[service]
        username = decrypt(fernet, info["username"])
        print(f"{service}: {username}")
    choice = input("表示またはコピーしたいサービス名を入力（Enterでスキップ）: ")
    if choice in data:
        pw = decrypt(fernet, data[choice]["password"])
        pyperclip.copy(pw)
        print(f"✅ パスワードをクリップボードにコピーしました。")


def edit_password(fernet, data):
    service = input("編集するサービス名: ")
    if service not in data:
        print("サービスが見つかりません。")
        return
    username = input("新しいユーザー名（空欄で変更なし）: ")
    password = input("新しいパスワード（空欄で変更なし）: ")
    if username:
        data[service]["username"] = encrypt(fernet, username)
    if password:
        data[service]["password"] = encrypt(fernet, password)
    save_data(data)
    print(f"[✓] {service} を更新しました。")


def delete_password(data):
    service = input("削除するサービス名: ")
    if service in data:
        del data[service]
        save_data(data)
        print(f"[✗] {service} を削除しました。")
    else:
        print("サービスが見つかりません。")


def main():
    generate_key()
    fernet = Fernet(load_key())
    data = load_data()

    while True:
        print("\n=== パスワードマネージャー ===")
        print("1. 登録")
        print("2. 一覧表示")
        print("3. 検索")
        print("4. 編集")
        print("5. 削除")
        print("6. 終了")

        choice = input("選択: ")

        if choice == "1":
            add_password(fernet, data)
        elif choice == "2":
            view_passwords(fernet, data)
        elif choice == "3":
            search_password(fernet, data)
        elif choice == "4":
            edit_password(fernet, data)
        elif choice == "5":
            delete_password(data)
        elif choice == "6":
            break
        else:
            print("無効な入力です。")


if __name__ == "__main__":
    main()
