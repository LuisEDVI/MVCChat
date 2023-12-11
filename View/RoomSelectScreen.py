from View.ScreenBase import ScreenBase

import tkinter as tk
from tkinter import ttk
import threading

class RoomSelectScreen(ScreenBase):
    
    def goto_login(self):
        self.controller.change_screen('login')

    def join_room(self):
        room_thread =threading.Thread(target=self.set_room)
        room_thread.start()

    def set_room(self):
        id = self.roomid_entry.get()
        if not id:
            return  
        self.controller.connect_room(id)

    def set_elements(self):
        page_title_user = tk.Label(
            self.root,
            text="Olá " + self.controller.get_username(),
            font=('Kreon SemiBold', 30),
            fg="black", 
            bg="white"
        )

        self.current_canvas.create_window(340, 150, anchor=tk.W, window=page_title_user)

        page_title = tk.Label(
            self.root,
            text="Digite o ID da Sala",
            font=('Kreon SemiBold', 30),
            fg="black", 
            bg="white"
        )

        self.current_canvas.create_window(340, 230, anchor=tk.W, window=page_title)

        roomid_label = tk.Label(
            self.root,
            text="ID da sala:",
            font=('Kreon SemiBold', 16),
            fg="black",
            bg="white"
        )

        self.current_canvas.create_window(346, 340, anchor=tk.W, window=roomid_label)

        self.roomid_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Kreon SemiBold', 16), 
        )

        self.current_canvas.create_window(500, 380, window=self.roomid_entry)

        joinroom_button = tk.Button(
            self.root,
            text="Entrar",
            font=('Kreon SemiBold', 16),
            fg="white",
            bg="black",
            relief="flat",
            width="15",
            command=self.join_room
        )

        self.current_canvas.create_window(960, 625, anchor=tk.SE, window=joinroom_button)

        goBack_button = tk.Button(
            self.root,
            text="voltar",
            font=('Kreon SemiBold', 10),
            fg="white",
            bg="black", 
            relief="flat",
            width="10",
            height="1",
            command=self.goto_login
        )

        self.current_canvas.create_window(120, 618, anchor=tk.SE, window=goBack_button)