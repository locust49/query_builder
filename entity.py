from types import NoneType
from config.const import Types, Constraints
from config.loggingConfig import rootLogger
from query import Query


class Entity:
    name: str = ""
    fields: list[tuple[str, Types, Constraints | list[Constraints] | None]] = []

    def __init__(
        self,
        entityName,
        entityFields: list[tuple[str, Types, Constraints | list[Constraints] | None]],
    ) -> None:
        assert all(
            isinstance(element, tuple)
            and (
                list(map(type, element)) == [str, Types, Constraints]
                or list(map(type, element))
                == [str, Types, list]  # TODO verify list elements
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

    def create(self, db) -> bool:
        try:
            db.executeQuery(Query.create_entity(self))
            return True
        except:
            return False

    def save(self, db, record: tuple | list[tuple]) -> bool:
        try:
            save_query = Query.save_record(self, record)
            if save_query is not None:
                db.executeQuery(save_query)
            else:
                return False
            return True
        except:
            return False
