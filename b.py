import random
random_num=random.randint(1,100)
gnum=int(input("enter your guess number: "))
steps=1
while gnum!=random_num :
    if gnum > random_num:
        print("enter lower number: ")
        gnum=int(input("enter your guess number: "))
        steps=steps+1
    else:    
         print("enter higher number: ")
         gnum=int(input("enter your guess number: "))
         steps=steps+1
print("you guessed the number and  your number of steps: " ,steps)        
         
         
         
        
        
    
