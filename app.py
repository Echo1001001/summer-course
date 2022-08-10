# -*- encoding=utf-8 -*-
'''
Author：钱渝
Time：2022年07月27日
'''

from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))

        model1 = joblib.load("C:\\Users\\有圆圆身体的蓝胖子\\Desktop\\7.27\\regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("C:\\Users\\有圆圆身体的蓝胖子\\Desktop\\7.27\\tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r2))
        # return (render_template("index.html", result1= "ok", result2= "ok"))
    else:
        return(render_template("index.html", result1 = "WAITING", result2 = "WAITING"))

if __name__ == "__main__":
    app.run()

