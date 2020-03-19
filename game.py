import random
uscore=0
cscore=0
print("welcome to stone|paper|scissor")
while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
    choice = int(input("User turn: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
		
    print("user choice is: " + choice_name) 
   

	
    comp_choice = random.randint(1, 3) 
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
		
    print("I choose: " + comp_choice_name)
    
    if(choice == comp_choice):
       print("That's a tie,no one gets a point,choose again")
      
    elif(choice == 1 and comp_choice == 2):
         print("I win this round ") 
         print("---SCORES---")
         cscore=cscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    elif(choice == 1 and comp_choice == 3):
         print("I lost this round") 
         print("---SCORES---")
         uscore=uscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    elif(choice == 2 and comp_choice == 3): 
         print("I win this round") 
         print("---SCORES---")
         cscore=cscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))	
    elif(choice == 2 and comp_choice == 1): 
         print("I lost this round") 
         print("---SCORES---")
         uscore=uscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    elif(choice == 3 and comp_choice == 1): 
         print("I win this round") 
         print("---SCORES---")
         cscore=cscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    elif(choice == 3 and comp_choice == 2): 
         print("I lost this round") 
         print("---SCORES---")
         uscore=uscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    elif(choice == 1 and comp_choice == 2): 
         print("I win this round") 
         print("---SCORES---")
         cscore=cscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    elif(choice == 2 and comp_choice == 3):
         print("I win this round") 
         print("---SCORES---")
         cscore=cscore+1
         print("user: "+str(uscore))
         print("computer: "+str(cscore))
    if(uscore==5 or cscore==5):
         break
         print("Total score is: ")
         print("user: "+str(uscore))
         print("computer: "+str(cscore))


if(uscore>cscore):
    print("You won the match")
elif(cscore>uscore):
    print("You lost the match")
