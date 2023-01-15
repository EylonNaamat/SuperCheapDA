import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class User:
    def __init__(self,user) -> None:
        self.user = user

    def get_user(self, username, password):
        try:
            print("2")
            ref = db.reference(f'users/{username}')
            ans_user = ref.get()
            print("3")
            if ans_user is None:
                print("4")
                return {"ans":"badusername"}
            if str(password) != str(ans_user.get("password")):
                print("5")
                return {"ans":"badpassword"}
            ans_user["ans"] = "work"
            print("6")
            return ans_user
        except:
            return {"ans":"dabname"}


