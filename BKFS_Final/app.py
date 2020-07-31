# Import required modules
import flask
import pickle
import nltk
from nltk.stem import PorterStemmer
import pandas as pd
from flask import Flask, request

# Create an instance of Flask and declare variables for our model
app = Flask(__name__)
modelname = 'LRmodel.pkl'


# Homepage, render input prompt HTML
@app.route('/')
def index():
    return flask.render_template('index.html')

# Result page, get prediction result and render
@app.route('/predict', methods=['GET', 'POST'])
# Handle request
def form():
    # Document content was sent with POST request
    if request.method == 'POST':
        # Preparation
        data = request.form['content']
        data=[data]
        #print(data)
        model = pickle.load(open('LRmodel.pkl','rb'))

        #print('loaded')
        # Get result

        result = model.predict(data)
        #print(result)
        confidence=model.predict_proba(data)
        #print(confidence)

        return flask.render_template('result.html', result=result,confidence=confidence)

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

if __name__ == "__main__":
    #app.debug = True
    app.run()
