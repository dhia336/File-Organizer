import customtkinter as ctk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import shutil

from sqlalchemy import true
# Classes
class Frames():
    def __init__(self,window):
        self.win = window
        self.frames = [
            ctk.CTkFrame(self.win),
            ctk.CTkFrame(self.win),
            ctk.CTkFrame(self.win),
            ctk.CTkFrame(self.win),
            ctk.CTkFrame(self.win)
                        ]
        # extention
        self.extlab = ctk.CTkLabel(self.frames[0],text="Putting all the files with the same extention in a new folder")
        # file type frame
        self.typlab = ctk.CTkLabel(self.frames[1],text="Putting all the files with the same type in the a new folder")
        self.typconfbtn = ctk.CTkButton(self.frames[1],text="Configure",command=config_type)
        # name frame
        # date frame 
        # size frame 
        # default packing
        self.frames[0].pack(pady = 10,padx = 10)
        self.extlab.pack(pady=10, padx=10)
    def show (self,var):
        # hide all
        for f in self.frames:
            f.pack_forget()
        # show frame
        self.frames[var].pack(pady = 10,padx = 10)
        if var == 0:
            self.extlab.pack(pady = 10, padx = 10 )
        elif var == 1:
            self.typlab.pack(pady = 10, padx = 10 )
            self.typconfbtn.pack(pady = 10, padx = 10 )
# Functions
def showw():
    frames.show(radiovar.get())

def choose_folder():
    global cfolder
    cfolder = ctk.filedialog.askdirectory(title="select a file")
    if cfolder == "":
        cfolder = os.getcwd()
    folder_lab.configure(text = f"folder: {cfolder}")

def get_extention(ch):
    return ch[ch.rfind(".")+1:]

def organize_ext():
    files = os.listdir(cfolder)
    if files :
        for f in files:
            if f.find(".") != 0 and f.find(".") != -1:
                if not os.path.exists(cfolder+r"\\"+get_extention(f)):
                    os.makedirs(cfolder+r"\\"+get_extention(f))
                    shutil.move(cfolder+r"\\"+f, cfolder+r"\\"+get_extention(f))
                else:
                    shutil.move(cfolder+r"\\"+f, cfolder+r"\\"+get_extention(f))
            else:
                if not os.path.exists(cfolder+r"\\"+"Others"):
                    os.makedirs(cfolder+r"\\"+"Others")
                    shutil.move(cfolder+r"\\"+f, cfolder+r"\\"+"Others")
                else:
                    shutil.move(cfolder+r"\\"+f, cfolder+r"\\"+"Others")
    else:
        messagebox.showerror("ERROR","No files in this folder !!")

def organize_typ():
    files = os.listdir(cfolder)
    with open("Things\\Setting.txt","r") as f:
        s = f.read().split("\n")
    fold = []
    ext = []
    for i in s:
        fold.append(i.split(":")[0])
        ext.append(i.split(":")[1])
    if files:
        for f in files:
            i = 0
            if f.find(".") != 0 and f.find(".") != -1:
                while(i<len(files)and get_extention(f) not in ext[i]):
                    i=i+1
                if get_extention(f)  in ext[i]:
                    if not os.path.exists(cfolder+"/"+fold[i]):
                        os.makedirs(cfolder+"/"+fold[i])
                        print(cfolder+"/"+f)
                        print(cfolder+"/"+fold[i])
                        shutil.move(cfolder+"/"+f, cfolder+"/"+fold[i])
                    else:
                        shutil.move(cfolder+"/"+f, cfolder+"/"+fold[i])
    else:
        messagebox.showerror("ERROR","No files in this folder !!")
def ferme():
    top.destroy()
