print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("    Welcome to treasure island\nYour mission is to find the treasure.")
way=input("You're at a cross road.Where do you want to go? Type 'left' or 'right'\n ")
W=way.lower()
if W=="left":
    l=input("You come to a lake. There is an island in the middle of the lake.Type 'Wait'to wait for a boat. Type 'swim' to swim across\n").lower()
    if l=="wait":
        h=input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue.\nWhich colour do you choose\n").lower()
        if h=="red":
             print("You enter the fire room.\nGame Over")
        elif h=="blue":
             print("You enter the chest room.You have found the treasure.\nYou Win")
        elif h=="Yellow":
             print("You enter the lion's room.\nGame Over")
        else:
             print("please Enter the above 3 colours") 
    elif l=="swim":
             print("You're dead bcoz of the crocodile in the water.\nGame over")
elif W=="right":
     r=input("You enter the cave.There is two way to get out of the cave. Type 'left' or 'right'\n ").lower()
     if r=="left":
          print("You arrive at the bridge which is connected to an island")
          m=input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue.\nWhich colour do you choose\n").lower()
          if m=="red":
             print("You enter the fire room.\nGame Over")
          elif m=="blue":
             print("You enter the chest room.You have found the treasure.\nYou Win")
          elif m=="Yellow":
             print("You enter the lion's room.\nGame Over")
          else:
             print("please Enter the above 3 colours") 
     else:
          print("You went to the bear's territory.\nGame over")