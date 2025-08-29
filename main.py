import streamlit  as st
import pandas as pd

st.image("logo1.png") 
st.image("bg0.png")
st.title("AYUSH PROGRAMING CODES")
st.markdown("<Guided by Google and youtube vidioes> <When you have any dout you can search on ChatGpt>")
button = st.button("VISIT GOOGLE")

if button:
    st.markdown("[Open Google](https://www.google.com)")
st.markdown("<This website for only Education porpose>")
st.markdown("Made by- Ayush kumar")
st.header("WELCOME IN AYUSH coding 🌹")

st.subheader("Ayush Programing")
st.subheader("python coding")
st.markdown("Enter your some BioData")

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Father Name : ")
mnum = st.text_input("Enter Mobile Number : ")
Adr = st.text_input("Enter Your Adress : ")

cllas = st.selectbox("Select Your Class : ",["class6✨","class7✨","class8✨","class9✨","class10✨"])

button = st.button("SUBMIT")
if button:
    st.markdown(f"""
                Name = {name}
                Father Name = {fname}
                Mobile number = {mnum}
                class = {cllas}
                Adress = {Adr}
                """)

# File upload
uploaded_file = st.file_uploader("csv.csv")

if uploaded_file is not None:
    #file read
    file_contents = uploaded_file.read()
    st.write("File uploaded successfully!")

number = st.slider("pick a number", 0, 100)
st.markdown("This is comform for you are not robot")

st.markdown("<LETS MAKE A SIMPLE PROGRAME>")
st.markdown("""-first of all we download python and vscode in our windows
                And make a folder for store our codes and program.
                Also you need to learn python for make asimple program.
                You learn python from youtube and google for basics.
                and ok we start our codings.📑""")
st.subheader("<PRINT HELLO WORLD>")
st.code("""print("hello world")""")
st.markdown("Lets make a simple list and dictionary📚")
st.code("""mark = ("x=100 , y=20 ,t=6 ,r=50")
print("mark")""")
st.subheader("QUIZ🧠")
st.markdown("<When you about some python lets we make a simple quiz program>")
st.subheader("""Time to start building your quiz application.
 Open your editor and creat the file quiz.py with the following content.📂""")
st.code("""answer = input("your question that you ask from anybody")
if answer == "your right answer":
    print("correct")
else:
    print(f"The answer is'you answer', not {answer!r}")
""")
st.markdown("""<A quiz with only one question isn't very exciting! 
You can ask another question by repeatingyour code:>""")
st.code("""answer = input("who discover the ocean map of india ?")
if answer == "Vaskodigama":
    print("correct")
else:
    print(f"The answer is'Vaskodigama', not {answer!r}")

answer = input("which country is the largest country of world ?")
if answer == "Russia":
    print("correct")
else:
    print(f"The answer is'Russia', not {answer!r}")
""")
st.markdown("""<you've addeda question by copying and pasting
the previous code then changing the question text and the correct 
answer.Again, you can test this by running the script:>""")

st.markdown("""<It works! However, copying and pasting
code like this isn't great. There's a programing principal
called (Don't Repeat Yourself(DRY)), which says that you 
should usualy avoid repeated code becouse it gets hard to maintain.>
""")
button = st.button("CLICK HERE FOR A CODE🖥")
if button:
    st.subheader("Simple code for make a simple text to speech")
    st.markdown("<This is simple way of learning the talking AI and coding>")
    st.markdown("<You need pttysx3 module for run this text to speech>")
    st.code("""import pyttsx3
    engine = pyttsx3.init()

    engine.say("Type your text to speech")
    engine.runAndWait()
""")

