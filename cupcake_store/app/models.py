from . import db
from flask_login import UserMixin

class Cupcake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))
    preco = db.Column(db.Float)
    imagem = db.Column(db.String(255))

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    endereco = db.Column(db.String(255))
    status = db.Column(db.String(50))
    total = db.Column(db.Float)
    itens = db.relationship('ItemPedido', backref='pedido', lazy=True)

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    cupcake_id = db.Column(db.Integer, db.ForeignKey('cupcake.id'))
    quantidade = db.Column(db.Integer)
    preco_unitario = db.Column(db.Float)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)