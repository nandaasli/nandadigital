from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
model_file = open('model_uas1.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')
@app.route('/')



if __name__ == '__main__':
app.run(debug=True)
