from entity import Entity
from config.const import Types, Constraints
from database import MyDatabase

db = MyDatabase()
if db.getConnection() is not None:
    user_fields: list[tuple[str, Types, Constraints | list[Constraints] | None]] = [
        ("id", Types.SERIAL, [Constraints.PRIMARY_KEY, Constraints.NOT_NULL]),
        ("username", Types.TEXT, None),
        ("email", Types.TEXT, [Constraints.UNIQUE]),
        ("password", Types.TEXT, None),
    ]
    user = Entity("User", user_fields)
    user.create(db)
    res = user.save(db, ("slyazid", "slyazid@student.1337.ma", "1234"))
    res & user.save(db, ("aelouarg", "aelouarg@student.1337.ma", "5678"))
    res & user.save(
        db,
        [
            ("rel-hada", "rel-hada@student.1337.ma", "9012"),
            ("oaghzaf", "oaghzaf@student.1337.ma", "3456"),
        ],
    )
    res & user.save(db, ("mmounchi", "mmounchi@student.1337.ma"))
    res = user.save(db, ("test",))
    if res is False:
        print("One or many saving operation went wrong.")
else:
    print(
        "Could not make connection to database with the specified configuration...\nQuitting now."
    )
