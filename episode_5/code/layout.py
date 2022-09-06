# In this file we are going to demonstrate a simple
# layout with a window and two frames, using both the
# grid() and pack() layout managers and some buttons

import tkinter as tk


class SnappyTk(tk.Tk):
    """Our application window class

    Args:
        tk (tk.Tk): subclass the Tk() base class
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("A simple layout example")
        self.geometry("500x700")
        self.config(background="blue")

        # now we will add two frames to the window
        # we will use grid() here for the frames
        # in the top frame we will use pack() to show some buttons
        # in the bottom frame we will use grid() again to
        # show some more buttons

        frmTop = tk.Frame(bg="red")
        frmBottom = tk.Frame(bg="yellow")

        # use grid to show these in the main window
        frmTop.grid(row=0, column=0)
        frmBottom.grid(row=1, column=0)

        # add some buttons to the top frame and pack them
        btn1 = tk.Button(frmTop, text="Command 1")
        btn2 = tk.Button(frmTop, text="Command 2")
        btn3 = tk.Button(frmTop, text="Command 3")
        btn4 = tk.Button(frmTop, text="Command 4")
        btn1.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()

        # add some buttons to the bottom frame and grid them
        btn5 = tk.Button(frmBottom, text="Command 5")
        btn6 = tk.Button(frmBottom, text="Command 6")
        btn7 = tk.Button(frmBottom, text="Command 7")
        btn8 = tk.Button(frmBottom, text="Command 8")
        btn5.grid(row=0, column=0)
        btn6.grid(row=0, column=1)
        btn7.grid(row=1, column=0)
        btn8.grid(row=1, column=1)


if __name__ == "__main__":
    root = SnappyTk()
    root.mainloop()
