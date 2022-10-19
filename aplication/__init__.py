from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#Cargo todas las configuraciones

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)




db.create_all()

@app.route('/')
def index():
    return render_template('index.html')