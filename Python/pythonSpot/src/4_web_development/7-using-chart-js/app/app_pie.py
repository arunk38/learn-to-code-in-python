from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def chart():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    colors = ["#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA", "#ABCDEF", "#DDDDDD", "#ABCABC"]
    return render_template('chart_pie.html', set=zip(values, labels, colors))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)