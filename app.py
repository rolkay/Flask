import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/stock', methods=['GET'])
def track_stock():
    symbol = request.args.get('symbol')
    if symbol:
        api_key = '8ETX4ZO6F2765ELH'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        stock_data = data['Global Quote']
        return render_template('index.html', stock_data=stock_data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
