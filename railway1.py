import pandas as pd    # pip install pyaudio  # pip install pandas
from pydub import AudioSegment  # pip install pydub
from gtts import gTTS   # pip install gTTS
import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from playsound import playsound

# function to play music when a button is clicked
def play_music(file_path):
    playsound(file_path)


def textToSpeech(text, filename, language):
    mytext = str(text)
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)


def mergeAudios(audios):
    # this function returns pydubs audio segment
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined
    

def generateSkeleton():
    audio = AudioSegment.from_mp3("railway.mp3")

# //////////////////////////////////////////Hindi Announcement :

    # 1. Generate kripiya dhayan dijiye
    start =41500
    finish =43950
    audioProcessed = audio[start:finish]
    audioProcessed.export("1.mp3", format="mp3")

    # 2. is from city

    # 3. Generate se chalkar
    start =44900
    finish =46000
    audioProcessed = audio[start:finish]
    audioProcessed.export("3.mp3", format="mp3")

    # 4. is via city

    # 5. Generate ke raste
    start =47500
    finish =48750
    audioProcessed = audio[start:finish]
    audioProcessed.export("5.mp3", format="mp3")

    # 6. is to city

    # 7. Generate ko jaane wali gaadi sakhya
    start =49600
    finish =52700
    audioProcessed = audio[start:finish]
    audioProcessed.export("7.mp3", format="mp3")

    # 8. is train no and name

    # 9. Generate kuch hi samay mei platform sankhya
    start =59000
    finish =62000
    audioProcessed = audio[start:finish]
    audioProcessed.export("9.mp3", format="mp3")

    # 10. is platform number

    # 11. Generate par aa rahi hai
    start = 62800
    finish = 64500
    audioProcessed = audio[start:finish]
    audioProcessed.export("11.mp3", format="mp3")

# //////////////////////////////////////////English Announcement :
    start =18500
    finish =19700
    audioProcessed = audio[start:finish]
    audioProcessed.export("12.mp3", format="mp3") 

    # 1. Generate may i have your attention please train no 
    start =112000
    finish =116000
    audioProcessed = audio[start:finish]
    audioProcessed.export("13.mp3", format="mp3")

    # 2. is train no and name

    # 3. Generate from
    start =122750
    finish =123450
    audioProcessed = audio[start:finish]
    audioProcessed.export("15.mp3", format="mp3")

    # # 4. is from city

    # 5. Generate to
    start =124050
    finish =124850
    audioProcessed = audio[start:finish]
    audioProcessed.export("17.mp3", format="mp3")

    # 6. is to city

    # 7. Generate via
    start =126150
    finish =127150
    audioProcessed = audio[start:finish]
    audioProcessed.export("19.mp3", format="mp3")

    # 8. is via city

    # 9. Generate is arriving shortly on platform number 
    start =128800
    finish =132900
    audioProcessed = audio[start:finish]
    audioProcessed.export("21.mp3", format="mp3")

    # 10. is platform number


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    for index, item in df.iterrows():

# /////////////////////////////////// hindi announcement        
        # 2. Generate from-city
        textToSpeech(item['from'], '2.mp3', "hi")

        # 4. Generate via-city
        textToSpeech(item['via'], '4.mp3', "hi")

        # 6. Generate to-city
        textToSpeech(item['to'], '6.mp3', "hi")

        # 8. Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '8.mp3', 'hi')

        # 10. Generate platform number
        textToSpeech(item['platform'], '10.mp3', "hi")

# /////////////////////////////////// english announcement 
        # 2. Generate from-city
        textToSpeech(item['from'], '16.mp3', "en")

        # 4. Generate via-city
        textToSpeech(item['via'], '20.mp3', "en")

        # 6. Generate to-city
        textToSpeech(item['to'], '18.mp3', "en")

        # 8. Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], '14.mp3', "en")

        # 10. Generate platform number
        textToSpeech(item['platform'], '22.mp3', "en")

        audios = [f"{i}.mp3" for i in range(1,23)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement{item['train_no']}_{index+1}.mp3", format="mp3")
    return df

if __name__ == '__main__':
    print("Generating skeleton...")
    # generateSkeleton()
    print("Now generating announcement...")
    exel = generateAnnouncement("announce_hindi.xlsx")
    print("all generated")
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
    # btn = tkinter.Button(window, text="Announcement: Dungarpur to Partapur via Sagwara ", width=100, height=4, bg="skyblue", command=lambda:play_music('announcement1 2 6 3 8_1.mp3'))
    # btn.pack()

    # btn = tkinter.Button(window, text="Announcement: Ratlam to Partapur via Banswara", width=100, height=4, bg="skyblue", command=lambda:play_music('announcement1 3 6 9 4_2.mp3'))
    # btn.pack()

    # btn = tkinter.Button(window, text="Announcement: Partapur to Udaipur via Banswara", width=100, height=4, bg="skyblue", command=lambda:play_music('announcement2 2 8 3 1_3.mp3'))
    # btn.pack()

    for index, item in exel.iterrows():
        btn = tkinter.Button(window, text=f"{item['from'].capitalize()} to {item['to'].capitalize()} ({item['train_name'].capitalize()})", background='skyblue', border=5, width=100, height=3, command=lambda:play_music(f"announcement{item['train_no']}_{index+1}.mp3"))
        btn.pack()

    window.mainloop()
