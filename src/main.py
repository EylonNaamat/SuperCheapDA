from typing import Union
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from modules.user import User
from modules.super import Super
from modules.city import City
from modules.city_super_display import City_super
from modules.display import Display

app = FastAPI()
cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://supercheapfirebase-default-rtdb.firebaseio.com/'
})

# //////////////////////michael////////////////////////////
@app.get("/signin/getuser")
async def get_sighin_user(username:str, password:str):
    print("1")
    myUser = User({})
    print("11")
    return myUser.get_user(username, password)
    
@app.get("/mysuper/getsuper")
async def get_super_info(Super_Id:str):
    tempMySuper = Super({})
    stam =  tempMySuper.get_super(Super_Id)
    return stam

@app.get("/mysuper/setsuper")
async def set_super_info(Super_Id:str, super_name:str, super_city:str):
    tempMySuper = Super({})
    stam =  tempMySuper.set_super(Super_Id,super_name,super_city)
    return stam

@app.get("/mysuper/movesuper")
async def add_super_to_city(old_city:str, new_city:str, Super_Id:str):
    tempMySuper = City(old_city)
    stam =  tempMySuper.move_super(new_city,Super_Id)
    return stam

@app.get("/myaccount/setuser")
async def insertuser(first_name:str, last_name:str, email:str, username:str, password:str, city:str, birth_date:str, gender:str, is_manager:str, super_id:str):
    temp_user = User({'first_name':first_name, 'last_name':last_name, 'email':email, 'username':username,
            'password':password, 'city':city, 'birth_date':birth_date, 'gender':gender, 'is_manager':is_manager,
            'super_id':super_id})
    stam = temp_user.update_user()
    return stam

@app.get("/addcomment")
async def add_comment(id_comment:str, super_name:str, super_city:str, user_username:str, grade, review:str):
    tempSuper = Super({})
    super_id = tempSuper.findsuperId(super_name,super_city)
    if super_id == "fail":
        return {"ans":"fail"}
    stam =  tempSuper.add_comment(id_comment, super_id, user_username, grade, review)
    return stam

#http://localhost:5001/addcomment?id_comment=123456&super_name=bar%20col&super_city=Tel Aviv&user_username=Ariel&grade=hatzlaha&review=Ariel

@app.get("/displaycomment")
async def display_comment(super_name:str, super_city:str):
    tempSuper = Super({})
    stam =  tempSuper.getComments(super_name,super_city)
    return stam

@app.get("/displaysale")
async def display_sale(super_name:str, super_city:str):
    tempSuper = Super({})
    stam =  tempSuper.getSales(super_name,super_city)
    return stam

@app.get("/getnewcomments")
async def get_new_comments(super_ID:str):
    temp_super = Super({})
    stam =  temp_super.get_super_new_comment(super_ID)
    return stam

#http://localhost:5001/getnewcomments?super_ID=00a0248a-3657-4b1d-8445-8b813bfd954e

@app.get("/getcomment")
async def get_comment(id_comment:str,super_ID:str):
    temp_super = Super({})
    stam =  temp_super.getComment(id_comment,super_ID)
    return stam

    

# //////////////////////eylon////////////////////////////
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/signup/user/checkuserexists")
async def checkuserexists(username:str):
    try:
        ref = db.reference('users')
        user_ref = ref.child(username)
        if user_ref.get() != None:
            return {"user":"exists"}
    except:
        return {"user": "doesnt exists"}

    return {"user": "doesnt exists"}

@app.get("/signup/user/insertuser")
async def insertuser(first_name:str, last_name:str, email:str, username:str, password:str, city:str, birth_date:str, gender:str, is_manager:str, super_id:str):
    PARAMS = {'first_name':first_name, 'last_name':last_name, 'email':email, 'username':username,
            'password':password, 'city':city, 'birth_date':birth_date, 'gender':gender, 'is_manager':is_manager,
            'super_id':super_id}
    try:
        ref = db.reference('users')
        user_ref = ref.child(username)
        user_ref.update(PARAMS)
    except:
        return {"user": 'error'}

    return {"user": "success"}

@app.get("/signup/super/insertsuper")
async def insertsuper(super_ID:str, super_name:str, super_city:str, comments_size:str, super_rating:str):
    PARAMS = {'super_ID':super_ID, 'super_name':super_name, 'super_city':super_city, 
            'comments_size':comments_size, 'super_rating':super_rating}
    try:
        ref = db.reference('Supers')
        user_ref = ref.child(super_ID)
        user_ref.update(PARAMS)
    except:
        return {"super": 'error'}

    return {"super": "success"}


@app.get("/signup/city/insertcity")
async def insertcity(super_ID:str, super_city:str):
    PARAMS = {"active":True}
    try:
        ref = db.reference('cities')
        city_ref = ref.child(super_city)
        city_ref = city_ref.child(super_ID)
        city_ref.update(PARAMS)
    except:
        return {"city": 'error'}

    return {"city": "success"}

# http://localhost:5001/displaysuper/getsupers?city=Ariel
@app.get("/displaysuper/getsupers")
async def get_supers(city:str):
    curr_city = City_super(city)
    temp = curr_city.get_supers()
    return temp

@app.get("/displaysuper/calculatecart")
async def get_supers(superid:str):
    display_super = Display(superid)
    temp = display_super.calculate_cart()
    return temp

@app.get("/displaysuper/getrating")
async def get_rating(superid:str):
    display_super = Display(superid)
    rating = display_super.get_rating()
    return rating

@app.get("/displaysuper/getnumcomments")
async def get_num_comments(superid:str):
    display_super = Display(superid)
    num_comments = display_super.get_num_comments()
    return num_comments

@app.get("/displaysuper/getsupername")
async def get_super_name(superid:str):
    display_super = Display(superid)
    super_name = display_super.get_super_name()
    return super_name





@app.get("/signup/user")
async def get_user(first_name:str, last_name:str, email:str, username:str, password:str, city:str, birth_date:str, gender:str, is_manager:str, super_id:str):
    PARAMS = {'first_name':first_name, 'last_name':last_name, 'email':email, 'username':username,
    'password':password, 'city':city, 'birth_date':birth_date, 'gender':gender, 'is_manager':is_manager,
    'super_id':super_id}

    try:
        ref = db.reference('users')
        user_ref = ref.child(username)
        user_ref.update(PARAMS)
    except:
        return {"Hello": 'error'}

    return {"Hello": first_name}


#//////////////////////////// Ben /////////////////////

@app.get("/additem")
def addItem(item_name:str, price:str, company:str,super_id:str):
    super = Super({})
    return super.additem(item_name,price,company,super_id)


@app.get("/deleteitem")
def delete_item(item_name:str, company:str, super_id:str):
    super = Super({})
    return super.delete_item(item_name,company,super_id)

@app.get("/deletesale")
def delete_sale(sale_name:str,super_id:str):
    super = Super({})
    return super.delete_sale(sale_name,super_id)


@app.get("/dosale")
def dosale(item_name:str, saleQuantity:str,priceSale:str,company:str,sale_name:str,super_id:str):
    super = Super({})
    return super.dosale(item_name,saleQuantity,priceSale,company,sale_name,super_id)

@app.get("/iscity")
def iscity(city_name:str):
    city = City({})

    return city.iscity(city_name)

@app.get("/isitem")
def isitem(item_name:str):
    super = Super({})
    return super.isitem(item_name)






#//////////////////////////////////////////