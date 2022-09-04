# This file will test out various options we can set on
# a tkinter application object.

import tkinter as tk


class snappytk(tk.Tk):
    """This is our base application class for the 
    tkinter GUI window

    Args:
        tk (tk.Tk): Subclass to show a tkinter window
    """

    def __init__(self, *args, **kwargs):
        super().__init__()

        # Lets add some buttons to see how it looks
        for i in range(5):
            btn = tk.Button(self, text=f"Command {i}")
            btn.pack(padx=5, pady=5)

        # We can give our application a title
        self.title("GUI with Tkinter")

        # Now we can set a size for our window
        self.geometry("300x250")

        # We can move the window around the screen
        # with some extra values in the geometry string
        # positive values move the window from the left side of the screen
        # negative values move the window from the right side of the screen
        self.geometry("+1000+300")

        # We can specify a min and max size for the window
        # when it is resizable
        self.minsize(width=200, height=300)
        # self.maxsize(width=500, height=600)

        # We can limit the window to not allow resizing in both directions
        # self.resizable(0, 0)

        # In Windows we can change the icon showing in the title bar
        # self.iconbitmap("episode_3/pics/snappytk.ico")

        # We can change attributes for windows to do a variety of things
        # These depend on which operating system you are running
        # Lets get a list of the available attributes first
        # print(self.attributes())

        # We can make the window a 'toolwindow'
        # self.attributes("-toolwindow", 1)

        # We can make the window go full screen
        # self.attributes("-fullscreen", 1)

        # We can disable or make our window show on top of other windows
        # self.attributes("-disabled", 1)
        # self.attributes("-topmost", 1)

        # We can set the window to be transparent
        # self.attributes("-alpha", 0.1)

        # If we use a background colour we can make a transparent window
        # in a slightly more flexible way
        self.config(bg="green")
        self.attributes("-transparentcolor", "green")

        # We can make a 'floating' window that has been
        # stripped of all decorations
        self.overrideredirect(1)


if __name__ == "__main__":
    root = snappytk()
    root.mainloop()
