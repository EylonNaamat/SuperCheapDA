import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Super:
    def __init__(self, super) -> None:
        self.super = super
# ///////////////////////////michael///////////////////////
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
        
            ref = db.reference(f'Supers/{super_id}')
            ref = ref.child("new_comments")
            ref = ref.child(id_comment)
            ref.update({"id_comment":id_comment})

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

    def get_super_new_comment(self,super_ID):
        ref=db.reference(f'Supers/{super_ID}/new_comments')
        data=ref.get()
        ref.delete()
        return data

    def getComment(self,id_comment,super_ID):
        ref=db.reference(f'Supers/{super_ID}')
        ref = ref.child("comments")
        ref = ref.child(id_comment)
        data=ref.get()
        return data

# ///////////////////////////michael///////////////////////
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


    def additem(self,item_name:str, price:str, company:str,super_id:str):
        try:
            ref = db.reference(f'Supers/{super_id}/products/{item_name}')
            ref.update({company:price})
        except:
            return {"add_item": 'error'}

        return {"add_item": "good"}

    def delete_item(self,item_name:str, company:str, super_id:str):
        try:
            ref = db.reference(f'Supers/{super_id}/products/{item_name}/{company}')
            ref.delete()
        except:
            return {"delete_item": 'error'}

        return {"delete_item": "good"} 
    def delete_sale(self,sale_name:str,super_id:str):
        try:
            ref = db.reference(f'Supers/{super_id}/Sales')
            sale_ref = ref.child(sale_name)
            if sale_ref.get() == None:
                return {"delete_sale":"sale doesn't exists"}
            else:
                sale_ref.delete()
        except:
            return {"delete_sale": 'error'}

        return {"delete_sale": "good"}

    def dosale(self,item_name:str, saleQuantity:str,priceSale:str,company:str,sale_name:str,super_id:str):
    #check if the sale already exists
        try:
            ref = db.reference(f'Supers/{super_id}/Sales')
            user_ref = ref.child(sale_name)
            if user_ref.get() != None:
                return {"do_sale":"sale exists"}
        except:
            return {"do_sale": "error_search"}
        #check if the itemname and company doesnt exists in this super    
        try:
            ref = db.reference(f'Supers/{super_id}/products/{item_name}')
            user_ref = ref.child(company)
            print(user_ref.get())
            print(ref.get())
            if user_ref.get() == None:
                return {"do_sale":"doesnt exists"}
        except:
            return {"do_sale": "error_search"}
        #try insert sale
        try:
            ref = db.reference(f'Supers/{super_id}/Sales/{sale_name}')
            ref.update({"sale_name":sale_name,"item name":item_name,"company":company, "quantity":saleQuantity,"price":priceSale})
        except:
            return {"do_sale": 'error'}

        return {"do_sale": "good"}

    def isitem(self,item_name:str):
        try:
            ref = db.reference('dict_product')
            user_ref = ref.child(item_name)
            if user_ref.get() != None:
                return {"is_item":"exists"}
        except:
            return {"is_item": "doesnt exists"}

        return {"is_item": "doesnt exists"}