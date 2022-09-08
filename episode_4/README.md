# SnappyTk Episode 4 - What's a layout manager?

[Back to Episode List](../README.md)

[Watch Episode 4 on YouTube](https://youtu.be/SeXI_08f9Q0)

[Get the code for Episode 4 here](code/)

Now that we have seen how to display a window and configure it with some options for our application, we are going to want to start showing our interface. Tkinter has some terminology and some rules that you need to understand to get your interfaces looking the way you want them.

One of the things that many people new to Tkinter struggle with is understanding what a **Layout Manager** is. Let's take a look at how you can show some buttons in your window and what these mysterious layout managers do.

**NOTE:** we are using a simple class to show our window with a size defined. See if you can write this from memory. If you can't check out the code for this episode to help remind you how.

## Adding a button
The first thing we are going to do is add a button to our window with the code below:

    self.btnClickMe = tk.Button(self, text="Click Me")

This button won't do anything when you click it, it is just for show for now.

If we run our code after adding the button, you will notice that the button is missing!?!? It isn't showing. Why not?

## Layout Managers
The reason the button isn't showing is that Tkinter uses a system called a *layout manager* to determine what widget will show and where. 

Think of the layout manager as like a coach on a sports team. They work out who (which widgets) go where on the field (our window).

Tkinter has a number of different layout managers that can control the display of widgets in your applications. There are actually five different ones, but two are special, as they are widgets themselves.Let's take a look at the three main ones:

- The place() layout manager
- The pack() layout manager
- The grid() layout manager

We will go through each one of these to see how they work. We won't go into too much detail here though. We will leave that for when we look at each one in more detail individually.

## The place() layout manager
This is an easy one to use. You tell it where on your window you want the widget to go, the x & y pixel coordinates, and it will put the widget there. Let's try it on our window with this code:

    self.btnClickMe.place(x=100, y=100)

#### Pro's and Con's of place()
Using the place layout manager allows you to specify exactly where the widget will be shown. However, it doesn't allow for moving the widget if the window resizes, making the interface stagnant and not responsive to a user who wants to change the size of the window.

Try moving the button around the window with different x and y values, and try adding another button and showing them both at the same time but in different locations. You will find it works well and is easy to use, but might not be what you want if you need a more flexible interface that can change with your window and user's requirements.

## The pack() layout manager
Packing widgets is just like it sounds. You 'stuff' them into the container and they show in the order you pack them in your code. They try to take up only a minimum amount of space they need. Let's pack two buttons to see how they will display by default:

      self.btnClickMe = tk.Button(self, text="Click Me")
      self.btnClickMe.pack()

      self.btnClickMe2 = tk.Button(self, text="Click Me2")
      self.btnClickMe2.pack()

You will notice now they appear in the middle of the window, and you didn't even specify any arguments to the pack command.

There are a lot of options you can use when you 'pack' widgets. Try changing the second button's pack command to this one and see what it does:

      self.btnClickMe2.pack(fill=tk.BOTH, expand=1)

#### Pro's and Con's of pack()
Pack makes it hard to place *exactly* where you want each widget, but if you don't need that exactness pack() can be a quick and easy way to get widgets displaying.

Unlike the place() command, widgets may change their locations when you change the window size. This could be a good thing or not what you want. Make sure you test out what happens when you resize the window.

## The grid() layout manager
This layout manager is one for people who like logic and are familiar with working with grids in things like excel. You specify your widgets display in a row and column location, with each widget taking up one *cell* of the grid.

If you try to put two widgets in the same grid location, you will only see the last one on top! Here is an example of our two buttons showing side-by-side horizontally:

      self.btnClickMe = tk.Button(self, text="Click Me")
      self.btnClickMe.grid(row=0, column=0)

      self.btnClickMe2 = tk.Button(self, text="Click Me2")
      self.btnClickMe2.grid(row=0, column=1)

**NOTE:** with the grid() manager, you can't use it to create spacing in your widget layouts most of the time by leaving cells, columns or rows empty. For example if you put one button in row=1 and another in row=3, you might think that there would be some space between them.

There won't be. If a row or column has not widgets in it to give it a height or width, it won't display at all.

Try this out for yourself.

#### Pro's and Con's with grid()
Grid is easy to use and can allow you to create all kinds of complex layouts. However, this means that it can take some thinking to design the layout just how you want it to display and then set it up with your widgets. The grid might also need some tweaking to make it work how you want it to when the window is re-sized, but we will go over this in more detail later.

## Can you use multiple layout managers?
No (and yes)! You can only use one layout manager per container. The application is one container, so you can only use one layout manager at a time. 

If you want to use more than one you just need to add more containers like a tk.Frame or tk.LabelFrame widget. Each one of these can have its own layout manager that is the same, or different, from the application's layout manager.

# Practice
Now it is time to try out the different managers yourself. 
- Can you create a grid of 3x3 buttons using grid()?
- Can you place a button in the center of the window using place()?
- Can you pack() two buttons so one is on the left and other is on the right side of the window?