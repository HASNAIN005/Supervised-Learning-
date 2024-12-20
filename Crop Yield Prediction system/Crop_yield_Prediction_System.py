from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle


dtr=pickle.load(open('DTR.pkl','rb'))
preprocessor=pickle.load(open('preprocessor.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Predict',methods=['POST','GET'])
def prediction():
    if request.method == 'POST':
        Area = request.form['Area']
        Year = request.form['Year']
        Item = request.form['Item']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']

        user_input = np.array([[Area, Year, Item, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp]])
        user_input = preprocessor.transform(user_input)
        result = dtr.predict(user_input).reshape(1, -1)
        result_value = result[0, 0]
        return render_template('index.html', result=result_value)















if __name__=='__main__':
    app.run(debug=True)