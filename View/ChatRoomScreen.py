from View.ScreenBase import ScreenBase

import tkinter as tk
import asyncio
from tkinter import ttk, Canvas, Scrollbar

class ChatRoomScreen(ScreenBase):

    def send_message(self):
        msg = self.message_entry.get()
        if not msg:
            return
        asyncio.run(self.controller.send_message(False, msg))
        self.message_entry.delete(0, tk.END)

    def exit_app(self):
        self.controller.close_app()

    def on_mouse_scroll(self, event):
        self.message_box_canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def add_message(self, message):
        label = tk.Label(
            self.message_box,
            font=("Kreon SemiBold", 16),
            text=message, 
            anchor="w",
            bg="white",
            fg="black",
            wraplength=950,
            justify="left"
        )

        self.i += 1
        label.grid(row=self.i, column=0, sticky="ew")

        self.current_canvas.update_idletasks() 

    def set_elements(self):
        self.i = 0
        connected_as = tk.Label(
            self.root,
            text="Conectado como: " + self.controller.get_username(),
            font=('Kreon SemiBold', 16),
            fg="black", 
            bg="white"
        )

        self.current_canvas.create_window(20, 25, anchor=tk.W, window=connected_as)

        room_id = tk.Label(
            self.root,
            text="ID da sala atual: " + self.controller.get_roomid(),
            font=('Kreon SemiBold', 16),
            fg="black", 
            bg="white"
        )

        self.current_canvas.create_window(20, 60, anchor=tk.W, window=room_id)


        change_room_button = tk.Button(
            self.root,
            text="SAIR",
            font=('Kreon SemiBold', 10),
            fg="white",
            bg="red", 
            relief="flat",
            width="15",
            height="1",
            command=self.exit_app
        )

        self.current_canvas.create_window(980, 65, anchor=tk.SE, window=change_room_button)

        # Frame scrollável com tamanho fixo
        message_box_frame = ttk.Frame(
            self.root,
            width=960,
            height=480
        )
        
        self.current_canvas.create_window(980, 565, anchor=tk.SE, window=message_box_frame)

        # Crie um canvas dentro do frame
        self.message_box_canvas = Canvas(
            message_box_frame,
            width=940,
            height=480,
            bg="white",
        )

        self.message_box_canvas.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(
            message_box_frame,
            orient="vertical",
            command=self.message_box_canvas.yview
        )
        
        scrollbar.pack(side="right", fill="y")

        self.message_box_canvas.configure(yscrollcommand=scrollbar.set)

        # Crie um frame interno para conter o conteúdo
        self.message_box = ttk.Frame(
            self.message_box_canvas
        )

        self.message_box_canvas.create_window((0, 0), window=self.message_box, anchor="nw")

        self.current_canvas.update_idletasks()  # Atualize o canvas

        # Configurar a região de rolagem
        self.message_box_canvas.config(scrollregion=self.message_box.bbox("all"))

        self.root.bind_all("<MouseWheel>", self.on_mouse_scroll)

        self.message_entry = ttk.Entry(
            self.root, 
            style='TEntry', 
            width="71",
            font=('Kreon SemiBold', 16), 
        )

        self.current_canvas.create_window(450, 597, window=self.message_entry)

        send_message_button = tk.Button(
            self.root,
            text="Enviar",
            font=('Kreon SemiBold', 11),
            fg="white",
            bg="black",
            relief="flat",
            width="10",
            height="1",
            command=self.send_message
        )

        self.current_canvas.create_window(980, 617, anchor=tk.SE, window=send_message_button)
    