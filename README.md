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

⚙️ GitHubに上げる手順
```python
# 1. .gitignore を作成
# 内容:
venv/
__pycache__/
*.pyc
data/vault.enc

# 2. Git初期化＆コミット
git init
git add .
git commit -m "Initial commit - MVP password manager"

# 3. GitHubリポジトリを作成
# GitHubで新しいリポジトリ作成後、URLをコピー

# 4. リモートを追加＆プッシュ
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main

# 5. クローンして利用する場合
git clone <your-repo-url>
cd password_manager
python -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
python main.py
```


1. 仮想環境を作成・有効化

```zsh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
# 依存ライブラリをインストール
```zsh
pip install -r requirements.txt
```
# アプリを起動
```zsh
python main.py
```

    初回起動時に data/vault.enc が自動生成されます

    マスターパスワードでデータを暗号化・復号します
