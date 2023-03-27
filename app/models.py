from typing import Type
import config
from cachetools import cached
from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Ad(Base):

    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())


@cached({})
def get_engine():
    return create_engine(config.PG_DSN)


@cached({})
def get_session_maker():
    return sessionmaker(bind=get_engine())


def init_db():
    Base.metadata.create_all(bind=get_engine())


def close_db():
    get_engine().dispose()

ORM_MODEL_CLS = Type[Ad]
ORM_MODEL = Ad