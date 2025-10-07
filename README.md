# MVP Password Manager (SafeInCloud風)

このリポジトリは、Pythonで作った**最小限のSafeInCloud風パスワード管理アプリ（MVP）**です。  
ローカルで暗号化されたパスワードを管理できます。

---

## 🧭 できること（MVP）

1. 🔐 マスターパスワードで全データを暗号化
2. 💾 ローカルに保存 (`data/vault.enc`)
3. 📋 CLIでパスワードを登録・一覧表示
4. 次回起動時に同じマスターパスワードで復号可能

---

## ⚡ 起動方法

1. 仮想環境を作成・有効化

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
