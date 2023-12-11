from Model.Model import Model
import sys
import asyncio

class Controller:

    def __init__(self):
        self.View = None
        self.Model = None
        self.loop = asyncio.get_event_loop()

    def set_view(self, ViewSetter):
        self.View = ViewSetter

    def set_model(self, Model: Model):
        self.Model = Model

    def create_user(self, username, password, coonfpassword):
        if password != coonfpassword:
            self.View.alert('password_mismatch')
            return
        res = self.Model.post_user(username, password)
        if res == 'user_exists':
            self.View.alert(res)
            return
        else:
            self.change_screen('roomselect')

    def log_user(self, username, password):
        res = self.Model.user_login(username, password)
        if res == 'invalid_credentials':
            self.View.alert(res)
            return
        else:
            self.change_screen('roomselect')

    def connect_room(self, code):
        task = self.loop.create_task(self.Model.server_connection(code))
        self.loop.run_until_complete(task)
        self.change_screen('room')

        message_task = self.loop.create_task(self.listen_message())
        send_message_task = self.loop.create_task(self.send_message(True, None))

        self.loop.run_until_complete(asyncio.gather(message_task, send_message_task)) 
             
    async def listen_message(self):
        while True:
            msg = await self.Model.get_message()
            if not msg == None:
                self.View.chatroom_screen.add_message(msg['Message'])
            
    async def send_message(self, isConnection, message):
        await self.Model.send_message(isConnection, message)
        
    def get_username(self):
        return self.Model.user.username
    
    def get_roomid(self):
        return self.Model.room.id
            
    def change_screen(self, screen_name):
        self.View.set_screen(screen_name)

    def close_app(self):
        self.View.root.destroy()
        sys.exit(1)
