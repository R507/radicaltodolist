from app.server import run_server
from app.utils.logger import setup_logging
from app.utils.deploy_db import deploy_db


if __name__ == '__main__':
    setup_logging()
    deploy_db()
    run_server()
