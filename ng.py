import random

fNameM = ['Bob', 'Jim', 'Isaac', 'Jacob', 'Luke', 'Riley']
fNameF = ['Rachel', 'Tammy', 'Sarah', 'Hadley', 'Abby']
lName = ['Smith', 'Lorenzo', 'Dussault', 'Williams', 'Johnson']

randomChooser = input("To select Male or Female, press m or f")

if randomChooser == "m":

        from random import randrange

        random_index = randrange(0,len(fNameM))

        print (fNameM[random_index])

        from random import randrange

        random_index = randrange(0,len(lName))

        print (lName[random_index])

elif randomChooser =="f":

        from random import randrange

        random_index = randrange(0,len(fNameF))

        print (fNameF[random_index])

        from random import randrange

        random_index = randrange(0,len(lName))

        print (lName[random_index])

else:
       print("Input Not Recognized")
