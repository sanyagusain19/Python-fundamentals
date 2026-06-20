def main():
    #Taking inputs regarding type of player and level of difficulty
    players = input("Single player or Multiplayer ? ").lower()
    difficulty = input("Hard or Medium or easy ?").lower()

    #checking whether inputed value for difficulty is correct or not.
    if not( difficulty == "hard" or difficulty == "medium" or difficulty == "easy"):
        print("You entered a wrong difficulty value, Try again!")
        return 
    #checking whether inputted value for players are correct or not
    if not(players=="single player" or players == "multiplayer"):
        print("Enter valid player!")
        return
    
    #if-else statements:
    if difficulty == "hard" :
        
        if players == "single player" :
            recommend("Elder ring")
        elif players == "multiplayer":
            recommend("Dota 2 or Counter strike 2")
        
    
    elif difficulty == "medium":
        
        if players == "single player" :
            recommend("Hollow night")
        elif players == "multiplayer":
            recommend("Valorant")
      
   
    else:
        
        if players == "single player" :
            recommend("Minecraft")
        elif players == "multiplayer":
            recommend("amongUs")
       
         
#recommendation function:
def recommend(name):
    print(f"Recommended game is : {name}")
 

main()