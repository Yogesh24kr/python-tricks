# from cx_Freeze import setup, Executable 
# excludes = []
# packages = []
# base = none
# if sys.platform == "win32":
#     base = "win32GUI"
    
# setup(name = "GeeksforGeeks" , 
#       version = "0.1" , 
#       description = "" , 
#       executables = [Executable("reandurllib.py")]) 

##############################################################################################################################
def musicurl():
        dd = filedialog.askopenfilename(title="Audio File")
        audiotrack.set(dd);
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    root.mute.grid();
    progressbarmusiclable.grid();
    progressbarlable.grid();
    mixer.music.play()
    mixer.music.set_volume(0.4)
    progressbarvollable.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    status.configure(text="Playing...")
    song = MP3(ad);
    totalsonglen = int(song.info.length)
    progressbarmusic['maximum'] = totalsonglen
    progressbarmusicendtime.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglen))))
    def progressmusictick():
        currentlen = mixer.music.get_pos()//1000
        progressbarmusic['value'] = currentlen
        progressbarmusicstarttime.configure(text='{}'.format(str(datetime.timedelta(seconds=currentlen))))
        progressbarmusic.after(2,progressmusictick)
    progressmusictick() 
    
def volumup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.05)
    progressbarvollable.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarvol['value'] = mixer.music.get_volume() * 100
    
def stopmusic():
    mixer.music.stop();
    status.configure(text="Stop...")
def volmdown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.05)
    progressbarvollable.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    progressbarvol['value'] = mixer.music.get_volume() * 100
    
def pausemusic():
    mixer.music.pause()
    root.resume.grid();
    root.pause.grid_remove()
    status.configure(text="Pause...")
def songresume():
    root.resume.grid_remove()
    root.pause.grid();
    mixer.music.unpause()
    status.configure(text="Playong...")
def mute():
    global currentvol
    root.mute.grid_remove()
    root.unmute.grid();
    currentvol = mixer.music.get_volume();
    mixer.music.set_volume(0)
    status.configure(text="Mute...")
def unmute():
    root.unmute.grid_remove()
    root.mute.grid();
    mixer.music.set_volume(currentvol)
def createwidth():
    global status,progressbarvollable,progressbarvol,progressbarlable,progressbarmusiclable,progressbarmusicstarttime,progressbarmusicendtime,progressbarmusic
    ####################################################################################################### Lables
    tracklable = Label(root,text="Select Audio Track",bg="lightblue",font=('arial',15,'italic bold'))
    tracklable.grid(row=0,column=0,pady=20)
      
    status = Label(root,text="",bg="lightblue",font=('arial',15,'italic bold'))
    status.grid(row=2,column=1,pady=20)
    
    ######################################################################
    tracklableentry = Entry(root,font=('arial',15,'italic bold'),width='25',textvariable="audiotrack")
    tracklableentry.grid(row=0,column=1,pady=20,padx=20)
    ############################################################################
    browse = Button(root,text="Browse",font=('arial',15,'italic bold'),width='20',bd=5,activebackground='green',command=musicurl)
    browse.grid(row=0,column=2,pady=20,padx=20);
    
    play = Button(root,text="Play",font=('arial',15,'italic bold'),width='14',bd=5,activebackground='green',command=playmusic)
    play.grid(row=1,column=0,pady=20,padx=20);
    
    root.pause = Button(root,text="pause",font=('arial',15,'italic bold'),width='14',bd=5,activebackground='green',command=pausemusic)
    root.pause.grid(row=1,column=1,pady=20,padx=20);
    
    root.resume = Button(root,text="resume",font=('arial',15,'italic bold'),width='14',bd=5,activebackground='green',command=songresume)
    root.resume.grid(row=1,column=1,pady=20,padx=20);
    root.resume.grid_remove();
    
    stop = Button(root,text="stop",font=('arial',15,'italic bold'),width='14',bd=5,activebackground='green',command=stopmusic)
    stop.grid(row=2,column=0,pady=20,padx=20);
    
    
    volup = Button(root,text="volup",font=('arial',15,'italic bold'),width='14',bd=5,activebackground='green',command=volumup)
    volup.grid(row=1,column=2,pady=20,padx=20);
    
    voldown = Button(root,text="voldown",font=('arial',15,'italic bold'),width='14',bd=5,activebackground='green',command=volmdown)
    voldown.grid(row=2,column=2,pady=20,padx=20);
    
    root.mute = Button(root,text="mute",font=('arial',15,'italic bold'),width='8',bd=5,activebackground='green',compound=RIGHT,command=mute)
    root.mute.grid(row=3,column=3,pady=20,padx=20);
    root.mute.grid_remove();
    
    root.unmute = Button(root,text="unmute",font=('arial',15,'italic bold'),width='8',bd=5,activebackground='green',compound=RIGHT,command=unmute)
    root.unmute.grid(row=3,column=3,pady=20,padx=20);
    root.unmute.grid_remove();
    
    ########################################################################################## progress bar volume
    progressbarlable = Label(root,text='',bg='red')
    progressbarlable.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    progressbarlable.grid_remove();
    
    progressbarvol = Progressbar(progressbarlable,orient=VERTICAL,mode='determinate',value=40,length=190)
    progressbarvol.grid(row=0,column=0,ipadx=5)    
    
    progressbarvollable = Label(progressbarlable,text='0%',bg='lightgray',width=3)
    progressbarvollable.grid(row=0,column=0)
    
    ########################################################################################## progress bar for music track
    progressbarmusiclable = Label(root,text='',bg='red')
    progressbarmusiclable.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    progressbarmusiclable.grid_remove();
    
    progressbarmusicstarttime = Label(progressbarmusiclable,text='0.00:0',width=6 ,bg='red')
    progressbarmusicstarttime.grid(row=0,column=0)
    
    progressbarmusic = Progressbar(progressbarmusiclable,orient=HORIZONTAL,mode='determinate',value=0)
    progressbarmusic.grid(row=0,column=1,ipadx=360,ipady=2)   

    progressbarmusicendtime = Label(progressbarmusiclable,text='0.10:0',bg='red')
    progressbarmusicendtime.grid(row=0,column=2)
    
# ******************************************************************************************
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root = Tk()
root.geometry('1100x500+200+50')
root.title("Design and Develop Tarun Aggarwal")
root.iconbitmap("img/music.ico")
root.resizable(False,False)
root.configure(bg='lightblue')
createwidth()
########################################################################################## globle variables
audiotrack = StringVar()
currentvol = 0;
totalsonglen = 0;
count = 0
text = ''

#################################################################
te = "Develop By Tarun Aggarwal"

Slidertext = Label(root,text=te,bg="lightblue",font=('arial',19,'italic bold'))
Slidertext.grid(row=4,column=0,pady=20,padx=40,columnspan=3)
def runslider():
    global text,count
    if(count >= len(te)):
        count = -1
        text = ''
        Slidertext.configure(text=text)
    else:
        text = text+te[count]
        Slidertext.configure(text=text)
    count+=1
    Slidertext.after(200,runslider)
runslider();
mixer.init();
root.mainloop()
