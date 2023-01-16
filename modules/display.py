from firebase_admin import db

class Display:
    def __init__(self, superid) -> None:
        self.super_id = superid

    def calculate_cart(self):
        try:
            ref = db.reference('Supers')
            super_ref = ref.child(self.super_id).child("products")
            super_ref = super_ref.get()
            super_ref["ans"] = "success"
        except:
            return {"ans": 'error'}

        return super_ref

    def get_rating(self):
        try:
            ref = db.reference('Supers')
            super_ref = ref.child(self.super_id).child("super_rating")
            super_ref = super_ref.get()
        except:
            return {"ans": 'error'}

        return {"ans": super_ref}

    def get_num_comments(self):
        try:
            ref = db.reference('Supers')
            super_ref = ref.child(self.super_id).child("comments_size")
            super_ref = super_ref.get()
        except:
            return {"ans": 'error'}

        return {"ans": super_ref}

    def get_super_name(self):
        try:
            ref = db.reference('Supers')
            super_ref = ref.child(self.super_id).child("super_name")
            super_ref = super_ref.get()
        except:
            return {"ans": 'error'}

        return {"ans": super_ref}