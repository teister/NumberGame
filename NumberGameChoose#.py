import random

def game():
    running = True
    #count var to count how many numbers have been entered
    count = 0
    print("Welcome to the number game! You will get a random number from 1-100, and you will have to make sure the list stays in order! Good luck!")
    #how long should the list be?
    amount = input("how long should the list be?")
    
    try:
        amount=int(amount)
    except ValueError:
        print("invalid value! quitting...")
        running = False
    
    if amount < 2:
        print("make sure the value is more than 1! quitting...")
        running = False

    nums = {0: 0,}
    for x in range(1,amount+1):
        nums[x] = ''
    nums[amount + 1] = amount*21

    #tell the user the range of random numbers
    if amount < 10: print("the range of random numbers is from 1 to ",20*amount)
    if amount >= 10: print("the range of random numbers is from 1 to ",50*amount)
    
    #print the 'board' before the game starts, to make it look better.
    print("========================")
    for x in range(1,amount +1): print(x,":")
    print("========================")

    while running:
        #generate the random number, how much its multiplied by is different, to make higher numbers easier.
        if amount <= 10:
            numgen = random.randint(1, 20*amount)
        else:
            numgen = random.randint(1,50*amount)

        print("generated number: ", numgen)
        where = int(input("where to place? "))
        # make sure the selected place is valid
        if not 0 < where < amount+1:
            print("invalid number, please enter a number from 1 to ",amount+1," quitting..." )
            running = False
        elif nums[where] != '':
            print("number already taken! quitting...")
            running = False
        #only run game if selected place is valid
        if running == True:
            print("========================")
            #repeat amount times, every time x+1, if x=selected place, set nums.x to generatednum, print nums.x
            for x in range(1, amount+1):
                if where == x:
                    nums[x] = numgen
                    
                print(x,":",nums[x])
            print("========================")
            #checks if the list is in order
            for x in range(1, amount+1):
                #make not sure nums.x nor nums.x-1 is empty
                if not (nums.get(x-1) == '' or nums.get(x) == ''):
                    #if nums.numx-1 > nums.numx: stop
                    if nums.get(x-1) > nums.get(x):
                        running = False
                #same as before, but - is +, and > is <
                if not(nums.get(x+1) == '' or nums.get(x) == ''):
                    if nums.get(x+1) < nums.get(x):
                        running = False
        #increase the count if a valid number was entered.
        if running == True:
            count +=1
        # check for win
        if int(count) == int(amount):
            print("you won!")
            running = False

    #play again?
    playagain = input("play again?(Y/n)")
    if playagain == "y" or playagain == '':
        print("========================")
        game()


game()
