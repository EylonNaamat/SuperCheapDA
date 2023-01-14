from typing import Union
from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = FastAPI()
cred = credentials.Certificate('firebase-sdk.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://supercheapfirebase-default-rtdb.firebaseio.com/'
})


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/signup/user/checkuserexists")
async def get_user(username:str):
    try:
        ref = db.reference('users')
        user_ref = ref.child(username)
        if user_ref.get() != None:
            return {"user":"exists"}
    except:
        return {"user": "doesnt exists"}

    return {"user": "doesnt exists"}

@app.get("/signup/user/insertuser")
async def get_user(first_name:str, last_name:str, email:str, username:str, password:str, city:str, birth_date:str, gender:str, is_manager:str, super_id:str):
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
async def get_user(super_ID:str, super_name:str, super_city:str):
    PARAMS = {'super_ID':super_ID, 'super_name':super_name, 'super_city':super_city}
    try:
        ref = db.reference('Supers')
        user_ref = ref.child(super_ID)
        user_ref.update(PARAMS)
    except:
        return {"super": 'error'}

    return {"super": "success"}


@app.get("/signup/city/insertcity")
async def get_user(super_ID:str, super_name:str, super_city:str):
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
        # ref = db.reference(f"users/{username}/first_name")
    except:
        return {"Hello": 'error'}

    return {"Hello": first_name}

@app.get("/items")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}