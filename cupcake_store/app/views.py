from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import Cupcake, Pedido, ItemPedido, User
from . import db, login_manager
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def vitrine():
    cupcakes = Cupcake.query.all()
    return render_template('vitrine.html', cupcakes=cupcakes)

@main.route('/add_carrinho/<int:id>')
def add_carrinho(id):
    carrinho = session.get('carrinho', {})
    carrinho[str(id)] = carrinho.get(str(id), 0) + 1
    session['carrinho'] = carrinho
    flash('Cupcake adicionado ao carrinho!')
    return redirect(url_for('main.vitrine'))

@main.route('/carrinho')
def carrinho():
    carrinho = session.get('carrinho', {})
    itens = []
    total = 0
    for id, qtd in carrinho.items():
        cupcake = Cupcake.query.get(int(id))
        subtotal = cupcake.preco * qtd
        itens.append({'cupcake': cupcake, 'quantidade': qtd, 'subtotal': subtotal})
        total += subtotal
    return render_template('carrinho.html', itens=itens, total=total)

@main.route('/remover_carrinho/<int:id>')
def remover_carrinho(id):
    carrinho = session.get('carrinho', {})
    if str(id) in carrinho:
        del carrinho[str(id)]
        session['carrinho'] = carrinho
        flash('Cupcake removido do carrinho!')
    return redirect(url_for('main.carrinho'))

@main.route('/finalizar_pedido', methods=['GET', 'POST'])
@login_required
def finalizar_pedido():
    if request.method == 'POST':
        endereco = request.form['endereco']
        carrinho = session.get('carrinho', {})
        total = 0
        pedido = Pedido(cliente_id=current_user.id, endereco=endereco, status='Pendente', total=0)
        db.session.add(pedido)
        for id, qtd in carrinho.items():
            cupcake = Cupcake.query.get(int(id))
            subtotal = cupcake.preco * qtd
            item = ItemPedido(pedido=pedido, cupcake_id=cupcake.id,
                              quantidade=qtd, preco_unitario=cupcake.preco)
            total += subtotal
            db.session.add(item)
        pedido.total = total
        db.session.commit()
        session['carrinho'] = {}
        flash('Pedido realizado com sucesso!')
        return redirect(url_for('main.pedido', id=pedido.id))
    return render_template('finalizar_pedido.html')

@main.route('/pedido/<int:id>')
@login_required
def pedido(id):
    pedido = Pedido.query.get_or_404(id)
    return render_template('pedido.html', pedido=pedido)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.vitrine'))
        else:
            flash('Usuário ou senha inválidos!')
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.vitrine'))

@main.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Acesso negado!')
        return redirect(url_for('main.vitrine'))
    pedidos = Pedido.query.all()
    return render_template('admin.html', pedidos=pedidos)