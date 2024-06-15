from flask import Blueprint, render_template

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
    pass


@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar os clientes """
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_usuário():
    """formulario para detalhes dos dados do usuário"""
    return render_template('detalhe_usuario.html')

@cliente_route.route('/<int:cliente_id>/edit')
def edit_usuário():
    """formulario para editar os dados do cliente"""
    return render_template('form_edit_user.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_usuário():
    """formulario para atualizar os dados do cliente"""
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_usuário():
    """formulario para deletar os dados do cliente"""
    pass