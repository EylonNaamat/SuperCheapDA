import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Super:
    def __init__(self, super) -> None:
        self.super = super

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

    def findsuperId(self,super_name:str, super_city:str):
        ref = db.reference(f'Supers')
        snapshot  = ref.order_by_child('super_name').equal_to(super_name).get()
        for key,val in snapshot.items():
            if val.get("super_city") == super_city:
                return val.get("super_ID")
        return "fail"

    def add_comment(self,id_comment:str, super_id:str, user_username:str, grade, review:str):
        try:
            print(super_id)
            ref = db.reference(f'Supers/{super_id}')
            print("1")
            ref = ref.child("comments")
            print(id_comment)
            ref = ref.child(id_comment)
            print("4")
            ref.update({"id_comment":id_comment, "super_id":super_id, "user_username":user_username , "grade":grade, "review":review})
        except:
            return {"ans":"fail"}
        return {"ans":"work"}