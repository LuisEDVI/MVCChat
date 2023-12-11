from View.ScreenBase import ScreenBase
import tkinter as tk
from tkinter import ttk

class LoginScreen(ScreenBase):

    def send_data(self):
        self.controller.log_user(self.username_entry.get(), self.password_entry.get())

    def goto_signup(self):
        self.controller.change_screen('signup')
    
    def set_elements(self):
        page_title = tk.Label(
            self.root,
            text="Login",
            font=('Kreon SemiBold', 45),
            fg="black", 
            bg="white"
        )

        self.current_canvas.create_window(426, 180, anchor=tk.W, window=page_title)

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

        login_button = tk.Button(
            self.root,
            text="Log In",
            font=('Kreon SemiBold', 16),
            fg="white",
            bg="black",
            relief="flat",
            width="15",
            command=self.send_data
        )

        self.current_canvas.create_window(960, 625, anchor=tk.SE, window=login_button)

        notAUserLabel_label = tk.Label(
            self.root,
            text="Não tem cadastro?",
            font=('Kreon SemiBold', 14),
            fg="black",
            bg="white"
        )

        self.current_canvas.create_window(30, 600, anchor=tk.W, window=notAUserLabel_label)

        goToSignup_button = tk.Button(
            self.root,
            text="Cadastro",
            font=('Kreon SemiBold', 10),
            fg="white",
            bg="black", 
            relief="flat",
            width="10",
            height="1",
            command=self.goto_signup
        )

        self.current_canvas.create_window(270, 618, anchor=tk.SE, window=goToSignup_button)