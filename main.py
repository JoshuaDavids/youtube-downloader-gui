import tkinter as tk

from pytube import *


def download():
    global E1
    strAtr = E1.get()
    Yt = YouTube(str(strAtr))
    videos = Yt.get_videos()
    s = 1
    for v in videos:
        print(str(s) + '.' + str(v))
        s += 1
    n = int(input('Enter your choice: '))
    vid = videos[n - 1]
    destination = str(input('Select the directory you wish to store your file: '))
    vid.download(destination)


root = tk.Tk()

w = tk.Label(root, text='YouTube Video Downloader')
w.pack()

E1 = tk.Entry(root, bd=5)
E1.pack(side=tk.TOP)

button = tk.Button(root, text='Download', command=download())
button.pack(side=tk.BOTTOM)

root.mainloop()
