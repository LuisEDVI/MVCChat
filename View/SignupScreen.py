from View.ScreenBase import ScreenBase

import tkinter as tk
from tkinter import ttk

class SignupScreen(ScreenBase):

    def send_data(self):
        self.controller.create_user(self.username_entry.get(), self.password_entry.get(), self.confpassword_entry.get())

    def goto_login(self):
        self.controller.change_screen('login')

    def set_elements(self):
        page_title = tk.Label(
            self.root,
            text="Cadastro",
            font=('Kreon SemiBold', 45),
            fg="black", 
            bg="white"
        )

        self.current_canvas.create_window(385, 180, anchor=tk.W, window=page_title)

        username_label = tk.Label(
            self.root,
            text="Usuário:",
            font=('Kreon SemiBold', 16),
            fg="black",
            bg="white"
        )

        self.current_canvas.create_window(346, 260, anchor=tk.W, window=username_label)

        self.username_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Kreon SemiBold', 16), 
        )

        self.current_canvas.create_window(500, 300, window=self.username_entry)

        password_label = tk.Label(
            self.root,
            text="Senha:",
            font=('Kreon SemiBold', 16),
            fg="black",
            bg="white"
        )

        self.current_canvas.create_window(346, 350, anchor=tk.W, window=password_label)

        self.password_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Kreon SemiBold', 16),
        )
        
        self.current_canvas.create_window(500, 390, window=self.password_entry)

        confpassword_label = tk.Label(
            self.root,
            text="Confirmar Senha:",
            font=('Kreon SemiBold', 16),
            fg="black",
            bg="white"
        )

        self.current_canvas.create_window(346, 430, anchor=tk.W, window=confpassword_label)

        self.confpassword_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="25", 
            font=('Kreon SemiBold', 16),
        )
        
        self.current_canvas.create_window(500, 470, window=self.confpassword_entry)

        signup_button = tk.Button(
            self.root,
            text="Cadastrar",
            font=('Kreon SemiBold', 16),
            fg="white",
            bg="black",
            relief="flat",
            width="15",
            command=self.send_data
        )

        self.current_canvas.create_window(960, 625, anchor=tk.SE, window=signup_button)

        alreadya_user_label = tk.Label(
            self.root,
            text="Já tem cadastro?",
            font=('Kreon SemiBold', 14),
            fg="black",
            bg="white"
        )

        self.current_canvas.create_window(30, 600, anchor=tk.W, window=alreadya_user_label)

        goToSignin_button = tk.Button(
            self.root,
            text="login",
            font=('Kreon SemiBold', 10),
            fg="white",
            bg="black", 
            relief="flat",
            width="10",
            height="1",
            command=self.goto_login
        )

        self.current_canvas.create_window(254, 618, anchor=tk.SE, window=goToSignin_button)