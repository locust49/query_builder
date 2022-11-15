from typing import Any
import psycopg2
from config.dbConfig import db_config
from config.loggingConfig import rootLogger


class MyDatabase(object):
    def __init__(self):
        try:
            self.__connection = psycopg2.connect(**db_config)
            self.__cursor = self.__connection.cursor()
            rootLogger.info(
                "Connecting to database [{}].".format(db_config["database"])
            )
        except psycopg2.DatabaseError as error:
            rootLogger.info("An error occured during connection {}\n".format(db_config))
            rootLogger.error(error)

    def getCursor(self) -> Any:
        return self.__cursor

    def getConnection(self) -> Any:
        if hasattr(self, "_MyDatabase__connection"):
            return self.__connection
        else:
            return None

    def executeQuery(self, query: str):
        if self.getConnection() is not None:
            self.__cursor.execute(query)
            self.__connection.commit()
            rootLogger.info("Executing query : '{}'".format(query))

    def __del__(self):
        if self.getConnection() is not None:
            self.__connection.close()
            rootLogger.info(
                "Disconnecting from database [{}].".format(db_config["database"])
            )
