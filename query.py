from typing import Any
from config.const import Keyword, Types, Constraints
from config.loggingConfig import rootLogger

# TODO: define entity type instead of Any and fix circular import
# from entity import Entity


class Query:
    def __init__(self):
        rootLogger.info(msg="Instanciating {}".format(self.__class__.__name__))

    @staticmethod
    def listToTypedFields(mylist: list[tuple[str, Types, Constraints | None]]) -> str:
        query = "("
        listLength = len(mylist)
        for columnName, columnType, columnConstraint in mylist:
            listLength -= 1
            query += columnName + " " + columnType.value.upper()
            if columnConstraint is not None:
                query += " " + columnConstraint.value.upper()
            if listLength > 0:
                query += ", "
            elif listLength == 0:
                query += ");"
        return query

    @staticmethod
    def create_entity(entity: Any) -> str:
        """
            Generates an SQL query to create an entity (a table) in the database
        if it does not exist.
        @params entity : Entity
        """
        createQuery: str = (
            Keyword.CREATE_TABLE.value
            + " "
            + Keyword.IF_NOT_EXIST.value
            + ' "'
            + entity.name
            + '" '
            + Query.listToTypedFields(entity.fields)
        )
        rootLogger.info(
            "Generate query of entity : {} with fields {}".format(
                entity.name, entity.fields
            )
        )
        rootLogger.debug("SQL query builed successfuly: ['{}']".format(createQuery))
        return createQuery

    @staticmethod
    def save_record(entity: Any, fieldsName=None):
        """
            Generates an SQL query to save a record (a row) in the specified
        table.
        @params entity : str
        @params record : #TODO create field class to match any entity fields.
        """
        if fieldsName is None:
            fields = list(zip(*entity.fields))[0]
            print(fields)
        saveQuery: str = Keyword.INSERT.value + ' "' + entity.name + '" '
        return saveQuery
