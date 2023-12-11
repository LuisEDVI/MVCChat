from Model.User import User
from Model.Room import Room

import pymongo
import websockets
import json

class Model:
    
    server_uri = "ws://localhost:8765"
    connection = pymongo.MongoClient('mongodb://localhost:27017')

    db = connection['UserData']
    collection = db['User']

    def __init__(self):
        self.user = User()
        self.room = Room()
        self.websocket = None

    def post_user(self, username, password):
        if self.get_user_by_name(username) != None:
            return 'user_exists'
        self.collection.insert_one({
            "name": username,
            "password": password,
        })
        self.user_setup(username)
        return 'success'
    
    def user_login(self, username, password):
        if self.collection.find_one({
            "name": username,
            "password": password
        }) == None:
            return 'invalid_credentials'
        self.user_setup(username)
        return 'success'
    
    def user_setup(self, username):
        self.user.set_username(username)

    def get_user_by_name(self, username):
        return self.collection.find_one({
            "name":username
        }) 

    async def server_connection(self, code):
        self.room.set_id(code)
        print("Conectando...")
        self.websocket = await websockets.connect(self.server_uri)
        print("Conectado!")
    
    async def get_message(self):
        msg = await self.websocket.recv()
        return json.loads(msg)

    
    async def send_message(self, firstconnection, message):
        if not message:
            message = "O Usuário " + self.user.username +  " conectou-se à sala"
        else:
            message = self.user.username + ": " + message
        dict_message = {
            'first_connection': firstconnection,
            'RoomID': self.room.id,
            'Message': message
        }
        if self.websocket:
            print("Enviando mensagem: %s", dict_message)
            try:
                await self.websocket.send(json.dumps(dict_message))
                print("Mensagem enviada com sucesso.")
            except Exception as e:
                print(e)
        else:
            print("sem conexão")

