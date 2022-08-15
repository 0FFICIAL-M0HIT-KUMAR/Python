print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  a8P_____88  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          8PP""""""" 
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          "8b,   ,aa
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88           `"Ybbd8"'  
''')

print("Welcome to Treasure Island")
print("your mission is to find tha treasure")
decision=input('''Your're at a cross road, where do you want to go ? Type "Left" or "Right" \n''')
decision=decision.lower()

if decision=="right":
  print("You fell into a hole. ---GAME OVER---")
else:
  print('''You've come to lake . There is an island in the middle of the lake.''')
  decision=input('Type "wait" to wait for a boat. Type "Swim" to swim across\n')
  decision=decision.lower()

  if decision=="swim":
    print("You get attacked by an angry thout. ---GAME OVER---")
  else:
    print("you arrive at the island unharmed. There is a house with 3 doors.")
    decision=input('one "Red", one "Yelllow" and one "Blue" . Which colour do you choose ?\n')
    decision=decision.lower()
    if decision=="red":
      print("It,s a room full of fire. ---GAME OVER---")
    elif decision=="blue":
      print("You enter a room of beasts. ---GAME OVER---")
    else:
      print("You found the treasure ! ---YOU WIN !---")