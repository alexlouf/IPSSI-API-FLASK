import json
import urllib

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def info():
    url ="https://api.nomics.com/v1/volume/history?key=demo-26240835858194712a4f8cc0dc635c7a"
    result = urllib.request.urlopen(url)
    data =json.load(result)
    timestamp = []
    volume = []
    legend = "Volume d'échange quotidien ($)"
    for i in data:
        timestamp.append(i['timestamp'])
        volume.append(i['volume'])
    return render_template("index.html", labels=timestamp, values=volume, legend=legend)

@app.route("/prix")
def prix():
    url = "https://api.nomics.com/v1/exchange-rates/history?key=demo-26240835858194712a4f8cc0dc635c7a&currency=BTC&start=2011-08-18T00%3A00%3A00Z"
    result = urllib.request.urlopen(url)
    data = json.load(result)
    timestamp = []
    price = []
    legend = "BTC Price"
    for i in data:
        timestamp.append(i['timestamp'])
        price.append(i['rate'])
    return render_template("price.html", labels=timestamp, values=price, legend=legend)

@app.route("/market")
def market():
    url = "https://api.nomics.com/v1/market-cap/history?key=demo-26240835858194712a4f8cc0dc635c7a&start=2011-08-18T00%3A00%3A00Z"
    result = urllib.request.urlopen(url)
    data = json.load(result)
    marketcap = []
    timestamp = []
    legend = "Market CAP"
    for i in data:
        marketcap.append(i['market_cap'])
        timestamp.append(i['timestamp'])
    return render_template("market.html" , labels=timestamp, values=marketcap, legend=legend)


if __name__ == "__main__":
    app.run(debug=True)
