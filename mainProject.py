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



user1 = User(1, "Nikos", "nikos@test.com", False)
user2 = User(1, "Nikos", "nikos@test.com", True)
users=[]
users.append(user1)
users.append(user2)
service=UserService()
for user in service.activeUsers(users):
    print(user)
admin=Admin(1, "giannis", "giannis@test.com", True)
print (admin)
print (admin.permissions())