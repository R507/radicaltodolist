from flask import Blueprint, render_template


# bp = Blueprint(
#     'front',
#     __name__,
#     static_folder='todolist/build/static/',
#     static_url_path='/static/',
#     template_folder='todolist/build/',)

bp = Blueprint(
    'front',
    __name__,
    static_folder='todolist/build/',
    template_folder='todolist/build/',)


@bp.route('/')
def starting_page():
    # pretty sure this is not the best solution for deploying react UI, yet it's pretty simplistic
    # and probably is good enough for this project
    return render_template("index.html")
