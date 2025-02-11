from models import UserLevel

rules: dict[str, tuple[str, list[UserLevel]]] = {
    "user_read": (
        "Can read list of users",
        [UserLevel.ADMINISTRATOR, UserLevel.SUPERINTENDENT],
    ),
    "user_create": (
        "Can create new users",
        [UserLevel.ADMINISTRATOR, UserLevel.SUPERINTENDENT],
    ),
    "user_modify": ("Can edit existing users", [UserLevel.SUPERINTENDENT]),
    "user_disable": ("Can disable existing users", [UserLevel.SUPERINTENDENT]),
    "sc_global_read": (
        "Can read all school canteens",
        [UserLevel.ADMINISTRATOR, UserLevel.SUPERINTENDENT],
    ),
    "sc_global_create": (
        "Can create new school canteens",
        [UserLevel.ADMINISTRATOR, UserLevel.SUPERINTENDENT],
    ),
    "sc_global_modify": (
        "Can edit existing school canteens",
        [UserLevel.ADMINISTRATOR, UserLevel.SUPERINTENDENT],
    ),
    "sc_global_disable": (
        "Can disable exiting school canteens",
        [UserLevel.SUPERINTENDENT],
    ),
    "sc_local_modify": (
        "Can edit school canteens they are assigned to",
        [
            UserLevel.ADMINISTRATOR,
            UserLevel.SUPERINTENDENT,
            UserLevel.PRINCIPAL,
        ],
    ),
}
