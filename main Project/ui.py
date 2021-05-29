from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

import subprocess

def face():
    subprocess.call(["python", "E:\\Users\\nimali keny\\Desktop\\BE Project Material\\main Project\\face-try.py"])
    
def blink():
    subprocess.call(["python", "E:\\Users\\nimali keny\\Desktop\\BE Project Material\\main Project\\blinkDetect.py"])
    
def lane():
    subprocess.call(["python", "E:\\Users\\nimali keny\\Desktop\\BE Project Material\\main Project\\lanedetection.py"])
    
root = Tk() 
root.geometry('600x300') 
root.title('Driver Safety Detection')
canvas=Canvas(root, width=600, height=300)
image=ImageTk.PhotoImage(Image.open("E:\\Users\\nimali keny\\Desktop\\BE Project Material\\car.jpg"))
canvas.pack()
canvas.create_image(0,0,anchor=NW, image=image)


style = Style() 
style.configure('TButton', font =('calibri', 20, 'bold'), borderwidth = '2') 


# button 1 
btn1 = Button(root, text = 'Face Detection', command = face) 
btn1_canvas = canvas.create_window( 80, 30, anchor = "nw",window = btn1)

# button 2 
btn2 = Button(root, text = 'Blink Detection', command = blink) 
btn2_canvas = canvas.create_window( 350, 30, anchor = "nw", window = btn2)

# button 2 
btn3 = Button(root, text = 'Lane Detection', command = lane) 
btn3_canvas = canvas.create_window( 230, 110, anchor = "nw", window = btn3)

#button 4
btn4 = Button(root, text = 'Quit', command = root.destroy) 
btn4_canvas = canvas.create_window( 235, 200, anchor = "nw", window = btn4)

    
root.mainloop() 
