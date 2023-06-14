
print("""---------------DICE SIMULATOR------------------""")
import random 

choice=input("Do you want to roll the dice? Y/N \n")
if choice.upper() == "Y":
    choice = True
else:
    choice = False
    print("Simulation finished.")


    
while choice:
    roll=random.randrange(1,7)
    if choice == True:
        print(f"You rolled a {roll}")
    else:
        
        break
    if roll == 1:
        print(""" 
            |------------|
            |            |
            |     0      |
            |            |
            |------------| """)
    elif roll == 2:
        print("""
            |------------|
            |            |
            |   0    0   |
            |            |
            |------------| """)
    elif roll == 3:
        print("""
            |------------|
            |     0      |
            |            |
            |  0     0   |
            |------------| """)
    elif roll == 4:
        print("""
            |------------|
            |   0    0   |
            |            |
            |   0    0   |
            |------------| """)
    elif roll == 5:
        print("""
            |------------|
            |  0     0   |
            |     0      |
            |  0     0   |
            |------------|""") 
    elif roll == 6:
        print("""
            |------------|
            |  0   0   0 |
            |            |
            |  0   0   0 |
            |------------| """)
   

    ch = input("Do you want to roll again? (y/n): ")
    if ch.upper() == "Y":
        choice = True
    else:
        choice = False
        print("Simulation finished.")
          
