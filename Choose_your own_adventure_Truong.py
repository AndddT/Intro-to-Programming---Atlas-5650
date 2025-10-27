#Introduction to the story 
intro = """
There are many famous anime, like Sailor Moon, where a magical creature grants a student magical powers to
fight evil. However, no one ever talks about how this would play out in the modern world. Today, you will 
get to experience that situation in this CYOA!
One day you are walking back home from a long day at work.
An odd looking white cat with a moon on it's forehead asks if you would like to be granted
magical powers and to fight evil. You will be granted magical transformation powers and fight evil like in 
your favorite anime. In exchange the cat will grant you one wish. 
You are confused on why/how the cat is talking to you but you decide to respond to the cat.
"""
#Presents the user with 2 options 
fightEvil = """
You are now faced with an extremely difficult choice. If you fight evil, you can quit
your corporate job but that sounds dangerous. Or you can walk away and continue your normal life. What will
you do?

1 - I'm sick of my current job, give me those magical powers cat!
2- Leave me alone, I'm going home to bed
"""
#Creates text for if the user chooses to fight evil
fightEvilYes = """
The cat thanks you for helping humanity fight the war against evil. A magical scepter appears out of
thin air. The magic is running through you. A paper contract and pen also appears in front of you."""

#Creates text for if the user chooses to not fight evil
fightEvilNo = """
You walk home, pick up take out and continue your normal life.
"""

print(intro)

#Setting choiced to variables
firstChoice = "2"
secondChoice = "2"
run = True

#This loop will run initially since first choice was already set to 2 
while (firstChoice != "1"):
    firstChoice = input(fightEvil)
    if firstChoice == "1":
        print(fightEvilYes)
#The user will be able to break out of the game and loop if they enter 2
    elif firstChoice == "2":
        print(fightEvilNo)
        run = False
        break #kicks out of first choice loop

    else: 
        print("Please enter 1 or 2")
        firstChoice = input(fightEvil)

#Setting the second part of the story 
storyPt2 = """With that now decided, that cat begins reading the endless terms and agreements. It's longer than
gthe the one you clicked through for your iphone.
"""

contractChoice = """The contract is extremely boring and long. Now you need to decide to read it or not.
1 - Read the contract since it probably has some questionable fine print
2 - Go home, you are too tired to read the contract.
"""

contractChoiceYes = """The contract states you will only be making minimum wage if you choose to fight evil,
but the cat will provide benefits, housing and food cost. You decide to take it since you hate your corporate 
job and this is more exciting
"""

contractChoiceNo = """This contract is too restrictive, you decide to go home."""


thirdChoice = "2"
fourthChoice = "2"

#This loop will only run if the variable Run is True, meaning the user has not eneded the fame 
if run == True and thirdChoice != "1": 
    while (thirdChoice != "1"):
        print(storyPt2)
        thirdChoice = input(contractChoice)
        if (thirdChoice == "1"):
            print(contractChoiceYes)
#This elif will let the user break out of the game 
        elif (thirdChoice == "2"):
            print(contractChoiceNo)
            run = False
            break
        else:  
            print("Please enter 1 or 2")
            thirdChoice = input(contractChoice)

#Creating the ending text to a variable 
ending = """
You sign the contract and the cat informs you that you will have to fight evil for the rest of your
life or until you get defeated by the evil forces. You're coflicted since you didn't expect to fight evil for
that long, you just wanted a break from your corp job.
"""

endingChoice = """
It's now or never and you need to make a decision now. What will you do? 
1 - Decide this is more exciting than your job anyway. Then you take the sceptor, transform 
and go off to fight evil into the night.

2- Rip the contract and run away as fast as you can
"""
endingChoiceYes = """The cat thanks you for your service and you live your life as magical girl/boy and fight evil
for fun.
"""

endingChoiceNo = """Now that the contract is ripped you hightail it home and hope to never see that cat again.
"""

fifthChoice = "2"
sixthChoice = "2"

#This loop will run if the user had not broken out of the game 
if run == True and fifthChoice != "1": 
    while (fifthChoice != "1"):
        print(ending)
        fifthChoice = input(endingChoice)
        if (fifthChoice == "1"):
            print(endingChoiceYes)
#Lets the user break out of the game 
        elif (fifthChoice == "2"):
            print(endingChoiceNo)
            run = False
            break
        else:  
            print("Please enter 1 or 2")
