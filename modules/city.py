import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class City:
    def __init__(self, city_name) -> None:
        self.city_name = city_name

    def move_super(self,new_city, Super_Id):
        try:
            print("1")
            ref = db.reference(f'cities')
            print("2")
            ref.child(new_city).child(Super_Id).update({"active":True})
            print("3")
            ref = db.reference(f'cities').child(self.city_name).child(Super_Id)
            print("4")
            ref.delete()
            print("5")
            self.city_name = new_city
        except:
            return {"ans":"fail"}
        return {"ans":"work"}

    def iscity(this,city_name:str):
        try:
            ref = db.reference('cities')
            user_ref = ref.child(city_name)
            if user_ref.get() != None:
                return {"is_city":"exists"}
        except:
            return {"is_city": "doesnt exists"}

        return {"is_city": "doesnt exists"}


