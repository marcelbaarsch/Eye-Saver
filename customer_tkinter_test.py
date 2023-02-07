import tkinter as tk
import time
import pygame
from tkinter import messagebox

pygame.init()
pygame.mixer.music.load("powerUp.wav")

def show_fullscreen_message():
    pass

def start_timer():
    count = int(20) * 60
    for i in range (count, 0, -1):
        minutes, seconds = divmod(i, 60)
        label['text'] = "Remaining time: {:02d}:{:02d}".format(minutes, seconds)
        time.sleep(1)
        root.update()

    pygame.mixer.music.play()
    messagebox.showinfo("Time's up!", "Look away from the computer for 1 minute")

root = tk.Tk()
root.title("Eye Saver App")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

width = 300
height = 100
x = screen_width - width
y = screen_height - height - int(height/2)

root.geometry("{}x{}+{}+{}".format(width, height, x, y))


label = tk.Label(root, text="Save your eyes!")
label.pack()

#entry = tk.Entry(root)
#entry.pack()

button = tk.Button(root, text="Start Timer", command=start_timer)
button.pack()

root.mainloop()