button = st.button("CLICK HERE FOR A SIMPLE TALKING CHAT CODE")
if button:
    st.subheader("Simple Talking AI")
    st.markdown("<Lets go to make a simple Talking chatai>")
    st.markdown("<Made for this proectyou known that some python coding.>")
    st.markdown("You makethis project and enjoy.")
    st.code("""
 import pyttsx3
import webbrowser
engine = pyttsx3.init()

engine.say("hello! i am jarvis and welcome in this programing AI")
engine.runAndWait()

engine.say("@ what is your name?")
engine.runAndWait()

answer = input(" {text!r} ")
if answer == (f"user"):
    engine.say("nicen name user")
    engine.runAndWait()

else:
    engine.say("ok")
    engine.runAndWait()

engine.say("@ can you talk with me?")
engine.runAndWait()

answer = input(" {text!r} ")
if answer == ("ok"):
    engine.say("nice")
    engine.runAndWait()

else:
    engine.say("realy ok but i want to talk with you")
    engine.runAndWait()

engine.say("@ how are you?")
engine.runAndWait()

answer = input(" {text!r} ")
if answer == ("i am fine"):
    engine.say("ok !nice")
    engine.runAndWait()

else:
    engine.say("ok")
    engine.runAndWait()

""")

button = st.button("CLICK HERE FOR A SIMPLE TTOW")
if button:
    st.markdown("This is simple text to open webbrowser")
    st.code("""import pyttsx3
import webbrowser
import pyaudio
import speech_recognition as sr 

engine = pyttsx3.init()
recognizer = sr.Recognizer()

engine.say("hello! i am piyush and welcome in this programing AI")
engine.runAndWait()

answer = input("@input app name = ")
if answer == ("open google"):
    webbrowser.open("https://www.google.com")

elif answer == ("open google and search python")
    webbrowser.search("https://www.google.com/search q=search or enter website")

elif answer ==("open chrome"):
    webbrowser.open("https://www.chrome.com")

elif answer ==("open youtube"):
    webbrowser.open("https://www.youtube.com")

elif answer ==("serach python"):
    webbrowser.open("https://www.bing.com/search?q=python+download")
""")

button = st.button("CLICK FOR A BEST CODES")
if button:
    st.markdown("This a simple code for make a simple shooter game")
    st.markdown("This code only for education porpose")
    st.code("""import pygame

pygame.init()

# creat the window
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('car game')

#colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255,255)
yellow = (255, 255, 0)

# game settings
gameover = False
speed = 2
score = 0

# game loop
fps = 120


 # drow the grass
screen.fill(green)

pygame.display.update()

pygame.quit()

""")
st.markdown("👉This all the run only in the python and you also use vscode for run your python.")
st.markdown("We try to give you best experience in our website and try to give you more codes 📜🗂")

