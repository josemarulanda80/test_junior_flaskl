
from flask_migrate import Migrate

from flask import Flask,render_template,request, session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# current date and time
curDT = datetime.now()

app = Flask(__name__)

#Cargo todas las configuraciones

app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)







from aplication.database import User


@app.route('/')

def index():

    return render_template('index.html')

@app.route('/registrar',methods=['POST'])
def registrar():
    nombre=request.form['nombre']
    email = request.form['email']
    ciudad=request.form['ciudad']

    user = User(nombre=nombre,email=email,ciudad=ciudad)

    date_time = curDT.strftime("%m/%d/%Y, %H:%M:%S")
    cadena = f"El nombre es {nombre} con correo electronico {email} de la ciudad {ciudad} en la fecha {date_time}"
    f = open('log.txt','a')
    f.write('\n' + cadena)
    f.close()
    f = open ('./aplication/log.txt','r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    db.session.add(user)
    db.session.commit()
    return redirect('/')

@app.route('/all')
def all():
    users=User.query.all()
    print(users)
    return render_template('show.html',users=users)
#Esto siempre va abajo  del todo
db.create_all()