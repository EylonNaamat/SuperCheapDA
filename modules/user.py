import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class User:
    def __init__(self,user) -> None:
        self.user = user

    def get_user(self, username, password):
        try:
            ref = db.reference(f'users/{username}')
            ans_user = ref.get()
            if ans_user is None:
                return {"ans":"badusername"}
            if str(password) != str(ans_user.get("password")):
                return {"ans":"badpassword"}
            ans_user["ans"] = "work"
            return ans_user
        except:
            return {"ans":"dabname"}
    
    def update_user(self):
        try:
            ref = db.reference('users')
            user_ref = ref.child(self.user.get("username"))
            user_ref.update(self.user)
        except:
            return {"ans": 'fail'}
        return {"ans": 'work'}


