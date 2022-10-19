from aplication import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.Text)
    ciudad=db.Column(db.Text)
    
    def __init__(self,nombre,email,ciudad) -> None:
        self.nombre = nombre
        self.email= email
        self.ciudad=ciudad
    def __repr__(self) -> str:
        return f'User: {self.nombre}'