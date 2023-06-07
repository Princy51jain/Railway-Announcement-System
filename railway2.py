import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from playsound import playsound

# function to play music when a button is clicked
def play_music(file_path):
    playsound(file_path)


# set width and height for the interface
SET_WIDTH = 700
SET_HEIGHT = 467

# tkinter GUI starts here
window = tkinter.Tk()
window.title("Princy Jain Indian Railway Announcement System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image= photo)
canvas.pack()

# Buttons to control the playback
btn = tkinter.Button(window, text="Announcement: Dungarpur to Partapur via Sagwara ", width=100, height=4, bg="skyblue", command=lambda: play_music('announcement1 2 6 3 8_1.mp3'))
btn.pack()

btn = tkinter.Button(window, text="Announcement: Ratlam to Partapur via Banswara", width=100, height=4, bg="skyblue", command=lambda: play_music('announcement1 3 6 9 4_2.mp3'))
btn.pack()

btn = tkinter.Button(window, text="Announcement: Partapur to Udaipur via Banswara", width=100, height=4, bg="skyblue", command=lambda: play_music('announcement2 2 8 3 1_3.mp3'))
btn.pack()

window.mainloop()
