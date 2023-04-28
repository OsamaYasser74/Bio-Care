import numpy as np
from flask import Flask, request , render_template
import pickle
from flask_mysqldb import MySQL


app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask app'
app.config['MYSQL_DATABASE_HOST'] = 'host'

mysql = MySQL(app)


@app.route('/')
def index():
  return render_template("index.html")



@app.route('/heart', methods = ['GET', 'POST'])
def heart():

  model1 = pickle.load(open('heart_diagnosis_model.sav', 'rb'))

  if request.method == 'POST':
    userdetails = request.form
    Age       = float(userdetails["Age"])
    Sex       = float(userdetails["Sex"])
    Cp        = float(userdetails["Cp"])
    Trestbps  = float(userdetails["Trestbps"])
    Chol      = float(userdetails["Chol"])
    Fbs       = float(userdetails["Fbs"])
    Restecg   = float(userdetails["Restecg"]) 
    Thalach   = float(userdetails["Thalach"])
    Exang     = float(userdetails["Exang"])
    Oldpeak   = float(userdetails["Oldpeak"])
    slope     = float(userdetails["slope"])
    Ca        = float(userdetails["Ca"])
    Thal      = float(userdetails["Thal"])
    features1=[Age,Sex,Cp,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,slope,Ca,Thal]
    final_features = [np.array(features1)]
    prediction = model1.predict(final_features)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO heart (Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, slope, Ca, Thal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, slope, Ca, Thal))
    mysql.connection.commit()
    cur.close()
    return render_template('result1.html', my_prediction = prediction)
  elif request.method == 'GET':
    return render_template("heart.html")



@app.route('/hepatitisC', methods=['GET', 'POST'])
def hepatitisC():

  model2 = pickle.load(open('HepatitisC_disease_model.sav','rb'))

  if request.method == 'POST':
    userdetails = request.form
    Age                 = float(userdetails["Age"])
    Sex                 = float(userdetails["Sex"])
    Alb                 = float(userdetails["Alb"])
    Alp                 = float(userdetails["Alp"])
    Alt                 = float(userdetails["Alt"])
    Ast                 = float(userdetails["Ast"])
    Bil                 = float(userdetails["Bil"])
    Che                 = float(userdetails["Che"])
    Chol                = float(userdetails["Chol"])
    Crea                = float(userdetails["Crea"])
    Ggt                 = float(userdetails["Ggt"])
    Prot                = float(userdetails["Prot"])
    features2 = [Age, Sex, Alb, Alp, Alt, Ast, Bil, Che, Chol, Crea, Ggt, Prot]
    final_features2 = [np.array(features2)]
    prediction = model2.predict(final_features2)
    # cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO hepatitis (Age, Sex, Alb, Alp, Alt, Ast, Bil, Che, Chol, Crea, Ggt, Prot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(Age, Sex, Alb, Alp, Alt, Ast, Bil, Che, Chol, Crea, Ggt, Prot))
    # mysql.connection.commit()
    # cur.close()
    return render_template('result2.html', my_prediction=prediction)
  elif request.method == 'GET':
    return render_template("hepatitis.html")



@app.route('/diabetes', methods = ['GET', 'POST'])
def diabetes():

  model3 = pickle.load(open('model7744.pkl', 'rb'))

  if request.method == 'POST':
    userdetails = request.form
    Gender    = float(userdetails["Gender"])
    Age       = float(userdetails["Age"])
    Urea      = float(userdetails["Urea"])
    Cr        = float(userdetails["Cr"])
    HbA1c     = float(userdetails["HbA1c"])
    Chol      = float(userdetails["Chol"])
    Tg        = float(userdetails["Tg"]) 
    Hdl       = float(userdetails["Hdl"])
    Ldl       = float(userdetails["Ldl"])
    Vldl      = float(userdetails["Vldl"])
    Bmi       = float(userdetails["Bmi"])
    features3 = [Gender, Age, Urea, Cr, HbA1c, Chol, Tg, Hdl, Ldl, Vldl, Bmi]
    final_features = [np.array(features3)]
    prediction = model3.predict(final_features)
    print(prediction)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO diabetes(Gender, Age, Urea, Cr, HbA1c, Chol, Tg, Hdl, Ldl, Vldl, Bmi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(Gender, Age, Urea, Cr, HbA1c, Chol, Tg, Hdl, Ldl, Vldl, Bmi))
    mysql.connection.commit()
    cur.close()
    return render_template('result3.html', my_prediction = prediction )
  elif request.method == 'GET':
    return render_template("diabetes.html")
  


if __name__ == '__main__':
  app.run(debug=True , host="0.0.0.0" , port=5000)



