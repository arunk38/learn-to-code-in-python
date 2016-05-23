import html

from flask import Flask, render_template
import json
import urllib

app = Flask(__name__)


def getExchangeRates():
    rates = []
    response = urllib.request.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data.decode('utf-8'))
    print(rdata)

    rates.append(rdata['rates']['USD'])
    rates.append(rdata['rates']['GBP'])
    rates.append(rdata['rates']['HKD'])
    rates.append(rdata['rates']['AUD'])
    return rates


@app.route("/")
def index():
    rates = getExchangeRates()
    return render_template('test.html', **locals())


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)