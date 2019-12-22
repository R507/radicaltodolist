import json
import logging
import typing
import datetime

if typing.TYPE_CHECKING:
    from sqlalchemy.orm import Session

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, JSON
from sqlalchemy import TypeDecorator
from sqlalchemy import desc
from sqlalchemy.ext import mutable
from sqlalchemy.orm import relationship

from app.back.db import Base


LOGGER = logging.getLogger(__name__)


class TodoList(Base):
    __tablename__ = "todolist"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    priority = Column(String, nullable=False)  # TODO: make enum instead of string
    date_created = Column(DateTime, nullable=False)

    def to_dict(self):
        # TODO: proper marshaling
        result = {
            'id': self.id,
            'name': self.name,
            'priority': self.priority,
            'date_created': self.date_created,
        }
        return result

    @classmethod
    def get_entries(cls, db_session: 'Session'):
        LOGGER.debug('Getting all entries')
        result = db_session.query(cls).all()
        result = [item.to_dict() for item in result]  # TODO: probably not the best place for it
        return result

    @classmethod
    def add_entry(cls, db_session: 'Session', name: str, priority):
        LOGGER.debug('Adding entry with name %s and priority %s', name, priority)
        entry = cls(
            name=name,
            priority=priority,
            date_created=datetime.datetime.now())
        db_session.add(entry)

    @classmethod
    def edit_entry(cls, db_session: 'Session', entry_id: int, new_name: str, new_priority):
        LOGGER.debug('Updating entry with id %s', entry_id)
        entry = db_session.query(cls).filter(cls.id == entry_id).one()
        entry.name = new_name
        entry.priority = new_priority

    @classmethod
    def delete_entry(cls, db_session: 'Session', entry_id: int):
        LOGGER.debug('Deleting entry with id %s', entry_id)
        db_session.query(cls).filter(cls.id == entry_id).delete()