def config_type():
    global top
    top = ctk.CTkToplevel()
    #top.attributes("-topmost",True)
    top.transient(root)
    titlelabb = ctk.CTkLabel(top,text='CONFIGURATION',font=("",50))
    titlelabb.grid(pady = 20)
    with open("Things\\Setting.txt","r") as f:
        s = f.read().split("\n")
    fldrz=[]
    ext=[]
    widgs = []
    for i in range(len(s)):
        widgs.append(ctk.CTkFrame(top))
        widgs[i].grid(padx =20,pady = 5,sticky = "nw")
        f = s[i].split(":")
        fldrz.append(ctk.CTkButton(master=widgs[i],text=f[0],width=70))
        fldrz[i].pack(side = ctk.LEFT)
        ext.append([])
        for e in f[1].split(","):
            ext[i].append(ctk.CTkLabel(widgs[i],text=e,width=70))
            list(map(lambda a:a.pack(side = ctk.LEFT),ext[i]))
    bttfram = ctk.CTkFrame(top)
    bttfram.grid(pady = 10)
    closebtnn = ctk.CTkButton(bttfram,text="CLOSE",command=ferme)
    closebtnn.pack(padx = 5,pady = 10,side = ctk.LEFT)
    updbtnn = ctk.CTkButton(bttfram,text="REFRESH",command=typeorgup)
    updbtnn.pack(padx = 5,pady = 10,side = ctk.LEFT)
    edtbtnn = ctk.CTkButton(bttfram,text="EDIT",command=typeorgedt)
    edtbtnn.pack(padx = 5,pady = 10,side = ctk.LEFT)
def typeorgedt():
    os.startfile(r"THINGS\\Setting.txt")
def typeorgup():
    top.destroy()
    config_type()
def choose_method():
    match radiovar.get():
        case 0:
            organize_ext()
        case 1:
            organize_typ()
# window configs
root = ctk.CTk()
root.title("File Organizer")
# Global Variables
cfolder = os.getcwd()
radiovar = ctk.IntVar(value=0)
image = Image.open(r"Things\\Title.png")
photo_image = ImageTk.PhotoImage(image)
sort_frame = ctk.CTkFrame(root)
# title
title_lab = ctk.CTkLabel(root,text="",image=photo_image)
title_lab.pack(padx = 20,pady = 25)
# choose folder
folderframe = ctk.CTkFrame(root)
folderbtn = ctk.CTkButton(folderframe,text=" Working Folder ",command=choose_folder)
folderbtn.pack(side = ctk.LEFT,padx = 10,pady = 10)
folder_lab = ctk.CTkLabel(folderframe,text=f" folder: {cfolder}",font=("",15))
folder_lab.pack(side = ctk.RIGHT ,padx = 10)
folderframe.pack(pady = 5,padx = 20)
# sorting frame 
#sort_frame = ctk.CTkFrame(root)
sort_frame.pack(pady = 10,padx = 25)
# radio buttons (sort by [extention ,file type ,name ,date ,size....])
srt_lab = ctk.CTkLabel(sort_frame,text="Sort By : ",font=("",30))
srt_lab.pack(padx = 10,pady = 10)
radioframe = ctk.CTkFrame(sort_frame)
radioframe.pack(padx = 20,pady = 10)
radio1 = ctk.CTkRadioButton(radioframe, text="Extention", variable= radiovar, value=0,command=showw)
radio1.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio1.select()
radio2 = ctk.CTkRadioButton(radioframe, text="Type",variable= radiovar, value=1,command=showw)
radio2.pack(side = ctk.LEFT , padx = 10,pady = 10)
'''
radio3 = ctk.CTkRadioButton(radioframe, text="Name",variable= radiovar, value=2,state='disabled')
radio3.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio4 = ctk.CTkRadioButton(radioframe, text="Date",variable= radiovar, value=3,state='disabled')
radio4.pack(side = ctk.LEFT , padx = 10,pady = 10)
radio5 = ctk.CTkRadioButton(radioframe, text="Size",variable= radiovar, value=4,state='disabled')
radio5.pack(side = ctk.LEFT , padx = 10,pady = 10)
'''
# secondary frames frame
frm_frame = ctk.CTkFrame(sort_frame)
frm_frame.pack(pady = 5, padx = 5)
frames = Frames(frm_frame)
# run button
runbutton = ctk.CTkButton(sort_frame,text=" ORGANIZE ",compound="right",command=choose_method)
runbutton.pack(pady = 10,padx = 20,side = ctk.BOTTOM)

# execute programe
if __name__=="__main__":
    root.mainloop()