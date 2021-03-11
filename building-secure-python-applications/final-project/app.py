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

import logging
import requests
from flask import Flask, render_template, request, session, flash, url_for, redirect
from millify import millify
from passlib.hash import sha256_crypt
from credential_manager import credentials_db, save_credential_db

app = Flask(__name__)
app.secret_key = os.urandom(12)

logging.basicConfig(filename='failed_login_attempts.log', level=logging.INFO,
                    encoding='utf-8', format='%(asctime)s:%(message)s')


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
    if request.method == 'POST':
        try:
            entered_username = request.form["username"]
            entered_password = request.form["password"]
        except KeyError:
            flash("Please enter a valid username and password")
            return render_template('register.html')
        if entered_username in credentials_db:
            flash("You already have an account. Hope you didn't forget your password, "
                  "cause I ain't giving it to you.")
            return render_template('register.html')
        elif not nist_worthy_password(entered_password):
            flash("Your password is not secure enough. Passwords must be original and at least "
                  "12 characters, with 1 uppercase, 1 lowercase, 1 digit, and 1 symbol.")
            return render_template('register.html')
        # save username
        confirmed_credentials = {
            entered_username: {
                "username": entered_username,
                "password": sha256_crypt.hash(entered_password)
            }
        }
        credentials_db.update(confirmed_credentials)
        save_credential_db()
        session['name'] = entered_username
        session['logged_in'] = True
        flash("Registration successful.")
        return redirect(url_for('welcome_page'))
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """displays the login page and handles login"""
    if request.method == 'POST':
        bad_username, bad_password = None, None
        entered_username = request.form["username"]
        entered_password = request.form["password"]
        if entered_username not in credentials_db:
            flash("Username not found")
            bad_username = True
        elif entered_username in credentials_db:
            if sha256_crypt.verify(entered_password,
                                   credentials_db[entered_username]['password']):
                session['logged_in'] = True
                session['name'] = entered_username
                flash("login successful")
                return redirect(url_for('welcome_page'))
            flash("Incorrect password")
            bad_password = True
        if bad_username or bad_password:
            logging.info('Failed login from IP: %s || username: %s || password: %s',
                         request.remote_addr, entered_username, entered_password)
    elif session.get('logged_in'):
        flash("Why you do this? You're already logged in. You disappoint me.")
        return redirect(url_for('welcome_page'))
    return render_template('login.html')


@app.route('/update-password', methods=['GET', 'POST'])
def update_password():
    """changes the password of the current user"""
    if request.method == 'POST':
        entered_current_password = request.form['current_password']
        entered_new_password = request.form['new_password']
        # check if current password is correct
        current_password_correct = sha256_crypt \
            .verify(entered_current_password,
                    credentials_db[str(session['name'])]['password'])
        if not current_password_correct:
            flash("incorrect current password")

        # check if new password meets NIST standards
        new_password_strong = nist_worthy_password(entered_new_password)
        if not new_password_strong:
            flash("Your password is not secure enough. Passwords must be original and at least "
                  "12 characters, with 1 uppercase, 1 lowercase, 1 digit, and 1 symbol.")

        # if both conditions are true, change the password
        if nist_worthy_password(entered_new_password) and current_password_correct:
            credentials_db[str(session['name'])]['password'] = sha256_crypt.hash(
                entered_new_password)
            save_credential_db()
            flash("password changed successfully")
        return render_template("update_password.html")
    if session.get('name') in credentials_db:
        return render_template("update_password.html")
    flash("No user logged in. To change your password, please login first")
    return redirect(url_for('welcome_page'))


@app.route('/logout', )
def logout():
    """logs out the user. there's no button to do this right now,
    but there's also no point to it right now"""
    if session.get('logged_in'):
        session['logged_in'] = False
        session['name'] = None
        flash('Logged out.')
        # this catches the KeyError when there is no session active
    elif not session.get('logged_in'):
        flash("You must be logged in to log OUT, idiot.")
    return redirect(url_for('welcome_page'))


def nist_worthy_password(password):
    """checks that the password is at least 12 characters, has
     at least 1 uppercase, 1 lowercase, 1 number, and 1 special character"""
    #  checks if password meets NIST SP 800-63B criteria
    password_worthy_of_nist = (len(password) > 11
                               and any(c.isupper for c in password)
                               and any(c.islower for c in password)
                               and any(c in string.digits for c in password)
                               and any(c in string.punctuation for c in password))
    # check if password is in bad password file
    with open('bad_passwords.txt', 'r') as file:
        bad_passwords = file.read()
        if password in bad_passwords:
            password_worthy_of_nist = False
    return password_worthy_of_nist


if __name__ == '__main__':
    app.run()
