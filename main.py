users = [
    {"name": "Nikos", "active": True},
    {"name": "Maria", "active": False},
    {"name": "Giorgos", "active": True},
    {"name": "Nikos", "active": True},
]

def active_users(users):
    for user in users:
        if user["active"]:
            yield user
for user in active_users(users):
    print(user)