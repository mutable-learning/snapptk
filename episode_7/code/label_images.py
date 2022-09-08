import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class SnappyTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Showing images with label widgets")
        self.geometry("600x300")

        self.style = ttk.Style()
        self.style.configure("TFrame", background="grey")

        self.container_frame = ttk.Frame(self)
        self.container_frame.pack(fill=tk.BOTH, expand=1)

        self.pic = tk.PhotoImage(file="episode_7/pics/dog.png")
        self.dog = ttk.Label(self.container_frame, text="dog",
                             image=self.pic, compound="bottom")
        self.dog.pack(side='left')

        self.pic2 = tk.PhotoImage(file="episode_7/pics/bird.png")
        self.pic2 = self.pic2.subsample(4, 4)
        self.bird = ttk.Label(self.container_frame, text="bird",
                              image=self.pic2, compound="top")
        self.bird.pack(side='left')

        self.pic3 = Image.open("episode_7/pics/fish.png")
        self.pic3 = ImageTk.PhotoImage(self.pic3.resize((50, 50)))
        self.fish = ttk.Label(self.container_frame, text="fish",
                              image=self.pic3, compound="top")
        self.fish.pack(side='left')

        self.pic4 = Image.open("episode_7/pics/cat.png")
        self.pic4.thumbnail((50, 50))
        self.pic4 = ImageTk.PhotoImage(self.pic4)
        self.cat = ttk.Label(self.container_frame, text="cat",
                             image=self.pic4, compound="top")
        self.cat.pack(side='left')


if __name__ == "__main__":
    root = SnappyTk()
    root.mainloop()
