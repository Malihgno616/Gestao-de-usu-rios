from flask import Blueprint, render_template, request

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from database.cliente import CLIENTES

cliente_route = Blueprint('clientes', __name__)

@cliente_route.route('/')
def lista_cliente():
    """ listar os clientes """
    return render_template('lista_cliente.html', clientes= CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """  inserir os dados do usuário """
    data = request.json

    novo_usuario ={
        "id": len(CLIENTES) + 1, 
        "nome": data['nome'],
        "email": data['email'],
     }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar os clientes """
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_usuário():
    """formulario para detalhes dos dados do usuário"""
    return render_template('detalhe_usuario.html')

@cliente_route.route('/<int:cliente_id>/edit')
def edit_usuário(cliente_id):
    """formulario para editar os dados do cliente"""

    cliente=None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_usuario():
    """formulario para atualizar os dados do cliente"""
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_usuario(cliente_id):
    """formulario para deletar os dados do cliente"""
    
    global CLIENTES    
    CLIENTES =  [  c for c in CLIENTES if c['id'] != cliente_id ]
    return {"deleted": "ok"}