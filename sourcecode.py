import time
import datetime
import random
import pyttsx3
import speech_recognition as sr

def x(a): #voice engine
if a == 1:
global engine
engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
engine.setProperty('voice',voices[0].id)

elif a==2:

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

elif a==3:
engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
elif a==4:

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',160)

engine.setProperty('voice',voices[3].id)

def slp(n):# sleep function
time.sleep(n)
return True

def speak(audio): #speack function
engine.say(audio)
engine.runAndWait()

def takecom():
r = sr.Recognizer()
with sr.Microphone() as source:
print("Listning.")
audio = r.listen(source)
try:
print("recognising.")
text = r.recognize_google(audio,language='en-in')
except:
text = "error"
return text

def wish(): #greetings
hour = int (datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
return "good morning"
elif hour >= 12 and hour < 18:
return "good afternoon"
else:
return "good evening"

t1 = 0
t2= 0
r1=0
r2=0
o=0
puzzle=0

#name

x(4)
b = wish()
speak(b)
speak("this is a moke interview created for practice purpose. can i get your name please")
name = takecom()

x(2)
speak(f"hello {name}. this application is in developing mode, so there is some instructions you
should follow. 1, please start your answer after see listning in terminal. 2 if your answer is done,
please say next so that A I know wour answer is finished. best of luck")

#start

speak(f"{name} are you ready")
w= takecom()

x(3)

start=time.time()

list1 = [f"{name}, Tell me about yourself",f"{name}, Tell me about yourself without repeating your
name",f"{name}, walk me throug your resume."]
speak(random.choice(list1))
while True:
j=takecom()
l= j.split()
if "error" in l:
break
elif "next" in l:
break
else:
pass

end=time.time()
total= int(end-start)
if total>=120:
o= o+10
elif (total<120 and total >60):
o = o+5

start=time.time()

speak(f"{name},tell me something about your skills and expertise")

while True:
j=takecom()

l= j.split()
if "error" in l:
break
elif "next" in l:
break
else:
pass

end=time.time()
total= int(end-start)
if total>=120:
o= o+10
elif (total<120 and total >60):
o = o+5

start=time.time()
speak(f"what are your strengths, and weaknesses ?")
while True:
j=takecom()
l= j.split()
if "error" in l:
break
elif "next" in l:
break
else:
pass

end=time.time()
total= int(end-start)
if total>=120:
o= o+10

elif (total<120 and total >60):
o = o+5

slp(3)

k=["sorry sir","sorry sir i dont know","dont know","sorry"]
x(2)
speak(f"{name}")

v=[1,2,3,4,5,6,7,8,9,10]
d=random.sample((v),5)

if 1 in d:
speak("what is datatype of 22") #c1
j=takecom()
l=j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif "integer" in l:
t1= t1 + 1
speak(" great")
else:
t2 = t2 +1

if 2 in d:
speak("tell me how much diode required for bridge rectifier") #e1
j=takecom()

l=j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("4" in l) or ("for" in l):
t1= t1 + 1
speak("good")
else:
t2 = t2 +1

if 3 in d:
speak("which material is most commonly used in semiconductor") #e2
j=takecom()
l=j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("Silicon" in l) or ("silicon" in l) :
t1= t1 + 1
speak("nice")
else:
t2 = t2 +1

if 4 in d:
speak("can you tell me Who is the father of Computers?") #c2
j=takecom()
l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("charles" in l) or ("Charles" in l):

t1= t1 + 1
speak("good")
else:
t2 = t2 +1

if 5 in d:
speak(" tell me What is the full form of CPU?") #c3
j=takecom()
l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("central" in l) and ("Processing" in l) and ("Unit" in l):
t1= t1 + 1
speak("good")
else:
t2 = t2 +1

if 6 in d:
speak(f"{name} what is the unit of inductance") #e3
j=takecom()
l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("Henri" in l) or ("Henry" in l) or ("henri" in l) :
t1= t1 + 1
speak("good")
else:
t2 = t2 +1

if 7 in d:
speak(f"{name} Which is the computer language is written in binary codes only? ") #c4
j=takecom()
l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("machine" in l) and ("language" in l) :
t1= t1 + 1
speak("good")
else:
t2 = t2 +1

if 8 in d:
speak(f" can you tell me what is The resistivity of a pure silicon ") #e4
j=takecom()
l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("6000" in l) or (("6" in l)) :
t1= t1 + 1
speak("ok")
else:
t2 = t2 +1

if 9 in d:
speak(f"{name} what happens with current flow in diode, if we increase the depletion layer ")
#e5
j=takecom()

l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("decrease" in l) :
t1= t1 + 1
speak("good")
else:
t2 = t2 +1

if 10 in d:
speak(f" {name}Which of the following is the smallest unit of data in a computer ") #c5
j=takecom()
l= j.split()
if j in k:
t2 = t2+1
speak("ok.")
elif ("bit" in l) :
t1= t1 + 1
speak("ok. nice")
else:
t2 = t2 +1

slp(1)

x(4)
speak(f"{name}, now its a programing round, after you done just say, done")

v=[1,2,3]
d=random.sample((v),2)

if 1 in d:
speak("make simple calculater using your known programing language")
while True:
j=takecom()
l= j.split()
if "error" in l:
pass
elif "sorry" in l:
speak("ok.")
r2=r2+1
break
elif "repeat" in l:
speak("make simple calculater using your known programing language")
else:
r1=r1+1
break

if 2 in d:
speak("can you implement stack data structure")
while True:
j=takecom()
l= j.split()
if "error" in l:
pass
elif "sorry" in l:
speak("ok.")
r2=r2+1
break
elif "repeat" in l:
speak("can you implement stack data structure")

else:
r1=r1+1
break

if 3 in d:
speak("implement an array that can store 1 to 10 numbers")
while True:
j=takecom()
l= j.split()
if "error" in l:
pass
elif "sorry" in l:
speak("ok.")
r2=r2+1
break
elif "repeat" in l:
speak("implement an array that can store 1 to 10 numbers")
else:
r1=r1+1
break

x(3)

start=time.time()

list1 = [f"{name}, where you see yorself in next 5 years"]
speak(random.choice(list1))
while True:

j=takecom()
l= j.split()
if "error" in l:
break
elif "next" in l:
break
else:
pass

end=time.time()
total= int(end-start)
if total>=120:
o= o+10
elif (total<120 and total >60):
o = o+5

start=time.time()

speak(f"tell me 5 things about our company, that make our company different from others")

while True:
j=takecom()
l= j.split()
if "error" in l:
break
elif "next" in l:
break
else:
pass

end=time.time()
total= int(end-start)
if total>=120:
o= o+10
elif (total<120 and total >60):
o = o+5

x(4)
speak(f"{name}. at the last , can you solve this puzzle")
v=[1,2,3]
d=random.sample((v),1)

if 1 in d:
speak("If a giraffe has two eyes, a monkey has two eyes, and an elephant has two eyes, how many
eyes do we have?")
while True:
j=takecom()
l= j.split()
if "error" in l:
pass
elif "sorry" in l:
speak("the answer is 4, 2 eyes of your and 2 of me")
break

elif "repeat" in l:
speak("If a giraffe has two eyes, a monkey has two eyes, and an elephant has two eyes, how
many eyes do we have?")
elif "4" in l:
speak("good")
puzzle= puzzle+1

break

else:
speak("the answer is 4, 2 eyes of your and 2 of me")
break

if 2 in d:
speak("At 3 40, the hour hand and the minute hand of a clock form an angle of how much
degrees")
while True:
j=takecom()
l= j.split()
if "error" in l:
pass
elif "sorry" in l:
speak(" its 130 degrees")
elif "repeat" in l:
speak("At 3 40, the hour hand and the minute hand of a clock form an angle of how much
degrees")

elif "130" in l:
speak("good")
puzzle= puzzle+1
break

else:
speak(" its 130 degrees")
break

if 3 in d:
speak("What is black when you buy it, red when you use it, and gray when you throw it away?")
while True:

j=takecom()
l= j.split()
if "error" in l:
pass
elif "sorry" in l:
speak("it is a charcoal")
break

elif "repeat" in l:
speak("What is black when you buy it, red when you use it, and gray when you throw it
away?")

elif "charcoal" in l:
speak("good")
puzzle= puzzle+1
break

else:
speak("it is a charcoal")
break

speak(f"thank you very much{name}. It was very nice to talk with you. have a great day")

x(1)
speak("here is a feedback or rating of your interview. ")
x(3)
if o>40:
speak(f"{name},you are good in general question keep going")

elif (o<40 and o>20):

speak(f"{name},you have to progress in questions like, tell me about yourself, or, where you see
yourself in next years")
else:
speak(f"{name},you are too week in general questions, you have to progress")

x(2)
speak(f"{name} when it comes to your techinican questions")

if t1==5:
speak("you are good at techinical era")
elif (t1>t2 and t1!=5):
speak("you have to progress in techinical ")
else:
speak("you are too week in techinical, you have to progress ")

x(4)

if puzzle==1:
speak(f"{name}. read some puzzles, in case they can ask")
else:
speak(f"{name}. read some puzzles or some general knowledge, in case they can ask")

x(2)
speak("congratulation on yor successful interview, and best of luck ")