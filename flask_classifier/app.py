from flask import Flask, request,redirect, render_template
import pandas as pd
import joblib

#tutorial from https://towardsdatascience.com/building-a-machine-learning-web-application-using-flask-29fa9ea11dac



app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def main():
    if request.method=='POST':
        #Unpickle the msaved model
        clf_model=joblib.load('clf.pkl')

        #get the values that the user has entered in the weight and height input bars
        weight=request.form.get('weight')
        height=request.form.get('height')

        #put these in a data frame
        X=pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])

        #GET PREDICTION
        prediction=clf_model.predict(X)[0]
    else:
        prediction=""


    return render_template('website.html',output=prediction)







if __name__=='__main__':
    app.run(debug=True)