button = st.button("CLICK FOR A BEST GAME CODE")
if button:
    st.code("""import pygame
import sys
import random

# Invitialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_height, screen_height))
pygame.display.set_caption("simple shoter game")

# Set background
background = pygame.image.load("background.png")
screen.Surface("background.png")

# Set the frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Bullet settings
bullet_width = 5
Bullet_height = 10
bullet_speed = 7
bullet = []

# Enemy settings
enemy_width = 50
enemy_height = 60
enemy_speed = 2
enemies = []
# Spawn an enemy every 2 seconds
enemy_timer = 0
enemy_spawn_time = 2000

# Collision detection function 
def check_collision(rect1, rect2):
    return pygame.Rect(rect1, rect2).colliderect(pygame.Rect(rect2))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Creat a bullet at the current player position
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x <screen_width - player_width:
        player_x +=player_speed

    # Update bullet positions
    for bullet in bullet:
        bullet[1] -=bullet_speed
    bullets = [bullet for bullet in bullet if bullet[1] > 0]

    # Update enemy positions and spawn new ones
    current_time = pygame.time.get_ticks()
    if current_time - enemy_timer > enemy_spawn_time:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x,enemy_y])
        enemy_timer = current_time

    for enemy in enemies:
        enemy[1] += enemy_speed
    
    # Check for collisions
    for bullet in bullet[:]:
        for enemy in enemies[:]:
            if check_collision((bullet[0], bullet[1], bullet_width,Bullet_height
                              (enemy[0], enemy[1], enemy_width, enemy_height))):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    # Remove enemies that are off the screen
    enemies = [enemy for enemy in enemies if enemy[1] < screen_height]

    # Fill the screen with black
    screen.fill((-0, 0, 0))
     
    # Draw the bullets
    for bullets in bullet:
        pygame.draw.rect(screen, (255, 255, 255), (bullet[0], bullet[1], bullet_width, bullet_height))

     # Draw the enemies
    for bullets in bullet:
        pygame.draw.rect(screen, (255, 255, 255), (enemy[255], enemy[0], enemy_widtht, enemy_height))

    # Update the display 
    pygame.display.flip()

    # Cap the frame rate at 60 Fps
    pygame.time.Clock =(60)
""")
st.markdown("This code for make a simple chating bot.")
button = st.button("CHATBOT CODE")
if button:
    st.code("""answer = input("@ hello!
if answer =="hello":
    print("hii")
else:
    print("hello")

answer = input("@ How are you?")
if answer == ("fine"):
    print("nice")
else:
    print(f"ok {answer!r}")

answer = input("@ can you talk with me?")
if answer == ("yes"):
    print("realy")
else:
    print("realy ok but i want to talk with you")
    
answer = input("@ what is your your name?")
if answer == ("ayush"):
    print("nice name")
else:
    print("ok")

answer = input("@ which class in you read?")
if answer == ("9"):
    print("nice!")
else:
    print("ok nice!")

answer = input("@ in which country you live?")
if answer == ("india"):
    print("oh this is nice place i can to visit india")
else:
    print("ok but i am from india")

answer = input("@ you know that who i am?")
if answer == ("no"):
    print("i am AI of Ayush")
else:
    print("ok i am a ai")

answer = input("@ i think i enogh talk with you?")
if answer == ("ok"):
    print("ok byyy")
else:
    print("i can try to talk with you latter byy")""")




category = st.radio("select a categry", ["open", "CODE OF JARVIS🤖", "PRANK WITH FRIEND🦧", "MAKE YOUR OWN APP📱"])

if category =="open":
    st.markdown("Select second button for code")

if category == "CODE OF JARVIS🤖":
    st.markdown("This is our best project becouse in this project we make a our own jarvis like iron man jarivis.📳")
    st.markdown("For this project we need virtual envuroment in our folder.")
    st.code("""import speech_recognition as sr 
import webbrowser
import pyttsx3

# Pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def  processCommand(command):
    print(command)
    pass

if __name__=="__main__":
    speak("initializing jarvis.....")
    while True:
        # Listen for the wake word "jarvis"
        r = sr.Recognizer()
        

        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=5)
            command = r.recognition_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes i listen you")
            # Listen for command
            with sr.Microphone() as source:
                print("Active jarvis.....")
                audio = r.listen(source)
                command = r.recognition_google(audio)

                processCommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))
""")

elif category == "PRANK WITH FRIEND🦧":
    st.markdown("This cde only for education porpose please don't try for another porpose")
    st.code("""while True:
    print("ramdom ramdom%ramdom%r%ramdom% ramdom%ramdom%/
    ramdom%ramdom%ramdom ramdom%ramdom%r%ramdom% ramdom%ramdom%ramdom%ramdom%")
    """)

elif category == "MAKE YOUR OWN APP📱":
    st.markdown("👉This is flask module and this is use for make a \
    simple website you also make a simple website for your knowlage and fun.")
    st.code("""from flask import Flask

app = Flask(__name__)

@app.route("/")
def greet():
    return "Hello, World!"
""")

st.markdown("👉When you have any dout or promblem you see youtube vidios and know about\
batter for knowladge.")
button = st.button("VISIT YOUTUBE")
if button:
    st.markdown("[Open YouTube](https://www.youtube.com)")

st.subheader("ABOUT STREAMLIT")
st.subheader("MAKE YOUR OWN WEBSITE BY THE HELP OF STREAMLIT")

