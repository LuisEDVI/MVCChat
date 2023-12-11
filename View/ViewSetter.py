from View.LoginScreen import LoginScreen
from View.SignupScreen import SignupScreen
from View.RoomSelectScreen import RoomSelectScreen
from View.ChatRoomScreen import ChatRoomScreen
import Errors

import tkinter as tk
from tkinter import messagebox

import pyglet

class ViewSetter:

    def __init__(self, controller):
        self.controller = controller

        
        self.root = tk.Tk()
        
        self.root.title("Anon Chat")
        self.root.geometry("1000x640")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", controller.close_app)

        self.container = tk.Frame(self.root)
        self.container.pack()

        self.active_screen = 'login'

        self.login_screen = LoginScreen(self)
        self.singnup_screen = SignupScreen(self)
        self.roomselect_screen = RoomSelectScreen(self)
        self.chatroom_screen = ChatRoomScreen(self)

        self.screens = {
            'login': self.login_screen,
            'signup': self.singnup_screen,
            'roomselect': self.roomselect_screen,
            'room': self.chatroom_screen,
        }

        self.screens[self.active_screen].start_screen()


    def set_screen(self, screen_name):
        self.screens[self.active_screen].destroy_screen()
        self.active_screen = screen_name
        self.screens[screen_name].start_screen()

    def start(self):
        self.root.mainloop()

    def alert(self, message):
        messagebox.showerror("Warning", Errors.get_error(message))
