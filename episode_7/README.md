# SnappyTk Episode 7 - Labels with images

[Back to Episode List](../README.md)

[Watch Episode 7 on YouTube](https://youtu.be/tLKec9nUywQ)

[Get the code for Episode 7 here](code/label_images.py)

In this episode we are going to continue working with labels. However, now we are going to also display images along with text using labels in Tkinter. The **Label** widget allows you to display text, an image, or even both at the same time. See below for how to work with images in labels and go to the link above to get the code.

## Using a tk.PhotoImage
Before you can have a labels show an image you need to create an image object. By default tkinter has a **PhotoImage** object that will do this for you. You can't just load an image into a label using the path to the image. You first create the *photoimage* and then tell the label to use this as the image to display. Here is an example of this:

    self.pic = tk.PhotoImage(file="episode_7/pics/dog.png")
    self.dog = ttk.Label(self.container_frame, text="dog", image=self.pic, compound="bottom")
    self.dog.pack(side='left')

The first line creates the photoimage object and then in the second line we use the new image object in the label with **image=self.pic**.

## Showing text and images together
By default a label with show an image if it is set, or it will show the text if there is no image. We can change this though so the text and image show together. We do this using the **compound** argument in the label.

    self.dog = ttk.Label(self.container_frame, text="dog", image=self.pic, compound="bottom")

The *compound="bottom"* part of the line above tells the label to display the image below the text.

## Subsampling a PhotoImage to change its size
If you want to change the size of the image you need to do this before you use it with the label. If you are using a tk.PhotoImage object you can scale your image down in size by using the **subsample()** method like below:

        self.pic2 = tk.PhotoImage(file="episode_7/pics/bird.png")
        self.pic2 = self.pic2.subsample(2, 2)
        self.bird = ttk.Label(self.container_frame, text="bird", image=self.pic2, compound="top")
        self.bird.pack(side='left')

The second line above scales the image to half the size by looking at every second pixel. This works, but as you scale the image even more it will start to lose clarity and look less like the original. It is good for quick fix of an image, but may not look great with some images.

## Using the Python Imaging Library to resize images
If you want to use .jpg or .jpeg images, or you want to make cleaner resizes of your images, you can use the Python Imaging Library (PIL).

Before you can use it you will need to install the package onto your system or into your virtual environment. You can do this by running pip in the terminal:

- Windows: *pip install pillow*
- Mac/Linux: *pip3 install pillow*

**NOTE:** pillow is the name of the package to install.

Once it is installed you can then import it into your file with:

    from PIL import Image, ImageTk

We import both the *Image* and *ImageTk* classes from PIL to use and work with images.

## Resizing images with PIL
We can open an image with PIL, resize it, convert it to an image that a tkinter label can use, and then have the label display it. Here is an example of this:

      self.pic3 = Image.open("episode_7/pics/fish.png")
      self.pic3 = ImageTk.PhotoImage(self.pic3.resize((50, 50)))
      self.fish = ttk.Label(self.container_frame, text="fish", image=self.pic3, compound="top")
      self.fish.pack(side='left')

The first two lines are different. In the first line we open the image using the *Image* module from PIL. This allows us to use the **resize()** method in the second line to change the image's size. Finally in the second line we also have to use the *ImageTk* object to wrap the resized image so that we can use the object in the tkinter label.

## Keeping the image proportions using thumbnail()
If you want to resize the image but keep the proportions better, instead of resize() we can use the **thumbnail()** method on the image like below:

        self.pic4 = Image.open("episode_7/pics/cat.png")
        self.pic4.thumbnail((50, 50))
        self.pic4 = ImageTk.PhotoImage(self.pic4)
        self.cat = ttk.Label(self.container_frame, text="cat", image=self.pic4, compound="top")
        self.cat.pack(side='left')

You will notice we had to add a line of code because, unlike resize(), the thumbnail() method of an Image object just modifies the current image, it doesn't return a new image object. So we have to create the ImageTk.PhotoImage object now on the third line above, we can't do it all on the one line now.

## Practice
- Try to use labels to display images on your own computer.
- Test out what kinds of picture files work and what ones don't.
- Install the pillow package and use PIL to work with images.
- Try out some of the other methods an *Image* object can do, like rotate() and see if you can do something interesting with an image before showing it in a label.