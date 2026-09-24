from pydantic import BaseModel,EmailStr, Field

class User():
    def __init__(self,id,name,email,active):
        self.id=id
        self.name=name
        self.email=email
        self.active=active    
    def __str__(self):
        return(f"{self.id} {self.name} {self.email} {self.active}" )
    
class Admin(User):
    def __init__(self, id, name, email, active):
         super().__init__(id, name, email, active)
    role:str="Admin"
    def __str__(self):
            return(f"{self.id} {self.name} {self.email} {self.active} {self.role}" )  
    def permissions(self):
         return ["create_user", "delete_user", "view_users"]
    
class Logger():
     pass
class UserService():
    def __init__(self):
          self.logger=Logger()
    def activeUsers(self,users):
        for user in users:
            if user.active:
             yield user
def logger(func):
    def wrapper(*args,**kargs):
        print("START")
        result=func(*args,**kargs)
        print("END")
        return result
    return wrapper

users=[]

@logger
def createUsers():
    print("users creation")
    user1 = User(1, "Nikos", "nikos@test.com", True)
    user2 = User(2, "giannis", "giannis@test.com", False)
    admin=Admin(1, "kostas", "kostas@test.com", True)
    users.append(admin)
    users.append(user1)
    users.append(user2)

@logger
def getUsers():
    print("users get")
    return users

createUsers()
users=getUsers()

service=UserService()
for user in service.activeUsers(users):
    print(user)
