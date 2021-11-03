import bluetooth
import socket
from tkinter import*
import tkinter as tk
import serial
import pickle

sc=0; stp=0
lbl=None
dictionary={}
x=0
i=0
root=None
 
listOfBT = []
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

def rled():
    global stp
    log()
    if btn.config('text')[-1] == 'OFF RED':
        btn.config(text='ON RED')
        s.send(b'd')
    else:
        btn.config(text='OFF RED')
        s.send(b'a')

def start():
    global sc
    global root
    global lbl
    global stp
    global x
    global i
    global dictionary
    sc=sc+1
    lbl=Label(root, text='%i'%(sc), font=('arial',20,'bold'))
    if(stp==0):
        #print(str(sc))
        if x==0:
            lbl.after(30,start)
        #lbl.place(x=95,y=90)

    f=list(dictionary)
    try:
        #for i in f:
        if lbl["text"] == str(f[i]) and len(dictionary)>0:
            print(dictionary.get(f[i]))
            if dictionary.get(f[i]) == "ON RED":
               arduinoData.write(b'a')
            if dictionary.get(f[i]) == "OFF RED":
               arduinoData.write(b'b') 
            i=i+1
    except IndexError as e:{
    }
        

    #print(dictionary)


def stop():
    global sc
    global stp
    global room
    stp=1
    with open('dict1.pickle', 'wb') as f:
        pickle.dump(dictionary, f)

def pause():
    return

def log():
    global sc
    if btn.config('text')[-1] == 'OFF RED':
        dictionary[sc]="OFF RED"
    else:
        dictionary[sc]="ON RED"
    return

def reset():
    global root
    global lbl
    global stp
    global sc
    lbl.config(background="black")
    lbl=None
    sc=0
    x=0
    stp=0
    #lbl.setHidden(True)
    lbl=Label(root, text='0')
    #root.destroy()
    #root = create_frame(root)
    print("~~~~~~~~~~reset~~~~~~~~~~~~")
    #frame = create_different_frame(master)
    #root.pack()



def load():
    reset()
    global sc
    global dictionary
    global stp
    #button3["state"] = DISABLED
    stp=0
    f=list(dictionary)
    print(str(f[0]))
    print(len(dictionary))
    print(len(list(dictionary)))
    if lbl["text"] == str(f[0]):
        print("Hello world")

def scan():
    print("Scanning for bluetooth devices:")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)
    print(number_of_devices,"devices found")
    i=0
    for addr, name, device_class in devices:
        listOfBT.append(devices[i][0])
        print(devices[i][0])
        i=i+1
    print(listOfBT)
    scanUI(listOfBT)
    return

def openControllerUI():
    global btn
    root=Tk()
    root.title("stopwatch")
    root.geometry("210x410")
    root.resizable(False,False)
    root.configure(bg="black")
    button1=Button(root,text="Record", command=start)
    button2=Button(root,text="Stop",command=stop)
    button3=Button(root,text="Load",command=load)
    btn=tk.Button(root,text="ON RED", font=('arial',10,'bold'), borderwidth='8', height="4", width="6", command=rled)
    button4=Button(root,text="Reset",command=reset)
    button1.place(x=10,y=10)
    button2.place(x=100,y=10)
    button3.place(x=10,y=40)
    btn.place(x=10, y=180)
    button4.place(x=100, y=40)
    root.mainloop()


def scanUI(x):
    app = Tk()
    app.resizable(False, False)
    
    f = Frame(app,width=250,height=250, bg="black")
    f.grid(row=0,column=0,sticky="NW")
    f.grid_propagate(0)
    f.update()
    button_dict = {}
    by=66
    
    l = Label(f,text="Available Bluetooth",bg='#27BFB2',fg='white', font=('arial',18,'bold'))
    print("ege: "+str(listOfBT))
    l.place(x=125, y=25, width=500, height=50, anchor="center") 

    def text_updation(language):
        print(language)
        s.connect((language, 1))
        print('connected')
        app.destroy()
        openControllerUI()
        
    
    for lang in x:
    
    # pass each button's text to a function
        def action(x = lang): 
            return text_updation(x)
        
    # create the buttons 
        button_dict[lang] = Button(app, text = lang, command = action, font=('arial',10,'bold'))
        button_dict[lang].place(x=58, y=by, width=130, height=20)
        by = by+35
    
scan()











        



