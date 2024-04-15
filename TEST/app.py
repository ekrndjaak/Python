from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 가짜 사용자 데이터베이스
users = {
    "john": "password",
    "emma": "flaskrocks"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("index"))
        else:
            return "잘못된 사용자 이름 또는 비밀번호입니다. 다시 시도하세요."
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)