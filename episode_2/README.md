# SnappyTk Episode 2 - Displaying a simple Tkinter GUI window

[Back to Episode List](../README.md)

[Watch Episode 2 on YouTube]()

In this episode we are going to see how to display a window using Tkinter. We are going to look at three different ways of writing this code and exam why we should write our code to be flexible and follow some good practices.

[Version 1 - Basic code](code/window_testing_v1.py)<br>
In the first version or our code, we can display a tkinter window with three lines of code:

```
import tkinter as tk
root = tk.Tk()
root.mainloop()
```

This code will work, but it only works when we run the file as a script. To make our code better and safer we should use some of the built-in functionality of Python.

### What does mainloop() do?
In tkinter, the mainloop() function tells python to start showing the interface and wait for input while the interface is running. If you put any code after this line it won't run until you close the window! Try it out for yourself.

See what happens if you put this line of code after the root.mainloop() line:

    ...
    root.mainloop()
    print("After the mainloop")

[Version 2 - Using a main() function](code/window_testing_v2.py)<br>
In the second version of the code we add in a main() function and then use the built-in functionality of Python to only run this function if we are using the file as a script. The code looks like this:

```
import tkinter as tk

def main():
    root = tk.Tk()
    root.mainloop()

if __name__ == "__main__:
    main()
```

We are now using the ```if __name__ == "__main__": ``` idiom to tell the python interpreter to only run the main() function if the file is running as a script. If this file is read as an import to another file the main() function won't run.

[Version 3 - Using a class to encapsulate the code](code/window_testing_v3.py)<br>
We can go one step further to make our code more flexible and reliable by using a class to hold our application code. This looks like below:

```
import tkinter as tk

class my_gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

if __name__ == "__main__:
    root = my_gui()
    root.mainloop()
```
Note that the **root** variable is now uses the **my_gui** class. This is our interface class that is a version (subclass) of the tk.Tk class that we have been using in the previous two versions of code.

We now have a file that can be run as a script or imported into another file. We could use the my_gui class in another project by adding a line of code like below:

    from window_testing import my_gui

We will talk about encapsulation with classes in our interfaces in later episodes.

## Final thoughts
Any of the three versions of code will work. Try them all out and get used to typing in the double underscores and brackets. Try changing the names of the variables and clicking all over the window to see what you can and can't do by default with a tkinter window.

Whatever you do, don't just read the code, write it yourself!

## Practice
* Use print() statements to print out messages to the terminal and see when they display in the console to test out how mainloop() works.

## Links to more information
[Python Documentation](https://docs.python.org/3/library/__main__.html)

[Real Python](https://realpython.com/python-main-function/)
