# SnappyTk Episode 3 - Configuring Tkinter windows

[Back to Episode List](../README.md)

[Watch Episode 3 on YouTube](https://youtu.be/tPDwpXvEd3A)

Let's explore what we can do with a simple tkinter window to configure it. When you are first thinking about building your new software, spare a little time to decide how your application is going to work for your users and what you can do to make it easier for them and a nicer interface in general.

**NOTE:** We are using a class in our code to show the window. Due to this we use the keyword *self* to refer to the 'instance' of our window. If you weren't using a class you could replace all the 'self' code with the variable name that is storing your window object, like *root* for example.

### Set the title for the window
This will show the text in the title bar of the window

    self.title("GUI with Tkinter")

### Set the size for the window in pixels
You can specify how wide and high your window will be in pixels

     self.geometry("300x250")

### Set the distance from the screen edges the window will display
You can also specify how far from the screen edges the window will display. You can use both **+** and **-** here with the **+** being from the left/top screen edge to the left/top edge of the window, and **-** being from the right/bottom screen edge to the right/bottom edge of the window. 

    # 600 pixels from the left and 300 pixels from the top
    self.geometry("+600+300") 

Here is how you can display a window in each corner of the screen:

    self.geometry("+0+0") # top left
    self.geometry("+0-0") # bottom left
    self.geometry("-0+0") # top right
    self.geometry("-0-0") # bottom right

You can also combine the window sizing and location in the same command

     self.geometry("300x250+600+300")

### Set the min and max sizes the window can be resized to
If the window is resizable, these commands will control how big or small it can get. They also set the size when the window is maximized.

     self.minsize(width=200, height=300)
     self.maxsize(width=500, height=600)

### Set whether the window can be resized or not
You can stop the window being resized by width, height or both

     self.resizable(0, 0) # window can't be resized

### Set the icon image for the window
If you want to display an icon in the title bar you can

     self.iconbitmap("episode_3/pics/snappytk.ico")

### Check what window attributes your OS supports
Depending on your OS, there are other attributes you can set. To see what attributes you have available on your computer, you can print them out easily

     print(self.attributes())

### Set the window to be a 'toolwindow'
A tool window limits some of the things you can do with your window. It might be good for a dialog box, for example. Try it out

     self.attributes("-toolwindow", 1)

### Set the window to take up the whole screen
If you want your window to take up the entire screen, you can do that. It won't work if you window's maxsize is set though!

     self.attributes("-fullscreen", 1)

### Disable the window
You can disable a window so that it is visible but you can't interact with it

     self.attributes("-disabled", 1)

### Move the window above all others
If you have multiple windows you can move one above all the others

     self.attributes("-topmost", 1)

### Adjust the window's transparency level
You can make windows transparent, including the title bar. 0 is fully transparent and 1 is fully opaque

     self.attributes("-alpha", 0.1)

### Set a colour to be transparent for an interesting window
If you want to show the title bar but make the rest of the window transparent you can. Set the transparentcolor attribute to the same colour as the window's background colour

     self.config(bg="green")
     self.attributes("-transparentcolor", "green")

### Tell the window manager to ignore the window
If you want a window that only shows the contents and nothing else, you can do that too

     self.overrideredirect(1)

## Practice ideas:
- try out all the different code above on your own window
- try moving a window around the screen to various locations
- see what will happen if you set the alpha to 0
- create your own .ico file for your app and have it display (if on windows)