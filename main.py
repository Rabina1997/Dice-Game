import random # for generating random nums


valN=input("Enter no of Players: ") #get players count
valM=input("Enter M value: ") # get m value i.e maximum points for winning

n=int(valN)
m=int(valM)
print("No of Players: "+ str(n))
print("Maximum Points: "+ str(m))

dict={} #create dictionary with players and their points
for i in range(n):
    dict[i]=0
    
lowest=0
count=0
won_arr=[] #arr to keep the players who already won
keys=list(dict.keys())  #get keys of dict in list form

previous_val={} #for storing previous round scores
for i in range(n):
    previous_val[i]=0
    
 
#run loop until keys are empty(all players have won) or the lowest valuein dict is >=m   
while lowest<=m or keys:
    
    first_player=random.choice(keys) #choose first player randomly
    
    
    if(count>0):
        print(".........Next Round")
    print("first player : "+"Player "+str(first_player))
    count=count+1
    
    # start round-robin from selected player
    for i in keys[first_player:]: 
        print("Player : "+str(i)+ " is playing now!")
        dice_val=random.choice([1,2,3,4,5,6]) #get random points between 1 to 6
        print("Player "+str(i)+" got a "+str(dice_val))
        
        
        #for continous one's skip the chance
        one=1
        if(dice_val is one and previous_val[i] is one):
            print("You lost this chance!!")
        if((dice_val!=one or previous_val[i]!=one) and dict[i]<m):
            if(i not in won_arr):
                dict[i]=dict.get(i)+ dice_val
                previous_val[i]=dice_val
                
            if(dict[i]>=m): #check if player won
                if(i not in won_arr):
                    won_arr.append(i)
                    keys.remove(i)
                    print("Player "+str(i)+" won!!")
                    
            six=6
            print("Player no : Points")
            print(dict)
            #if player got 6 then give chances until he gets 6
            if(dice_val is six and dict[i]<m):
                while dice_val !=six:
                    print("Wow! You got a 6! You got to roll again!")
                    dice_val2=random.choice([1,2,3,4,5,6])
                    print("Player "+str(i)+" : You got a "+ str(dice_val2))
                    if(i not in won_arr):
                        dict[i]=dict.get(i)+dice_val2
                        previous_val[i]=dice_val2
                    if(dict[i]>=m):
                        if i not in won_arr:
                            won_arr.append(i)
                            keys.remove(i)
                            print("Player "+str(i)+ " won!!")
                            
            print("Previous "+ str(previous_val))
            
            if not keys:
                print("Game Over!!")
                break
            
    for i in keys[:first_player]: # start round-robin from left out players
        print("Player : "+str(i)+ " is playing now!")
        dice_val=random.choice([1,2,3,4,5,6]) #get random points between 1 to 6
        print("Player "+str(i)+" got a "+str(dice_val))
        
        
        #for continous one's skip the chance
        one=1
        if(dice_val is one and previous_val[i] is one):
            print("You lost this chance!!")
        if((dice_val!=one or previous_val[i]!=one) and dict[i]<m):
            if(i not in won_arr):
                dict[i]=dict.get(i)+ dice_val
                previous_val[i]=dice_val
                
            if(dict[i]>=m): #check if player won
                if(i not in won_arr):
                    won_arr.append(i)
                    keys.remove(i)
                    print("Player "+str(i)+" won!!")
                    
            six=6
            print("Player no : Points")
            print(dict)
            #if player got 6 then give chances until he gets 6
            if(dice_val is six and dict[i]<m):
                while dice_val !=six:
                    print("Wow! You got a 6! You got to roll again!")
                    dice_val2=random.choice([1,2,3,4,5,6])
                    print("Player "+str(i)+" : You got a "+ str(dice_val2))
                    if(i not in won_arr):
                        dict[i]=dict.get(i)+dice_val2
                        previous_val[i]=dice_val2
                    if(dict[i]>=m):
                        if i not in won_arr:
                            won_arr.append(i)
                            keys.remove(i)
                            print("Player "+str(i)+ " won!!")
                
    print("Players left in the game : "+str(keys))
    lowest=min(dict.values())
        
    if not keys:
        print("Game Over!!")
        break
        
    

