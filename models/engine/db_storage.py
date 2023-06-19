#!/usr/bin/python3
"""this module defines a class to manage database for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User


class DBStorage:
    """database class"""
    __engine = None
    __session = None

    def __init__(self):
        """initialising the class objects begins here"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on all objects of a class or all classes"""
        class_list = [
            State, City, Place, Amenity, Review, User]

        rows = []

        if cls:
            rows = self.__session.query(cls)
        else:
            for cls in class_list:
                rows += self.__session.query(cls)
        return {type(v).__name__ + "." + v.id: v for v in rows}

    def new(self, obj):
        """add a new session"""
        self.__session.add(obj)

    def save(self):
        """save a new session created"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables and start a session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """remove an instance from the current session"""
        self.__session.remove()
