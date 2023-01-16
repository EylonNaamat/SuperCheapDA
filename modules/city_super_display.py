from firebase_admin import db

class City:
    def __init__(self,city) -> None:
        self.city = city

    def get_supers(self):
        try:
            ref = db.reference('cities')
            city_ref = ref.child(self.city)
            city_ref = city_ref.get()
            city_ref["ans"] = 'success'
        except:
            return {"ans": 'error'}

        return city_ref