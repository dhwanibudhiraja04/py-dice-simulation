
print("""---------------DICE SIMULATOR------------------""")
import random 
choice = True
die_no= int(input("Enter how many dice you want to roll: "))
list_die=[]
for i in range(0, die_no):
    rand_no= random.randint(1,6)
    list_die.append(rand_no)
     
while choice:
    
    for roll in list_die:
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
        
