import os
import logging

from app.back import db
from app.back import models
from app.settings import DB_NAME

_ = models


LOGGER = logging.getLogger(__name__)


def deploy_db():
    if os.path.isfile(DB_NAME):
        LOGGER.info('DB with name %s already exists', DB_NAME)
    else:
        LOGGER.info('Creating DB with name %s', DB_NAME)
        db.Base.metadata.create_all(db.engine)
