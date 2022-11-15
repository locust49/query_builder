from enum import Enum
from types import DynamicClassAttribute

# Logging file name
logFileName = "query-builder"


class MyEnum(Enum):
    @DynamicClassAttribute
    def value(self):
        """The value of the Enum member in uppercase."""
        return self._value_.upper()


# Enums
class Keyword(MyEnum):
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


class Types(MyEnum):
    ID = "id"
    INT = "int"
    TEXT = "text"
    SERIAL = "serial"


class Constraints(MyEnum):
    PRIMARY_KEY = "primary key"
    NOT_NULL = "not null"
    NULL = "null"
    UNIQUE = "unique"
    FOREIGN_KEY = "foreign key"
