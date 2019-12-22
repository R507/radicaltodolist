from app.views import create_app
from app.utils.logger import setup_logging
from app.utils.deploy_db import deploy_db
from app.settings import SERVER_ADDRESS, SERVER_PORT


def main():
    setup_logging()
    deploy_db()
    app = create_app()
    print(app.url_map)  # some debug info
    app.run(host=SERVER_ADDRESS, port=SERVER_PORT)


if __name__ == '__main__':
    main()
