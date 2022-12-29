import os
from pygame import mixer
from tkinter import *
from threading import *
from tkinter import filedialog


def threadingplay():
    t1 = Thread(target=play_music)
    t1.start()

def threadingstop():
    t1 = Thread(target=pause_music)
    t1.start()

def threadingpause():
    t1 = Thread(target=resume_music())
    t1.start()



def play_music():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    lbl.config(text=music_name[0:-4], bg="black", fg="white", font="Arial 15 bold")


def pause_music():
    mixer.music.pause()
    lbl.config(text="Pause", bg="black", fg="white", font="Arial 15 bold")


def resume_music():
    mixer.music.unpause()
    music_name = playlist.get(ACTIVE)
    lbl.config(text=music_name[0:-4], bg="black", fg="white", font="Arial 15 bold")


def openf ():
    path = filedialog.askdirectory()
    os.chdir(path)
    songs = os.listdir(path)
    for song in songs:
        if song.endswith(".mp3"):
           playlist.insert(END, song)


mixer.init()
root = Tk()
root.title("Player")
root.config(bg="black")
root.geometry("350x550")
root.resizable(False, False)


iconplay = PhotoImage(file="3.png")
iconpause = PhotoImage(file="1.png")
iconpresume = PhotoImage(file="2.png")
iconpopenf = PhotoImage(file="4.png")


btn_open = Button(root,image=iconpopenf, bg="black", relief=FLAT, command=openf ).place(x=155, y=300)
btn_play = Button(root, command=threadingplay, image=iconplay, bg="black", relief=FLAT).place(x=37, y=380)
btn_stop = Button(root, command=threadingstop, image=iconpause, bg="black", relief=FLAT).place(x=242, y=380)
btn_resume = Button(root, command=threadingpause, image=iconpresume, bg="black", relief=FLAT).place(x=139, y=380)


playlist = Listbox(root, width=32, height=6, bg="white", font="Arial 15 bold")
playlist.pack()


lbl = Label(root, bg="black")
lbl.pack(pady=40)


root.mainloop()