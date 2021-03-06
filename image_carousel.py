# from itertools import cycle
# try:
#     # Python2
#     import Tkinter as tk
# except ImportError:
#     # Python3
#     import tkinter as tk
# class App(tk.Tk):
#     '''Tk window/label adjusts to size of image'''
#     def __init__(self, image_files, x, y, delay):
#         # the root will be self
#         tk.Tk.__init__(self)
#         # set x, y position only
#         self.geometry('+{}+{}'.format(x, y))
#         self.delay = delay
#         # allows repeat cycling through the pictures
#         # store as (img_object, img_name) tuple
#         self.pictures = cycle((tk.PhotoImage(file=image), image)
#                               for image in image_files)
#         self.picture_display = tk.Label(self)
#         self.picture_display.pack()
#     def show_slides(self):
#         '''cycle through the images and show them'''
#         # next works with Python26 or higher
#         img_object, img_name = next(self.pictures)
#         self.picture_display.config(image=img_object)
#         # shows the image filename, but could be expanded
#         # to show an associated description of the image
#         self.title(img_name)
#         self.after(self.delay, self.show_slides)
#     def run(self):
#         self.mainloop()
# # set milliseconds time between slides
# delay = 500
# # get a series of gif images you have in the working folder
# # or use full path, or set directory to where the images are
# image_files = [
# 'img1.png',
# 'img2.png',
# 'img3.png',
# 'img4.png',
# ]
# # upper left corner coordinates of app window
# x = 100
# y = 50
# app = App(image_files, x, y, delay)
# app.show_slides()
# app.run()

# ===================================================

# import Tkinter as tk
# from itertools import cycle

# foreign library, need to installed
# from ImageTk import PhotoImage
#
# images = ["first1.jpg", "first2.jpg", "first3.jpg", "first4.jpg"]
# photos = cycle(PhotoImage(file=image) for image in images)
#
# def slideShow():
#   img = next(photos)
#   displayCanvas.config(image=img)
#   root.after(50, slideShow) # 0.05 seconds
#
# root = tk.Tk()
# root.overrideredirect(True)
# width = root.winfo_screenwidth()
# height = root.winfo_screenwidth()
# root.geometry('%dx%d' % (640, 480))
# displayCanvas = tk.Label(root)
# displayCanvas.pack()
# root.after(10, lambda: slideShow())
# root.mainloop()

# ===================================================

import sys
from tkinter import * #or Tkinter if you're on Python2.7

def button1():
    novi = Toplevel()
    canvas = Canvas(novi, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'img1.png')
                                #image not visual
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1


mGui = Tk()
button1 = Button(mGui,text ='Next',command = button1, height=5, width=20).pack()

mGui.mainloop()