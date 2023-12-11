from Controller import Controller

import tkinter as tk
from tkinter import ttk

class ScreenBase:

    def __init__(self, view_setter):
        self.controller: Controller = view_setter.controller
        self.root = view_setter.root
        self.current_canvas = None

    
    def start_screen(self):
        self.current_canvas = tk.Canvas(self.root, width=1000, height=720, bg="white")
        self.current_canvas.pack()

        style = ttk.Style()
        style.configure('TEntry', relief='flat')

        self.set_elements()
    
    def set_elements(self):
        pass

    def destroy_screen(self):
        self.current_canvas.destroy()
    