import os
from utils import load_data, save_data, copy_to_clipboard, backup_file

DATA_FILE = "data/passwords.json"

def main():
    os.makedirs("data", exist_ok=True)
    master_pw = input("マスターパスワードを入力してください: ")
    key = master_pw
    data = load_data(DATA_FILE, key)

    while True:
        print("\n=== SafeInCloud風 CLI ===")
        print("1. 登録")
        print("2. 一覧表示")
        print("3. 検索")
        print("4. 編集")
        print("5. 削除")
        print("6. パスワードコピー")
        print("7. 終了")
        choice = input("番号を選んでください: ")

        if choice == "1":
            service = input("サービス名: ")
            username = input("ユーザー名: ")
            password = input("パスワード: ")
            data[service] = {"username": username, "password": password}
            save_data(DATA_FILE, data, key)
            backup_file(DATA_FILE)
            print("✅ 登録しました。")

        elif choice == "2":
            if not data:
                print("⚠️ 登録はまだありません。")
                continue
            for i, (s, info) in enumerate(data.items(), 1):
                print(f"{i}. {s} | {info['username']} | {'●'*len(info['password'])}")

        elif choice == "3":
            keyword = input("検索キーワード: ")
            results = {s: info for s, info in data.items() if keyword.lower() in s.lower()}
            if not results:
                print("❌ 該当データなし。")
                continue
            for i, (s, info) in enumerate(results.items(), 1):
                print(f"{i}. {s} | {info['username']} | {'●'*len(info['password'])}")

        elif choice == "4":
            service = input("編集するサービス名: ")
            if service not in data:
                print("❌ 該当サービスなし")
                continue
            username = input("新しいユーザー名（空欄で変更なし）: ")
            password = input("新しいパスワード（空欄で変更なし）: ")
            if username:
                data[service]["username"] = username
            if password:
                data[service]["password"] = password
            save_data(DATA_FILE, data, key)
            backup_file(DATA_FILE)
            print("📝 更新しました。")

        elif choice == "5":
            service = input("削除するサービス名: ")
            if service in data:
                del data[service]
                save_data(DATA_FILE, data, key)
                backup_file(DATA_FILE)
                print("🗑 削除しました。")
            else:
                print("❌ 該当サービスなし")

        elif choice == "6":
            service = input("コピーするサービス名: ")
            if service in data:
                copy_to_clipboard(data[service]["password"])
            else:
                print("❌ 該当サービスなし")

        elif choice == "7":
            save_data(DATA_FILE, data, key)
            print("💾 保存して終了します。")
            break

        else:
            print("⚠️ 無効な入力です。")

if __name__ == "__main__":
    main()
