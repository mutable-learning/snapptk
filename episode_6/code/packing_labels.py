import tkinter as tk
from tkinter import ttk

class SnappyTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Adding labels using pack()")
        self.geometry("500x400")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="grey")

        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(fill=tk.BOTH, expand=1)

        self.first = ttk.Label(self.container_frame, text="first", background="yellow", anchor=tk.SW)
        self.first.pack(fill=tk.BOTH,expand=1, side=tk.TOP)

        self.second = ttk.Label(self.container_frame, text="second", background="green", anchor=tk.SW)
        self.second.pack(fill=tk.BOTH,expand=1, side=tk.LEFT)

        self.third = ttk.Label(self.container_frame, text="third", background="orange", anchor='center')
        self.third.pack(fill=tk.BOTH,expand=1, side=tk.BOTTOM)

        self.fourth = ttk.Label(self.container_frame, text="fourth", background="pink")
        self.fourth.pack(fill=tk.BOTH,expand=1, side='right')

if __name__=="__main__":
    root=SnappyTk()
    root.mainloop()