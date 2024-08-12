import customtkinter as ctk
import os
from PIL import Image, ImageTk
# Functions
def frame_to_run(root):
    pass
# window configs
root = ctk.CTk()
root.title("File Organizer")
# Global Variables
cfolder = os.getcwd()
radiovar = ctk.IntVar(value=0)
image = Image.open("Title.bin")
photo_image = ImageTk.PhotoImage(image)
# title
title_lab = ctk.CTkLabel(root,text="",image=photo_image)
title_lab.pack(padx = 20,pady = 25)
# choose folder
folderframe = ctk.CTkFrame(root)
folderbtn = ctk.CTkButton(folderframe,text=" Choose Folder ")
folderbtn.pack(side = ctk.LEFT,padx = 10,pady = 10)
folder_lab = ctk.CTkLabel(folderframe,text=f" folder: {cfolder}",font=("",15))
folder_lab.pack(side = ctk.RIGHT ,padx = 10)
folderframe.pack(pady = 5,padx = 20)
# sorting frame 
sort_frame = ctk.CTkFrame(root)
sort_frame.pack(pady = 10,padx = 25)
# radio buttons (sort by [extention ,file type ,name ,date ,size....])
srt_lab = ctk.CTkLabel(sort_frame,text="Sort By : ",font=("",30))
srt_lab.pack(padx = 10,pady = 10)
radioframe = ctk.CTkFrame(sort_frame)
radioframe.pack(padx = 20,pady = 10)
radio1 = ctk.CTkRadioButton(radioframe, text="Extention", variable= radiovar, value=1)
radio1.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio2 = ctk.CTkRadioButton(radioframe, text="Type",variable= radiovar, value=2)
radio2.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio3 = ctk.CTkRadioButton(radioframe, text="Name",variable= radiovar, value=3)
radio3.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio4 = ctk.CTkRadioButton(radioframe, text="Date",variable= radiovar, value=4)
radio4.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio5 = ctk.CTkRadioButton(radioframe, text="Size",variable= radiovar, value=5)
radio5.pack(side = ctk.LEFT , padx = 10,pady = 10)
# choose frame
frame_to_run(sort_frame)
# run button
runbutton = ctk.CTkButton(sort_frame,text=" ORGANIZE ",compound="right",state="disabled")
runbutton.pack(pady = 10,padx = 20)

# execute programe
if __name__=="__main__":
    root.mainloop()