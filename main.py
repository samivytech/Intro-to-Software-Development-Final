""""
Author: Sam Kirsch
Class: Intro to Software Development
Last Modified: 12/5/22

This is a program that allows the user to select a major or minor guitar chord chart
"""

#[[[[[TO DO LIST]]]]]
# Draw Main Window
# add title
# add image **NEW**
# add major button **NEW** works!!
# add minor button

# Draw Major Window **NEW** works!!

# add return button **NEW** works!!
# add chord chart label

# add image

# format window **NEW**

# Draw Minor Window

# add return button
# add chord chart label

# add image
# add audio ***NEW** works!!




# import tkinter
import tkinter as tk
import pygame
from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
from PIL import ImageTk, Image
# major chords window
# class for popup window with toplevel

class majorWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # formatting
        self.geometry('600x600')
        self.title('Major Chord Progression')



        # Create Image, set variable to file location
        testImage = Image.open("majorProgression.png") # variable for image

        # Resize Image
        testImage = testImage.resize((300,200), Image.Resampling.BOX)
        majorImg = ImageTk.PhotoImage(testImage) # variables to resize image

        # Place image in label & place label in root
        majorLabel = tk.Label(self, image=majorImg)
        majorLabel.image = majorImg
        majorLabel.place(relx=0.5, rely=0.4, anchor='center')

        # init pygame mixer to use it
        pygame.mixer.init()

        # create function, pygame mixer allows audio file to be called
        def play():
            pygame.mixer.music.load("majorchords.mp3")
            pygame.mixer.music.play(loops=0)



        # Middle Label
        imageLabel = ttk.Label(self, text= 'Major Progression', font=('Helvetica', 21)) #label variable
        imageLabel.place(relx= 0.5, rely= 0.1, anchor='center')

        # Exit button
        returnButton = ttk.Button(self, text='Return Home', command=self.destroy) # return button variable
        returnButton.place(relx=0.15, rely=0.1, anchor = 'center')

        # Play button, command set to play function
        playButton = ttk.Button(self, text='Play Chord Progression', command=play) # play button variable
        playButton.place(relx=0.85, rely=0.1, anchor='center')



# minor chords window (same as major window... different image & audio file)

class minorWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('600x600')
        self.title('Minor Chord Progression')

        returnButton = ttk.Button(self, text='Return Home', command=self.destroy)
        returnButton.place(relx=0.15, rely=0.1, anchor='center')

        imageLabel = ttk.Label(self, text='Minor Progression', font=('Helvetica', 21))
        imageLabel.place(relx=0.5, rely=0.1, anchor='center')

        testImage = Image.open("minorimg.jpg")
        testImage = testImage.resize((300, 200), Image.Resampling.BOX)
        minorImg = ImageTk.PhotoImage(testImage)

        minorLabel = tk.Label(self, image=minorImg)
        minorLabel.image = minorImg
        minorLabel.place(relx=0.5, rely=0.4, anchor='center')

        pygame.mixer.init()

        def play():
            pygame.mixer.music.load("minorchords.mp3")
            pygame.mixer.music.play(loops=0)

        playButton = ttk.Button(self, text='Play Chord Progression', command=play)
        playButton.place(relx=0.85, rely=0.1, anchor='center')



# Home Window

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('600x600')
        self.title('Home')

        # open major window button
        ttk.Button(self,
                   text='Open a Major Chord Progression',
                   command=self.open_majorWindow).pack()
        # open minor window button
        ttk.Button(self,
                   text='Open a Minor Chord Progression',
                   command=self.open_minorWindow).pack()

        # home image
        testImage = Image.open("homeimg.png")

        homeImg = ImageTk.PhotoImage(testImage)

        # home label
        homeLabel = tk.Label(self, image=homeImg)
        homeLabel.image = homeImg
        homeLabel.place(x=200, y=200)



    def open_majorWindow(self):
        window = majorWindow(self)
        window.grab_set()

    def open_minorWindow(self):
        window = minorWindow(self)
        window.grab_set()


# Run app

if __name__ == "__main__":
    app = App()
    app.mainloop()
