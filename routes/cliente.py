from flask import Blueprint, render_template, request

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from database.models.cliente import Cliente


cliente_route = Blueprint('clientes', __name__)

@cliente_route.route('/')
def lista_cliente():
    """ listar os clientes """
    clientes= Cliente.select()
    print('lista_clientes: ', clientes)
    return render_template('lista_cliente.html', clientes= clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """  inserir os dados do usuário """
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar os clientes """
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_usuário(cliente_id):
    """formulario para detalhes dos dados do usuário"""

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_usuario.html', cliente=cliente)

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_usuário(cliente_id):
    """formulario para editar os dados do cliente"""

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_usuario(cliente_id):
    """formulario para atualizar os dados do cliente"""

    data = request.json
    cliente_editado= None
    
    cliente_editado = Cliente.get_by_id
    (cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()
    #editar usuario
    return render_template('item_cliente.html', cliente= cliente_editado)

    #editar usuario
   
   


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_usuario(cliente_id):
    """formulario para deletar os dados do cliente"""
    cliente = Cliente.get_by_id(cliente_id)
    (cliente_id)
    cliente.delete_instance()
    
    return {"deleted": "ok"}