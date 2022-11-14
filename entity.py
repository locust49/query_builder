from types import NoneType
from config.const import Types, Constraints
from config.loggingConfig import rootLogger
from query import Query


class Entity:
    name: str = ""
    fields: list[tuple[str, Types, Constraints | None]] = []

    def __init__(
        self, entityName, entityFields: list[tuple[str, Types, Constraints | None]]
    ) -> None:
        assert all(
            isinstance(element, tuple)
            and (
                list(map(type, element)) == [str, Types, Constraints]
                or list(map(type, element)) == [str, Types, NoneType]
            )
            for element in entityFields
        ), "Invalid fields parameters."
        assert (
            type(entityName) == str and entityName is not None and entityName != ""
        ), "Invalid entity name."
        self.name = entityName.lower()
        self.fields = entityFields
        rootLogger.info("Instanciating {}".format(self.__class__.__name__))

    def create(self, db):
        db.executeQuery(Query.create_entity(self))

    def save(self, db):
        self.queries.save_record(self)
