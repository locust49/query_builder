from enum import Enum

# Logging file name
logFileName = "query-builder"


# Enums
class Keyword(Enum):
    SELECT = "select"
    WHERE = "where"
    FROM = "from"
    WITH = "with"
    GROUP_BY = "group by"
    HAVING = "having"
    ORDER_BY = "order by"
    LIMIT = "limit"
    CREATE_TABLE = "create table"
    VALUES = "values"
    IF_NOT_EXIST = "if not exists"
    INSERT = "insert into"


class Types(Enum):
    ID = "id"
    INT = "int"
    TEXT = "text"


class Constraints(Enum):
    PRIMARY_KEY = "primary key"
    NOT_NULL = "not null"
    NULL = "null"
    FOREIGN_KEY = "foreign key"
