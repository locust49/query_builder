from typing import Any
from config.const import Keyword, Types, Constraints
from config.loggingConfig import rootLogger

# TODO: define entity type instead of Any and fix circular import
# from entity import Entity


class Query:
    def __init__(self):
        rootLogger.info(msg="Instanciating {}".format(self.__class__.__name__))

    @staticmethod
    def listToTypedFields(
        mylist: list[tuple[str, Types, Constraints | list[Constraints] | None]]
    ) -> str:
        query = "("
        listLength = len(mylist)
        for columnName, columnType, columnConstraint in mylist:
            listLength -= 1
            query += columnName + " " + columnType.value.upper()
            if columnConstraint is not None:
                if type(columnConstraint) is list:
                    for constraint in columnConstraint:
                        query += " " + constraint.value.upper()
                elif type(columnConstraint) is Constraints:
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
    def save_record(entity: Any, entityValues: Any, fieldsName=None):
        """
            Generates an SQL query to save a record (a row) in the specified
        table.
        @params entity : Entity
        @params entityValues : tuple of the record values
                #   TODO create field class to match any entity fields.
        @params fieldsName : if None includes all columns of entity except
                            column with SERIAL type else TODO
        """
        if fieldsName is None:
            fields = entity.fields.copy()
            # Pop auto-generated primary key of type Types.SERIAL
            pk_index = [tup[1] for tup in entity.fields].index(Types.SERIAL)
            pk_tuple = fields.pop(pk_index)
            fields = list(zip(*fields))[0]
            if len(entityValues) > len(fields):
                rootLogger.error("Can not generate sql query.")
                return None
            if type(entityValues) is list and all(
                len(entity) < len(fields) for entity in entityValues
            ):
                fields = fields[0 : len(entity)]
            elif type(entityValues) is tuple and len(entityValues) < len(fields):
                fields = fields[0 : len(entityValues)]
            if len(fields) == 1:
                fields = str(fields).replace(",", "")
        saveQuery: str = (
            Keyword.INSERT.value
            + ' "'
            + entity.name
            + '" '
            + (
                str(fields).replace("'", '"') + " " if fieldsName is None else ""
            )  # TODO: implement else !
            + Keyword.VALUES.value
            + " "
            + (
                str(entityValues)
                if type(entityValues) is tuple and len(entityValues) != 1
                else (
                    str(entityValues).replace(",", "")
                    if len(entityValues) == 1
                    else ",".join([str(entityValue) for entityValue in entityValues])
                )
            )
            + ";"
        )
        rootLogger.debug("SQL query builed successfuly: ['{}']".format(saveQuery))
        return saveQuery
