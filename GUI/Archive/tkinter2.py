import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Yay")
root.iconbitmap("GUI\\window_icon.ico")

#Adjust window size
root.geometry("740x620")

#Specify Grid
#tk.Grid.rowconfigure(root,0,weight=1)
#tk.Grid.rowconfigure(root,1,weight=1)
#tk.Grid.columnconfigure(root,0,weight=1)

#Images
# my_img = ImageTk.PhotoImage(Image.open("GUI\\background_diplomacy.jpeg"))
# my_label = tk.Label(root,image=my_img)
# my_label.place(x=0,y=0,relwidth=1, relheight=1)
# my_label.pack()
# my_label.grid(row=0,column=0,sticky="")

#Create a canvas
bg_image = ImageTk.PhotoImage(Image.open("GUI\\bg_small.jpg"))
cHeight = bg_image.height()
cWidth = bg_image.width()
canvas = tk.Canvas(root, width=cWidth,height=cHeight)
canvas.grid(row=0,column=0)


#Add Image inside canvas

canvas.create_image(0,0,image=bg_image,anchor="nw")


root.mainloop()