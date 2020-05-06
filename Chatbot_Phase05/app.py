import sqlite3
import time
import datetime
import re
import random
from flask import Flask, request, url_for, redirect, render_template
from chatbot_v3 import chatty

conn = sqlite3.connect('tablessss.db', check_same_thread=False)
c = conn.cursor()

email =''

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/')
def form():
	return render_template("form.html")

@app.route('/response', methods=['POST'])
def response():
    global email 
    email = request.form.get("email")
    return render_template("home.html")
    

@app.route('/feedback' , methods=['POST'])
def feedback():
    time1 = time.time()
    date1 = str(datetime.datetime.fromtimestamp(time1).strftime('%Y-%m-%d %H:%M:%S'))
    rating = request.form['meter']
    print(rating)
    c.execute("INSERT INTO happymeter( hs_studentID,hm_rating,hm_datestamp) VALUES(?, ?,?)",(email, rating,date1))
    conn.commit()
    return render_template("form.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    get_output=chatty(userText, email)
    return (get_output)


if __name__ == "__main__":
    #app.debug = True
    app.run()
