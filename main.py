# RULE BASED AI PYTHON CHATBOT

import datetime 
import time

name= input("Please, Enter Your Name :")
presenthour= datetime.datetime.now().hour

if 5<= presenthour <=11:
    print("Good Morning",name)
elif 11<= presenthour <=17:
    print("Good Afternoon",name)
elif 17<= presenthour <=20:
    print("Good Evening",name)
else:
    print("Good Night",name)



print("Welcone to Rule Based AI Chatbot",name)
print("you can ask me basic quetion, if you want to exit type 'bye'")


# Creating chatbot Memory [dictionary of responses]

responses= {
    "hi": "hey, how are you",
    "how are you":"I am fine, What about you how are you",
    "who are you":"I am a Rule Based Python Chatbot, Which give basic quetions anser",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
}

def getresponseofBot(userquetion):
    userquetion= userquetion.lower()
    for eachkey in responses:
        if  eachkey in userquetion:
            return responses[eachkey]
    

    return "I am not able to tell you that quetion answe, i will tell you when i knowing that answer"



# Taking user query

while    True :
    userInput= input("Please Enter your quetions:",)

    reply= getresponseofBot(userInput)
    print("Bot responses:",reply)


    # for Exit 

    if "bye" in userInput.lower():
        print("Thank you for using me",)
        break


