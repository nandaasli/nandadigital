from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
model_file = open('model_uas1.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')
@app.route('/')
def index():
return render_template('index backup uas.html', hasil=0, nhasil=0)
@app.route('/predict', methods=['POST'])
def predict():
ntahun = request.form.get('ntahun')
data=('Unnamed','dissimilarity','correlation','homogeneity','contrast','ASM','energy','label','label2')
nstart=len(data)
nseries=int(ntahun)-1
nakhir=nstart+nseries
prediction = model.predict(start=nstart, end=nakhir, dynamic=False)
output = np.round(prediction, 2)
nhasil = len(output)
return render_template('index backup uas.html', hasil=output, ntahun=nakhir, nhasil=nhasil)

if __name__ == '__main__':
app.run(debug=True)