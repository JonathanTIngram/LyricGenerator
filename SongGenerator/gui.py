#external libraries
import tkinter as tk
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
#other
import SongGenerator



#add button to voice lyrics


class Window:
    def __init__(self,master):
        master.minsize(width = 250, height = 250)
        master.title("Song Genorator version 1.0")
        master.resizable(width=False, height=False)
        master.configure(bg="BLACK")




        lyricLabel = Label(master, text="",
                            fg="#FFFFFF", bg="#000000", font=("Courier", 20))
        lyricLabel.grid(row = 1, column = 1, padx=50, pady=25)


        def lyrics(): #updates lyrics shown
        

            lyricLabel.configure(text=SongGenerator.new_lyric())

        def speech():
            tts = gTTS(text=lyricLabel.cget("text"))
            tts.save('lyric.mp3')
            playsound('lyric.mp3')
            os.remove('lyric.mp3')
        generateButton = Button(master, text="Generate Lyrics",
                                fg="#FFFFFF", bg="#333130", activebackground="#4d231f",
                                font=("Courier", 20), width=15,
                                command = lyrics)
        generateButton.grid(row = 2, column = 1, padx=50)


        voiceButton = Button(master, text="Say Lyrics",
                             fg="#FFFFFF", bg="#333130", activebackground="#4d231f",
                             font=("Courier", 20), width=15,
                             command = speech)
        voiceButton.grid(row=3, column = 1, padx=50)


        creatorLabel = Label(master, text="Created by Jonathan Ingram",
                             fg="#FFFFFF",bg="#000000", font=("Courier",10))
        creatorLabel.grid(row = 4, column = 1, padx = 50, pady=10)





root = tk.Tk()

window = Window(root)
tk.mainloop()
