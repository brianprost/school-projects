"""
Brian Prost
app.py
final_project
This exercise generates a simple web site about crypto currencies using
Python Flask and Jinja templates and adds a login and registration form
"""
import os
import string
from datetime import datetime

import requests
from flask import Flask, render_template, request, session, url_for, flash
from millify import millify
from passlib.hash import sha256_crypt
from credential_manager import credentials_db, save_credential_db

app = Flask(__name__)
app.secret_key = os.urandom(12)


@app.route('/', methods=['GET', 'POST'])
def welcome_page():
    """this is the main landing page. it displays an introduction to the website
    and links to the three other pages"""
    bitcoin_info = get_coin_info('bitcoin')
    ether_info = get_coin_info('ethereum')
    dogecoin_info = get_coin_info('dogecoin')
    return render_template('welcome_page.html',
                           bitcoin_price=millify(
                               bitcoin_info['data']['priceUsd'], precision=2),
                           ether_price=millify(
                               ether_info['data']['priceUsd'], precision=2),
                           dogecoin_price=millify(
                               dogecoin_info['data']['priceUsd'], precision=4),
                           bitcoin_market_cap=millify(
                               bitcoin_info['data']['marketCapUsd'], precision=2),
                           ether_market_cap=millify(
                               ether_info['data']['marketCapUsd'], precision=2),
                           dogecoin_market_cap=millify(
                               dogecoin_info['data']['marketCapUsd'], precision=4)
                           )


@app.route('/bitcoin')
def bitcoin_page():
    """this function grabs the current time, current price of bitcoin, and then sends
    both and a link to the bitcoin whitepaper to the render_template function to display
    a webpage about bitcoin"""
    date_and_time = datetime.now().strftime("%c")
    bitcoin_price = get_coin_info('bitcoin')
    paper = 'https://www.coinbase.com/bitcoin.pdf'
    return render_template('bitcoin_page.html',
                           date_and_time=date_and_time,
                           price='$' +
                           millify(bitcoin_price['data']
                                   ['priceUsd'], precision=2),
                           white_paper=paper)


@app.route('/ethereum')
def ethereum_page():
    """this function grabs the current time, current price of an ethereum coin, and then sends
        both and a link to the ethereum whitepaper to the render_template function to display
        a webpage about ethereum"""
    date_and_time = datetime.now().strftime("%c")
    ether_price = get_coin_info('ethereum')
    ethereum_paper = 'https://ethereum.org/en/whitepaper/'
    return render_template('ethereum_page.html',
                           date_and_time=date_and_time,
                           price='$' +
                           millify(ether_price['data']
                                   ['priceUsd'], precision=2),
                           white_paper=ethereum_paper)


@app.route('/dogecoin')
def dogecoin_page():
    """this function grabs the current time, current price of dogecoin, and then sends
        both and a link to the dogecoin github (there is no whitepaper) to the
        render_template function to display a webpage about dogecoin"""
    date_and_time = datetime.now().strftime("%c")
    dogecoin_price = get_coin_info('dogecoin')
    dogecoin_paper = 'https://github.com/dogecoin/dogecoin'
    return render_template('dogecoin_page.html',
                           date_and_time=date_and_time,
                           price='$' +
                           millify(dogecoin_price['data']
                                   ['priceUsd'], precision=4),
                           white_paper=dogecoin_paper)


def get_coin_info(coin):
    """uses the CoinCap API to lookup info on any given coin passed as an argument
    returns a dictionary of info about the coin"""
    url = "https://api.coincap.io/v2/assets/" + str(coin)
    headers, payload = {}, {}
    response = requests.request("GET", url, headers=headers, data=payload)
    coin_info = response.json()
    return coin_info


@app.route('/register', methods=['GET', 'POST'])
def register():
    """renders a register page and handles registration"""
    error_msg = ""
    if request.method == 'POST':
        entered_username = request.form["username"]
        entered_password = request.form["password"]
        if len(entered_username) < 1:
            error_msg = "Please enter a username"
        elif len(entered_password) < 1:
            error_msg = "Please enter a password"
        elif not password_complexity_check(entered_password):
            error_msg = "Your password is not secure enough. Passwords must be at least " \
                        "12 characters, with 1 uppercase, 1 lowercase, 1 digit, and 1 symbol."
        elif not user_is_new(entered_username):
            error_msg = "You already have an account. Hope you didn't forget your password, " \
                        "cause I ain't giving it to you."
        if len(error_msg) > 0:
            flash(error_msg)
            return render_template('register.html')
        else:
            # save username
            confirmed_credentials = {
                "username": entered_username,
                "password": sha256_crypt.hash(entered_password)
            }
            credentials_db.append(confirmed_credentials)
            save_credential_db()
            session['logged_in'] = True
            flash("Registration successful.")
            return welcome_page()
    else:
        flash(error_msg)
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """displays the login page and handles login"""
    error_log = []
    if request.method == 'POST':
        entered_username = request.form["username"]
        entered_password = request.form["password"]
        if user_is_new(entered_username):
            error_log.append("Invalid username")
        elif not user_is_new(entered_username):
            if password_is_correct(entered_username, entered_password):
                session['logged_in'] = True
                flash("login successful")
                return welcome_page()
            error_log.append("Incorrect password")
        flash(error_log)
        return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """logs out the user. there's no button to do this right now,
    but there's also no point to it right now"""
    session['logged_in'] = False
    return welcome_page()


def user_is_new(entered_username):
    """checks if user already is in the database"""
    for username in credentials_db:
        if username["username"] == entered_username:
            return False
    return True


def password_is_correct(entered_username, entered_password):
    """returns true or false if the password is correct"""
    for username in credentials_db:
        if username["username"] == entered_username:
            index_of_username = credentials_db.index(username)
    return sha256_crypt.verify(entered_password, credentials_db[index_of_username]['password'])


def password_complexity_check(password):
    """checks that the password is at least 12 characters, has
     at least 1 uppercase, 1 lowercase, 1 number, and 1 special character"""
    return (len(password) > 11
            and any(c.isupper for c in password)
            and any(c.islower for c in password)
            and any(c in string.digits for c in password)
            and any(c in string.punctuation for c in password))


if __name__ == '__main__':
    app.run()
