import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Super:
    def __init__(self, super) -> None:
        self.Super_Id = super

    def get_super(self,Super_Id):
        try:
            ref = db.reference(f'Supers/{Super_Id}')
            ans_user = ref.get()
            if ans_user is None:
                return {"ans":"fail"}
            newAns = {}
            newAns["ans"] = "work"
            newAns["super_name"] = str(ans_user.get("super_name"))
            newAns["super_city"] = str(ans_user.get("super_city"))
            return newAns
        except:
            return {"ans":"fail"}
    
    def set_super(self,Super_Id:str,super_name:str, super_city:str):
        ref = db.reference(f'Supers/{Super_Id}')
        ref.update({"super_name":super_name,"super_city":super_city})
        
        return self.get_super(Super_Id)