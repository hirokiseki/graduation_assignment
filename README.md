# graduation_assignment

# pythonのインストール
公式サイトからダウンロード

# Djangoのインストール
pip install django

# 新規プロジェクト作成
python -m django startproject test_app

# ブラウザで動作確認　（http://127.0.0.1:8000/hello/）
python manage.py runserver

# DBの管理ページ　(http://127.0.0.1:8000/hello/admin)
python manage.py ceatesuperuser でuserを追加して色々出来る
user名　admin
password admin

# DMのマイグレーション
python manage.py makemigrations hello(アプリの名前)
python manage.py migrate