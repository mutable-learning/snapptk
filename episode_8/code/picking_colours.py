# A simple window that will allow for a colour to
# be chosen and then change the widgets background colours.

import tkinter as tk
from tkinter import colorchooser


class SnappyTk(tk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master)

        self.configure_ui()
        self.create_interface()

    def configure_ui(self):
        self.config(bg="#ffffff")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_interface(self):
        self.colour = tk.StringVar(value='#ffffff')
        self.colour_label = tk.Label(
            self, textvariable=self.colour, bg=self.colour.get())
        self.colour_label.grid(row=0, column=0, sticky=tk.S)
        self.colour_button = tk.Button(
            self, text="Select a colour", command=self.select_color)
        self.colour_button.grid(row=1, column=0)

    def select_color(self):
        self.colour.set(colorchooser.askcolor(title="Pick a colour")[-1])
        self.config(background=self.colour.get())
        self.colour_label.config(background=self.colour.get())


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.frame = SnappyTk(root)
    root.frame.pack(fill=tk.BOTH, expand=1)
    root.mainloop()
