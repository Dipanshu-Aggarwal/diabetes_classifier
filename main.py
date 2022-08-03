# install flask -> pip install flask in command prompyt

from flask import Flask, render_template, request
import joblib

#load the model
model = joblib.load('predict_79.pkl')

# initialise the app
app = Flask(__name__)
# we are telling Flask that the whole file main.py is an instance of app
# we are not hardcoding it like app = Flask(main.py)

# http://127.0.0.1:5000

# http - hypertext transfer protocol
# 127.0.0.1 - local ip address
# 5000 - port
# / - route

#  if we do not define the route, the page will show that page not found. 

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/predict', methods = ['post'])
def predict():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    
    data = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if data[0] == 0:
        resp = 'not diabetic'
    else:
        resp = 'diabetic'

    return render_template('forms.html', data = resp)
    # Showing the response on the forms page itself.
# running the app - it must always be the last command. 
app.run(debug = 'True')
# the debug = True attribute makes sure that we do not have to execute 
# the file again and again to save changes to the server. 