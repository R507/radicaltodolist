from flask import Blueprint, request, g, redirect, url_for, abort, \
     render_template, flash, current_app  #,session
from app.back.models import TodoList
from app.back.db import session_scope


bp = Blueprint(
    'back',
    __name__,
    url_prefix='/backend',)


@bp.route('/', methods=['GET'])
def get_table():
    with session_scope() as db_session:
        return {'items': TodoList.get_entries(db_session)}


@bp.route('/', methods=['PUT'])
def add_entry():
    with session_scope() as db_session:
        TodoList.add_entry(
            db_session=db_session,
            name=request.json['name'],
            priority=request.json['priority'])
        return 'OK'


@bp.route('/', methods=['POST'])
def update_entry():
    with session_scope() as db_session:
        TodoList.edit_entry(
            db_session=db_session,
            entry_id=int(request.json['id']),
            new_name=request.json['name'],
            new_priority=request.json['priority'])
    return 'OK'


@bp.route('/', methods=['DELETE'])
def delete_entry():
    with session_scope() as db_session:
        TodoList.delete_entry(
            db_session=db_session,
            entry_id=int(request.json['id']))
    return 'OK'
