from __future__ import print_function
import os
import sys
import json
import random
from flask import Flask, render_template, session, redirect, url_for
from flask import jsonify
app = Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
@app.route('/list')
def list():
	if 'my_cards' in session:
		cards = session['my_cards']
	else:	
		print('reading config from disk', file=sys.stderr)
		config_file = 'config.json'
		config = json.loads(open(config_file).read())
		cards = config['Deck']['spades'] + config['Deck']['hearts'] + config['Deck']['diamonds'] + config['Deck']['clubs'] 
		session['my_cards'] =  cards
	
	return "<center><b>This is a Simple Card Game</b></center> <br>" + json.dumps(cards) + "<br> <b><a href = '/deal'>deal</a> <b><a href = '/shuffle'>shuffle</a></b> <b><a href = '/reset'>reset</a>"

@app.route('/shuffle')
def shuffle():
	cards = session['my_cards']
	random.shuffle(cards)
	session.pop('my_cards', None)
	session['my_cards'] =  cards
	return redirect(url_for('list'))

@app.route('/deal')
def deal():
	cards = session['my_cards']
	acard = random.choice(cards)
	i = cards.index(acard)
	newlist = cards[:i] + cards[i+1:]
	session.pop('my_cards', None)
	session['my_cards'] =  newlist
	return "<center><b>This is a Simple Card Game</b></center> <br>" + json.dumps(newlist) + "<br> <b><a href = '/deal'>deal</a></b> <b><a href = '/shuffle'> shuffle</a> <b><a href = '/reset'> reset</a> <br> Your Card " + acard

@app.route('/reset')
def reset():
	session.pop('my_cards', None)
	return redirect(url_for('list'))

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=8000)
