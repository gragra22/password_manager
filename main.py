from vault import save_passwords, load_passwords

def main():
    master = input("マスターパスワードを入力: ")

    passwords = load_passwords(master)
    if passwords is None:
        return

    while True:
        print("\n1. 登録  2. 一覧  3. 終了")
        choice = input("> ")

        if choice == "1":
            service = input("サービス名: ")
            user = input("ユーザー名: ")
            pw = input("パスワード: ")
            passwords[service] = {"user": user, "pw": pw}
            save_passwords(master, passwords)
            print("✅ 登録しました。")

        elif choice == "2":
            for s, info in passwords.items():
                print(f"{s}: {info['user']} / {info['pw']}")

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
