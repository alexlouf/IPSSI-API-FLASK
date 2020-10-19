import json
import urllib

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.nomics.com/v1/exchange-rates/history?key=demo-26240835858194712a4f8cc0dc635c7a&currency=BTC&start=2018-04-14T00%3A00%3A00Z&end=2020-04-16T00%3A00%3A00Z"
    result = urllib.request.urlopen(url)
    data = json.load(result)
    print(data)
    timestamp = []
    price = []
    legend = "BTC Price"
    for i in data:
        timestamp.append(i['timestamp'])
        price.append(i['rate'])
    return render_template("chart.html", labels=timestamp, values=price, legend=legend)



if __name__ == "__main__":
    app.run(debug=True)
