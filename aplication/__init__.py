from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#Cargo todas las configuraciones

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)




db.create_all()

@app.route('/',methods=['POST'])
def index():
    nombre=request.form['nombre']
    email = request.form['email']
    ciudad=request.form['ciudad']
    print(nombre)
    print(email)
    print(ciudad)

    return render_template('index.html')