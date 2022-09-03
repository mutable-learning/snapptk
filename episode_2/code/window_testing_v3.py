# Create the gui as a class so that we can re-use our code in
# other projects if we want to. This is an example of Encapsulation
# and we will look at this more in future episodes.

import tkinter as tk


class my_gui(tk.Tk):
    """
    A class to hold our application so we can import it into
    other projects if we want to.   

    Args:
        tk (tkinter root window): The root object for the tkinter interface
    """

    def __init__(self, *args, **kwargs):
        super().__init__()


# If the file is run as a script the code below will run and the interface will
# display. If it is imported into another project, the my_gui class will be
# available to use, but the code below will not run automatically.
if __name__ == "__main__":
    root = my_gui()
    root.mainloop()
