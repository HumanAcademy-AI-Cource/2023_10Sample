#!/usr/bin/env python3

# 必要なライブラリをインポート
from flask import Flask, render_template, send_from_directory

# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/images/banana.png")
def datas():
    """images/banana.pngで画像を取得するための関数"""
    return send_from_directory("./images", "banana.png")


@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
