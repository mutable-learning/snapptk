# In this file we will test out different layout managers
# to see how they work to show widgets in the window

import tkinter as tk


class SnappyTk(tk.Tk):
    """Just showing a window with a button to test
    different layout managers

    Args:
        tk (tk application): Application window class
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Layout Mangers - testing")
        self.geometry("300x250")

        btnClickMe = tk.Button(self, text="Click Me")
        btnClickMe.grid()

        btnClickMe2 = tk.Button(self, text="Click Me2")
        btnClickMe2.grid(row=1, column=1)


if __name__ == "__main__":
    root = SnappyTk()
    root.mainloop()