st.subheader("What is streamlit?")
st.markdown(""""Streamlit is an open-source Python library that makes it easy to create 
and share custom web apps for machine learning and data science. By using Streamlit
 you can quickly build and deploy powerful data applications. For more information about the open-source library,
  see the Streamlit Library documentation.
""")
st.subheader("What is Streamlit used for?")
st.image("stream2.png")
st.markdown("""Streamlit is an open-source Python library that makes it easy to create and share custom web apps for machine learning and data science.
 By using Streamlit you can quickly build and deploy powerful data applications.
  For more information about the open-source library, see the Streamlit Library documentation.""")

st.subheader("What is benifit of streamlit?")
st.image("stream.png")

st.markdown("""  One of the standout advantages of Streamlit is its rapid development cycle,
   which allows developers and data scientists to create and iterate on interactive web applications quickly
""")

st.subheader("What is streamlit best for ?")
st.image("stream6.png")
st.markdown("""Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time.
 Streamlit is the easiest way especially for people with no front-end knowledge to put their code into a web application:
 No front-end (html, js, css) experience or knowledge is required.""")

st.subheader("is streamlit is a languese?")
st.image("stream5.png")
st.markdown("""Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time.
 Streamlit is the easiest way especially for people with no front-end knowledge to put their code into a web application:
 No front-end (html, js, css) experience or knowledge is required.

 Does Streamlit require Internet?
 Streamlit's core functionality, running a local server and displaying the app in your browser, does not require an internet connection.
  However, some Streamlit features, like sharing through Streamlit Sharing or deploying to Streamlit Community Cloud, do require internet access.

 Elaboration:
Local Development & Running:
You can develop and run Streamlit apps locally without needing an internet connection. The Streamlit server runs on your machine, and the app displays in your web browser within your local environment. 
Internet Dependency:
Some features rely on internet connectivity: 
Sharing: Streamlit's sharing feature allows you to easily share your app with others by generating a temporary URL. This URL is hosted by Streamlit and thus requires internet access. 
Cloud Deployment: If you choose to deploy your app to the Streamlit Community Cloud, you'll need an internet connection to interact with the cloud services. 
External Data: If your Streamlit app interacts with external data sources (e.g., databases, APIs) that reside online, it will require internet access to retrieve that data. 
Offline Functionality:
You can create Streamlit apps that function offline by: 
Caching data using Streamlit's caching feature. 
Ensuring that all required libraries and data are available locally. 
Avoiding resources that demand internet access, such as web fonts or external scripts. 
""")
st.subheader("Is Streamlit better than React?")
st.markdown("""Since Streamlit is all Python, you usually don't need to know HTML, CSS, or JavaScript. However, if you do need some really custom UI components, knowing a bit of React might be useful.
 Streamlit is ideal for small projects, like quick internal data tools and dashboards.
""")
st.subheader("Who created Streamlit?")
st.markdown("""Streamlit was founded in 2018 by Adrien Treuille, Thiago Teixeira and Amanda Kelly,
 who were frustrated by the lack of easy and fast ways to share their data projects with others.
""")
st.subheader(" Is Streamlit a server?")
st.image("strea4.png")
st.markdown("""Streamlit apps have a client-server structure.
 The Python backend of your app is the server. The frontend you view through a browser is the client.
""")
st.subheader("What is the purpose of Streamlit?")
st.markdown("""Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps.
 Once you've created an app, you can use our Community Cloud platform to deploy, manage, and share your app.
""")
st.subheader("How safe is Streamlit?")
st.markdown("""Encryption. All Streamlit apps are served entirely over HTTPS.
 All data sent to or from Streamlit over the public internet is encrypted in transit using 256-bit encryption.
""")

st.subheader("What is the resource limit for Streamlit?")
st.markdown(""" 1GB RAM limit
Alternatively, since Streamlit Cloud has a 1GB RAM limit, you might want to consider deploying your app on platforms like GCP, AWS, to name a few. These platforms offer more memory and greater control over your app's environment.
 Feel free to reach out if you have any questions or want to discuss these options further!""")

st.markdown("-Ayush programing code")
st.markdown("This all imformation only for education porpose")

button = st.button("CLICK FOR A BEST 🎁")
if button:
    st.markdown("Thanks for visit this website 🌹💐🌹")

st.image("logo1.png")