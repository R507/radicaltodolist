from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from app.front.views import bp as bp_front
from app.back.views import bp as bp_back


def register_blueprints(app: 'Flask'):
    app.register_blueprint(bp_back)
    app.register_blueprint(bp_front)


def create_app(config=None):
    app = Flask(
        'todolist_app',
        static_url_path='/static_app/'  # without it'll conflict with platform_ui static folder
        # prolly should investigate simpler solution, since it kinda messy
    )

    app.config.update(dict(
        DEBUG=True,
        SECRET_KEY='development key',  # TODO: check wtf is this affects
        USERNAME='admin',
        PASSWORD='default',
    ))
    app.config.update(config or {})
    # app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    # app.register_blueprint(monitor_ui_bp, url_prefix='/monitor')
    register_blueprints(app)


    # app.debug = 1  # TODO: remove for prod

    return app
