import random



def welcome_message():
    print("You gonna play till you make 3 wins ! \n") 


def print_the_choise_for_both(user_choise,pc_choise):
    print("\n|You have selected " +user_choise+ " |")
    print("|The pc have selected " +pc_choise+ "|\n")
    
def pc_choise(pc):
     userlist=["ROCK","PAPER","SCISSORS"]
     pc=random.choice(userlist) 
     return pc

  
def player_choise(Player):
     

     userlist=["ROCK","PAPER","SCISSORS"]
     while True:
                try:
                    
                    Player = str(input("Give your choise from the following words ROCK,PAPER,SCISSORS:"))
                    Player=Player.upper()
                   
                
                except TypeError:
                    print('Please enter a word such as shown above') 
                    continue
                
                except EOFError:
                    print('Please input something') 
                    continue
                
                if Player in userlist:     #αν υπαρχει αυτο που επελεξε ο χρηστης στην λιστα 
                    return Player
                    break
                   
                else:                    #ελεγχος αν εδωσε εγκυρη απαντηση
                    print('Please enter a word such as shown above')
                        


    

    

userwon=0   
tie=0
pcwon=0
    
    
welcome_message()  #μυνημα χαιρετησμου
    
    
while userwon!=3 :
    
            x=str       
            y=str       
               
            
            
            user=player_choise(x) #επιλογη του χρηστη
            pc=pc_choise(y) # RNG για το τι θα επιλεξει το PC 
            
            
            print_the_choise_for_both(user,pc) #τυπωνει και τις 2 επιλογες(χρηστη,pc)
            
                                
            
            if  (pc=="ROCK" and user=="SCISSORS" ) or ( pc=="SCISSORS" and user=="PAPER" ) or  (pc=="PAPER" and user=="ROCK"):
                print("THIS ROUND GOES TO PC !  \n")
                pcwon += 1      #μετρητης για τις νικες του pc
                            
                
            elif pc==user:                #μετρητης για ισοπαλιες
                print(">> Ιt's a tie <<\n")
                tie += 1 
                
                                
            elif (user=="ROCK" and pc=="SCISSORS") or (pc=="PAPER" and user=="SCISSORS") or (user=="PAPER" and pc=="ROCK"):
                print("CONGRATULATIONS ! You won this round !\n")
                userwon += 1 #μετρητης για τις νικες του χρηστη 
                        
                
                    
            print("THE CURRENT SCORE IS : \n USER:",userwon,"\n PC:",pcwon) #τυπωνει το σκορ στην οθονη 
        
else:
       if userwon==3:           #μετρητης αν ο χρηστης εκανε 3 νικες 
           print("The game is over ")   
           input()
           
           
           
           
           
         

           
           
           
           
           
           
           
