# Monty Hall Paradox 
# Interview Question For Achronix
#
# By Bryant Tran

#import statements
import random

#variables to keep track of the win count
switch_win, keep_win = 0, 0
#variables to keep track of total count
switch_total, keep_total = 0, 0

#function used to check if user input if an int
def checkInput(input):
    try:
        int(input)
        if(1 <= int(input) <= 1000000):
            return True
        else:
            return False
    except ValueError:
        return False

#ask the user for the number of simulations to do
num_of_iterations = input("Enter the number of simulations to perform: ")
while(not checkInput(num_of_iterations)):
    print(num_of_iterations, "is not a valid input")
    num_of_iterations = input("Please enter a valid integer between 1 and 1000000: ")    

#for loop to run simulation num of times defined by user
for i in range(int(num_of_iterations)):
    #randomize the car location
    car_loc = random.randint(1,3)
    if(car_loc == 1):
        door_1, door_2, door_3 = "car", "goat", "goat"
    elif(car_loc == 2):
        door_1, door_2, door_3 = "goat", "car", "goat"
    else:
        door_1, door_2, door_3 = "goat", "goat", "car"

    #pick a random door
    door_picked = random.randint(1,3)

    #switching or keeping will be based on mod 2 of loop num to have even amount of both
    #switch when switch is true
    #keep when switch is false
    switch = (i % 2 == 0)

    #door 1 picked
    if(door_picked == 1):
        #keep door 1
        if(not switch):
            final_door = door_1
        #door 2 shown so switch to door 3
        elif(door_2 == "goat"):
            final_door = door_3
        #door 3 shown so switch to door 2
        else:
            final_door = door_2
    #door 2 picked
    elif(door_picked == 2):
        #keep door 2
        if(not switch):
            final_door = door_2
        #door 1 shown so switch to door 3
        elif(door_1 == "goat"):
            final_door = door_3
        #door 3 shown so switch to door 1
        else:
            final_door = door_1
    #door 3 picked
    else:
        #keep door 3
        if(not switch):
            final_door = door_3
        #door 1 shown so switch to door 2
        elif(door_1 == "goat"):
            final_door = door_2
        #door 2 shown so switch to door 1
        else:
            final_door = door_1

    #add to counters
    if(switch):
        switch_total += 1
        if(final_door == "car"):
            switch_win += 1    
    else:
        keep_total += 1
        if(final_door == "car"):
            keep_win += 1

print("Won ", switch_win, " times out of ", switch_total, " times when switching")
print("Won ", keep_win, " times out of ", keep_total, " times when keeping")
