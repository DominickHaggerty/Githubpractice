

Phillies = input("did the Phillies beat the Marlins in the Wild Card?   ")
Phillies = Phillies.capitalize()


if(Phillies == "Yes"):
    print("The Phillies move on to play the Braves in the NLDS")

    Phillies = input("Did the Phillies beat the Braves in the NLDS?   ")
    Phillies = Phillies.capitalize()
    

else:
    print("The Marlins move on to play the Braves in the NLDS")

    Marlins = input("did the Marlins beat the Braves in the NLDS?   ")
    Marlins = Marlins.capitalize()

    

DBacks = input("did the Diamondbacks beat the Brewers in the Wild Card?   ")

if(DBacks == "Yes"):
    print("The Diamondbacks move on to play the dodgers in the NLDS")

    DBacks = input("Did the DBacks beat the Dodgers in the NLDS?   ")

else:
    print("The Brewers move on to play the Dodgers in the NLDS")

    Brewers = input("Did the Brewers beat the Dodgers in the NLDS?  ")




if(Phillies == "Yes" and DBacks == "Yes"):
    print("The Phillies and the DBacks are playing in the NLCS")

elif(Phillies == "Yes" and DBacks == "No"):
    print("The Phillies play the Dodgers in the NLCS")

elif(Phillies == "No" and DBacks == "Yes"):
    print("The Braves play the DBacks in the NLCS")

elif(Phillies == "No" and DBacks == "No"):
    print("The Braves play the Dodgers in the NLCS")


if(Marlins == "Yes" and Brewers == "Yes"):
    print("The Marlins play the Brewers in the NLCS")

elif(Marlins == "Yes" and Brewers == "No"):
    print("The Marlins play the Dodgers in the NLCS")

elif(Marlins == "No" and Brewers == "Yes"):
    print("The Braves play the Brewers in the NLCS")

elif(Marlins == "No" and Brewers == "No"):
    print("The Braves play the Dodgers in the NLCS")



















