### Imports ####
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

### Setup tkinter root window ####
root = tk.Tk()
root.title("Diplomacy GUI")
root.geometry("1400x800")
root.configure(background="black")




class Gameframe(tk.Frame):
    def __init__(self, master): #, *pargs?
        tk.Frame.__init__(self, master) #, *pargs?

        #Open BG image & create a copy for scaling
        self.image = Image.open("GUI\\background_diplomacy.jpeg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)
        #Create a Lable widget with background image
        self.background = tk.Label(self, image=self.background_image)
        self.background.pack(fill=tk.BOTH, expand=tk.YES)
        self.background.bind('<Configure>', self.resize_image) ###TODO: Figure this out?

        #### Testing another pack ####
        #self.icon_image = ImageTk.PhotoImage(Image.open("GUI\\window_icon.png"))
        #self.icon = tk.Label(self, image=self.icon_image)
        #self.icon.pack()

    def resize_image(self,event):
        # Choose whether to scale image width or height to fill window, scale other dimension accordingly
        bg_ratio = 1.19 # BG image's ratio of width : height
        if (event.width / event.height) > bg_ratio:
            new_height = event.height
            new_width = int(bg_ratio * new_height)
        else:
            new_width = event.width
            new_height = int(new_width / bg_ratio)

        #Create a new self.image by resizing the copy image; configure the background
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    #TODO?
    def current_image_width(self):
        pass

    def draw_unit_icons(self):
        pass



g = Gameframe(root)
g.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)

#icon_image = ImageTk.PhotoImage(Image.open("GUI\\window_icon.png"))
#icon = tk.Label(image=icon_image)
#icon.pack()

root.mainloop()


##### Testing #####

# print(root.configure().keys())