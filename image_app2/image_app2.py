#!/usr/bin/env python3

# 必要なライブラリをインポート
from flask import Flask, render_template, send_from_directory


# Flaskを使用する準備
app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/get_image", methods=["GET"])
def get_image_function():
    """画像を返す関数"""
    image_path = "images/banana.png"
    print("image_path={}".format(image_path))
    return image_path


@app.route("/images/<path:name>")
def datas(name):
    """images/ファイル名という形式のURLでファイルをダウンロードできるようにする設定"""
    return send_from_directory("./images", name)

@app.route("/")
def main():
    """トップページにアクセスしたときに実行される関数"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
