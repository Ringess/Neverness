#!/data/data/com.termux/files/usr/bin/python3
print("Hi! What is your name?")
name=input()
if name == "Kir":
    print("I am glad to see you, old friend!")
elif name == "Kate":
    print("O! I heard about you! You are the most beautiful girl in the world!")
else:
    print("Nice to meet you,", name + "!")
print(name +", now i tell you about my favorite game. It is Subnautika. In this game the man, who has been fallen on the unknown planet, tried to survive. The whole planet is covered by an ocean. In depths you can find many different creatures. Some of them are very dangerous. If you want to survive, you must searching for food, water and resourses, needed to create an instruments.")
print ("Do you like an ocean?")
answer1 = input()
if answer1 == "yes":
    print ("I was sure that yo do! And do you like a whales?")
    answer12 = input()
    if answer12 == "yes":
        print ("I am too")
    else:
        print ("It is bad, because you would meet them")
else:
    print ("So, i am sure, that you should like it.")
    
print ("You can choose your path now. Tell me, what you prefer?" + "\n","1 - become an adventurer\n","2 - become a researcher")
prof=input()
if prof == "1":
    print("It is a good choise. You will participate in many adventures!")
elif prof == "2":
    print("Now you can become a wisest person in the world and get a hidden knowledge!")
else:
    print("So, you will be just a human. It is good too.")
