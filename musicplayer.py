from pygame import mixer
import tkinter
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

current_volume = float(0.5)
def play_song():
    filename = filedialog.askopenfilename(initialdir="/",title="please select a music:", filetypes = (("Text files",  "*.txt*"), ("all files", "*.*")))
    current_song = filename
    song_title = filename.split("/n")
    song_title = song_title[-1]

    try:
            mixer.init()
            mixer.music.load(current_song)
            mixer.music.set_volume(current_volume)
            mixer.music.play()
            song_title_label.config(fg="green", text="Now Playing:" + str(song_title))
            volume_label.config(fg="green",text="Volume : " + str(current_volume))

    except Exception as e:
            print(e)
            song_title_label.config(fg="red", text="Error playing track")
def reduce_volume():
    try:
        global current_volume
        if current_volume <=0:
            volume_label.config(fg="red", text="Volume : muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasn't been selected yet")

def increase_volume():
    try:
        global current_volume
        if current_volume >=1:
            volume_label.config(fg="green", text="Volume : max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume,1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red",text="Track hasn't been selected yet")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="track hasn't been selected yet")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="track hasn't been selected yet")


#main screen
master = Tk()
master.title("music player")

#labels
Label(master,text="custom music player", font=("calibri",15),fg= "red").grid(sticky="N", row=0, padx=120)
Label(master,text= "please select a music track", font=("Calibri",12), fg="blue").grid(sticky="N", row=1)
Label(master,text= "Volume", font=("Calibri",12), fg="red").grid(sticky="N", row=4)
song_title_label = Label(master, font=("calibri", 12))
song_title_label.grid(stick="N",row=3)
volume_label = Label(master,font=("Calibri",12))
volume_label.grid(sticky="N",row=5)

#buttons
Button(master, text="Select Song", font=("Calibri",12), command=play_song).grid(row=2,sticky="N")
Button(master, text="pause",font=("Calibri",12), command=pause).grid(row=3,sticky="E")
Button(master, text="Resume",font=("Calibri",12), command=resume).grid(row=3,sticky="W")
Button(master, text="-",font=("Calibri",12),width=5,command=reduce_volume).grid(row=5,sticky="W")
Button(master, text="+",font=("Calibri",12),width=5,command=increase_volume).grid(row=5,sticky="E")


master.mainloop()

