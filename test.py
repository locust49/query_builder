from entity import Entity
from config.const import Types, Constraints
from database import MyDatabase

db = MyDatabase()
if db.getConnection() is not None:
    user_fields: list[tuple[str, Types, Constraints | None]] = [
        ("id", Types.INT, Constraints.PRIMARY_KEY),
        ("username", Types.TEXT, None),
        ("email", Types.TEXT, None),
        ("password", Types.TEXT, None),
    ]
    user = Entity("User", user_fields)
    user.create(db)
else:
    print(
        "Could not make connection to database with the specified configuration...\nQuitting now."
    )
