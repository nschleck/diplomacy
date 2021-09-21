import tkinter
# from tkinter import * #Don't use wildcard import!

# / import diplomacy turnstate
windowTitle = "Diplomacy -- " + "Spring 1902"


#Create GUI window
root = tkinter.Tk()


#######################  LABELS ################################
#Create a label widget
#myLabel1 = tkinter.Label(root, text=windowTitle)
#Shove it onto screen
#myLabel1.grid(row=0, column=0)


######################### BUTTONS ###################################
#def myClick():
    # myLabel = tkinter.Label(root, text = "clicked!")
    # myLabel.pack()

#Create a button widget
#myButton = tkinter.Button(root, text="Click Me!", command=myClick)
# myButton.pack()

#Exit button
#button_quit = tk.Button(root, text = "Exit Program", command = root.quit)
#button_quit.grid(row=1,column=0,sticky="")

########################### INPUT ####################################
e = tkinter.Entry(root, borderwidth=15)
e.pack()



#Create Main Event Loop
root.mainloop()
