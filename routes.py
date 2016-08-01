from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kpi1')
def kpi1():
    return render_template("kpi1.html")

@app.route('/kpi2')
def kpi2():
    return render_template("kpi2.html")

@app.route('/kpi3')
def kpi3():
    return render_template("kpi3.html")


if __name__ == '__main__':
    app.run()
