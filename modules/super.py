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
            newAns["comments_size"] = str(ans_user.get("comments_size"))
            newAns["super_rating"] = str(ans_user.get("super_rating"))
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
            old_super = self.get_super(super_id)
            new_comments_size = int(old_super.get("comments_size"))+1
            new_rate = ((float(old_super.get("super_rating"))*int(old_super.get("comments_size")))+int(grade))/new_comments_size
            
            ref=db.reference(f'Supers/{super_id}')
            ref.update({"comments_size":new_comments_size})
            ref.update({"super_rating":new_rate})

            ref = db.reference(f'Supers/{super_id}')
            ref = ref.child("comments")
            ref = ref.child(id_comment)
            ref.update({"id_comment":id_comment, "super_id":super_id, "user_username":user_username , "grade":grade, "review":review})
        except:
            return {"ans":"fail"}
        return {"ans":"work"}
    
    def getComments(self,super_name:str, super_city:str):
        try:
            my_super_id = self.findsuperId(super_name,super_city)
            ref=db.reference(f'Supers/{my_super_id}')
            ref = ref.child("comments")
            ans_comments = ref.get()
        except:
            return {"ans":"fail"}
        if ans_comments is None:
            return {"ans":"fail"}
        ans_comments["ans"]= "success"
        return ans_comments

    def getSales(self,super_name:str, super_city:str):
        try:
            my_super_id = self.findsuperId(super_name,super_city)
            ref=db.reference(f'Supers/{my_super_id}')
            ref = ref.child("Sales")
            ans_sales = ref.get()
        except:
            return {"ans":"fail"}
        if ans_sales is None:
            return {"ans":"fail"}
        ans_sales["ans"]= "success"
        return ans_sales
