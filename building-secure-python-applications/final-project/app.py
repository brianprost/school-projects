"""
Brian Prost
app.py
lab_6
This exercise generates a simple web site about crypto currencies using
Python Flask and Jinja templates
"""
from datetime import datetime

import requests
from flask import Flask, render_template
from millify import millify

app = Flask(__name__)


@app.route('/')
def welcome_page():
    """this is the main landing page. it displays an introduction to the website
    and links to the three other pages"""
    return render_template('welcome_page.html')


@app.route('/bitcoin')
def bitcoin_page():
    """this function grabs the current time, current price of bitcoin, and then sends
    both and a link to the bitcoin whitepaper to the render_template function to display
    a webpage about bitcoin"""
    date_and_time = datetime.now().strftime("%c")
    bitcoin_price = "$" + millify(get_coin_price('https://api.coincap.io/v2/assets/bitcoin'),
                                  precision=2)
    paper = 'https://www.coinbase.com/bitcoin.pdf'
    return render_template('bitcoin_page.html',
                           date_and_time=date_and_time,
                           price=bitcoin_price,
                           white_paper=paper)


@app.route('/ethereum')
def ethereum_page():
    """this function grabs the current time, current price of an ethereum coin, and then sends
        both and a link to the ethereum whitepaper to the render_template function to display
        a webpage about ethereum"""
    date_and_time = datetime.now().strftime("%c")
    ethereum_price = "$" + millify(get_coin_price('https://api.coincap.io/v2/assets/ethereum'),
                                   precision=2)
    ethereum_paper = 'https://ethereum.org/en/whitepaper/'
    return render_template('ethereum_page.html',
                           date_and_time=date_and_time,
                           price=ethereum_price,
                           white_paper=ethereum_paper)


@app.route('/dogecoin')
def dogecoin_page():
    """this function grabs the current time, current price of dogecoin, and then sends
        both and a link to the dogecoin github (there is no whitepaper) to the
        render_template function to display a webpage about dogecoin"""
    date_and_time = datetime.now().strftime("%c")
    dogecoin_price = "$" + millify(get_coin_price('https://api.coincap.io/v2/assets/dogecoin'),
                                   precision=4)
    dogecoin_paper = 'https://github.com/dogecoin/dogecoin'
    return render_template('dogecoin_page.html',
                           date_and_time=date_and_time,
                           price=dogecoin_price,
                           white_paper=dogecoin_paper)


def get_coin_price(url):
    """this function accepts the url of the coin api and uses the CoinCap api to get
    and return the price of the requested coin"""
    headers, payload = {}, {}
    response = requests.request("GET", url, headers=headers, data=payload)
    coin_info = response.json()
    return coin_info['data']['priceUsd']


if __name__ == '__main__':
    app.run()
