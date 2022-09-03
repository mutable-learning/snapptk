# Make our code better by defining a main function to only run
# if the file is run as a script.

import tkinter as tk


def main():
    """
    This code will run when the python script is run.
    """
    # create a 'root' window object to show a tkinter window
    # remember that python is case-sensitive!
    root = tk.Tk()

    # run the mainloop() method to have the window run and display
    root.mainloop()


# When our script runs the python interpreter will see the code below
# and automatically run the main() function we defined above. However, if the code
# is imported into another project, the main() function will not be run
# automatically, making it a better way to create our interface.
if __name__ == "__main__":
    main()
