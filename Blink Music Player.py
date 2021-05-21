# Importing Required Modules & libraries
from tkinter import *
import pygame
import os

global volVal
volVal = 1.0

# Defining MusicPlayer Class
class MusicPlayer:

  # Defining Constructor
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Music Player Project")
    # Window Geometry
    self.root.geometry("1000x350+300+200")
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()

    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text=" Now Playing ",font=("comic sans ms",15,"bold"),bg="#5CDB95",fg="#2E1114",bd=8,relief=GROOVE)
    trackframe.place(x=0,y=0,width=600,height=200)
    # Inserting Song Track Label
    songtrack = Label(trackframe,textvariable=self.track,justify='center',wraplength=400,width=70,font=("ubuntu",10,"bold"),bg="#5CDB95",fg="#2A1B3D").grid(row=0,column=0,padx=15,pady=20)
    # Inserting Status Label
    trackstatus = Label(trackframe,textvariable=self.status,font=("verdana",15,"bold"),bg="#5CDB95",fg="#25274D").grid(row=1,column=0,padx=1,pady=1)

    # Creating Button Frame
    buttonframe = LabelFrame(self.root,text=" Control Panel ",font=("comic sans ms",15,"bold"),bg="#8EE4AF",fg="#2E1114",bd=8,relief=GROOVE)
    buttonframe.place(x=0,y=200,width=600,height=150)
    # Inserting Play Button
    playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=6,height=1,font=("courier",16,"bold"),fg="black",bg="#16FFBD").grid(row=0,column=0,padx=35,pady=5)
    # Inserting Pause Button
    playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=10,height=1,font=("courier",16,"bold"),fg="black",bg="#FFB48F").grid(row=0,column=1,padx=35,pady=5)
    # Inserting Unpause Button
    playbtn = Button(buttonframe,text="RESUME",command=self.unpausesong,width=10,height=1,font=("courier",16,"bold"),fg="black",bg="#15DB95").grid(row=1,column=1,padx=35,pady=5)
    # Inserting Stop Button
    playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=6,height=1,font=("courier",16,"bold"),fg="black",bg="#FF652F").grid(row=1,column=0,padx=35,pady=5)
    # Inserting Volume UP Button
    playbtn = Button(buttonframe,text="VOLUME +",command=self.volumeup,width=10,height=1,font=("courier",16,"bold"),fg="black",bg="#FF652F").grid(row=0,column=2,padx=35,pady=5)
    # Inserting Volume DOWN Button
    playbtn = Button(buttonframe,text="VOLUME -",command=self.volumedown,width=10,height=1,font=("courier",16,"bold"),fg="black",bg="#FF652F").grid(row=1,column=2,padx=35,pady=5)

    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,text=" Song Playlist ",font=("comic sans ms",15,"bold"),bg="#15DB95",fg="#2E1114",bd=8,relief=GROOVE)
    songsframe.place(x=600,y=0,width=400,height=350)
    # Inserting scrollbar
    scrol_y = Scrollbar(songsframe,orient=VERTICAL)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",justify=LEFT,height=20,selectmode=SINGLE,font=("ubuntu",10,"italic"),bg="silver",fg="black",bd=8,relief=GROOVE)
    # Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill="both")
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)
    # Changing Directory for fetching Songs
    os.chdir(r"C:\Users\Saransh\Documents\GitHub\Music-Player\Music")
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END,track)

  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set(self.playlist.get(ACTIVE))
    # Displaying Status
    self.status.set("\u25B6 Playing")
    # Loading Selected Song
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()

  def stopsong(self):
    # Displaying Status
    self.status.set("\u23F9 Stopped")
    # Stopped Song
    pygame.mixer.music.stop()

  def pausesong(self):
    # Displaying Status
    self.status.set("\u23F8 Paused")
    # Paused Song
    pygame.mixer.music.pause()

  def unpausesong(self):
    # Displaying Status
    self.status.set("\u25B6 Playing")
    # Playing back Song
    pygame.mixer.music.unpause()

  def volumeup(self):
      #Volume Up function
      global volVal
      #Volume MAX 1.0
      if volVal < 1.0:
          volVal += 0.1
          pygame.mixer.music.set_volume(volVal)
          self.status.set(f"Volume + {int(volVal*10)}")
      else:
          self.status.set("Max Volume")
      
  def volumedown(self):
      #Volumee Down function
      global volVal
      #Volume MIN 0.1
      if volVal > 0.1:
          volVal -= 0.1
          pygame.mixer.music.set_volume(volVal)
          self.status.set(f"Volume - {int(volVal*10)}")
      else:
          self.status.set("Min Volume")
      

# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()