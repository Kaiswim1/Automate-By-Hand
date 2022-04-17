import bluetooth
import socket
from tkinter import*
import tkinter as tk
import serial
import pickle
import keyboard

sc=0; stp=0
lbl=None
dictionary={}
x=0
i=0
k=0 #KeyStroke disabler enables only when 0
root=None
loading=None
app=None
nameChange=False
button_dict = {}
 
listOfBT = []
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

def rightPress():
    global k
    log()
    if k == 0:
        print('r')
        s.send(b'r')
        k=k+1


def leftPress():
    global k
    log()
    if k == 0:
        print('r')
        s.send(b'l')
        k=k+1

def upPress():
    global k
    log()
    if k == 0:
        print('u')
        s.send(b'u')
        k=k+1

def downPress():
    global k
    log()
    if k == 0:
        print('u')
        s.send(b'd')
        k=k+1


def stopKey():
    global k
    print('s')
    log()
    s.send(b's')
    k=0

def rled():
    global sc
    global stp
    log()
    if btn.config('text')[-1] == 'OFF RED':
        btn.config(text='ON RED')
        print(sc)
        s.send(b's') #stop
    else:
        btn.config(text='OFF RED')
        print(sc)
        s.send(b'f') #forward

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
        if x==0: 
            lbl.after(30,start)

    f=list(dictionary)
    try:
        #for i in f:
        if lbl["text"] == str(f[i]) and len(dictionary)>0:
            print(dictionary.get(f[i]))
            if dictionary.get(f[i]) == "ON RED":
               #arduinoData.write(b'a')
                s.send(b's')
            if dictionary.get(f[i]) == "OFF RED":
               #arduinoData.write(b'b')
                s.send(b'f')
            i=i+1
    except IndexError as e:{
    }
        

    #print(dictionary)


#When we stop, it saves the dictionary to a pickle,
#TODO: save it to a text file
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
        dictionary[sc]="ON RED"
    else:
        dictionary[sc]="OFF RED"
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
    start()
    f=list(dictionary)
    print(str(f[0]))
    print(len(dictionary))
    print(len(list(dictionary)))
    if lbl["text"] == str(f[0]):
        print("Hello world")


def loadingScreen():
    global loading
    loading = Tk()
    img = PhotoImage(file='C:/Users/kaisw/Downloads/LoadingPageABH.png')
    Label(loading,image=img).pack()
    loading.overrideredirect(True)
    loading.geometry("578x220+435+285")
    loading.update()

def scan():
    global loading
    print("Scanning for bluetooth devices:")
    loadingScreen()
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)
    print(number_of_devices,"devices found")
    i=0
    for addr, name, device_class in devices:
        listOfBT.append(devices[i][0])
        print(devices[i][0])
        i=i+1
    print(listOfBT)
    loading.destroy()
    scanUI(listOfBT)
    return
    

def openControllerUI():
    global btn
    global app
    app.destroy()
    root=Tk()
    root.title("stopwatch")
    root.geometry("210x410")
    root.resizable(False,False)
    root.configure(bg="black")
    button1=Button(root,text="Record", command=start)
    button2=Button(root,text="Stop",command=stop)
    button3=Button(root,text="Load",command=load)
    btn=tk.Button(root,text="ON RED", font=('arial',10,'bold'), borderwidth='8', height="4", width="6", command=rled)
    
    keyboard.on_press_key("right", lambda _:rightPress())   
    keyboard.on_release_key("right", lambda _:stopKey())

    keyboard.on_press_key("up", lambda _:upPress())   
    keyboard.on_release_key("up", lambda _:stopKey())

    keyboard.on_press_key("left", lambda _:leftPress())   
    keyboard.on_release_key("left", lambda _:stopKey())

    keyboard.on_press_key("down", lambda _:downPress())   
    keyboard.on_release_key("down", lambda _:stopKey())

    button4=Button(root,text="Reset",command=reset)
    button1.place(x=10,y=10)
    button2.place(x=100,y=10)
    button3.place(x=10,y=40)
    btn.place(x=10, y=180)
    button4.place(x=100, y=40)
    root.mainloop()



def onRightClick(event):
    global name
    global app
    name = tk.StringVar()
    print(button_dict[0].cget('text'))
    rc = Tk()
    rc.title("Rename")
    rc.geometry("180x160")
    rc.resizable(True,True)
    rc.configure(bg="#E7E7E7")
    f = Frame(rc,width=250,height=250, bg="#2C2C2C")
    f.grid(row=0,column=0,sticky="NW")
    f.grid_propagate(0)
    f.update()
    l = Label(f,text="Rename to",bg='#DD8630',fg='white', font=('arial',18,'bold'))
    l.place(x=95, y=15, width=200, height=35, anchor="center")
    rename = tk.Entry(f, width = 15, textvariable = name)

    def okay():
        name = rename.get()
        print(name)
        app.update()
        
    print()

    
    rename.place(x=90, y=48, width=168, height=20, anchor="center")
    ok=tk.Button(rc,text="OK", font=('arial',10,'bold'), borderwidth='0', height="2", width="6", command=okay)
    ok.place(x=30+4, y=80)
    cancel=tk.Button(rc,text="CANCEL", font=('arial',10,'bold'), borderwidth='0', height="2", width="6", command=rc.destroy)
    cancel.place(x=90+4, y=80)
    rc.mainloop()
    
    


def scanUI(x):
    global app
    global button_dict
    app = Tk()
    app.resizable(False, True)
    
    f = Frame(app,width=250,height=250, bg="black")
    f.grid(row=0,column=0,sticky="NW")
    f.grid_propagate(0)
    f.update()
    by=66
    
    l = Label(f,text="Available Bluetooth",bg='#27BFB2',fg='white', font=('arial',18,'bold'))
    print("ege: "+str(listOfBT))
    l.place(x=125, y=25, width=500, height=50, anchor="center") 

    def text_updation(language):
        print(language)
        s.connect((language, 1))
        print('connected')
        #button
        openControllerUI()
        
        
    
    for lang in x:
    
    # pass each button's text to a function
        def action(x = lang): 
            return text_updation(x)
        
    # create the buttons
        if nameChange == False:
            button_dict[lang] = Button(app, text = lang, command = action, font=('arial',10,'bold'))
            button_dict[lang].place(x=58, y=by, width=130, height=20)
            button_dict[lang].bind('<Button-3>',  onRightClick) 
            by = by+35


    app.mainloop()

        
    
scan()
