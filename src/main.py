from typing import Union
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from modules.user import User

app = FastAPI()
cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://supercheapfirebase-default-rtdb.firebaseio.com/'
})


@app.get("/signin/getuser")
async def get_sighin_user(username:str, password:str):
    print("1")
    myUser = User({})
    print("11")
    return myUser.get_user(username, password)
    
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


@app.get("/items")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}