import random
#makes the play again? work
running = True

def game():
    #count var to count how many numbers have been entered
    count = 0
    print("Welcome to the number game! You will get a random number from 1-100, and you will have to make sure the list stays in order! Good luck!")
    running = True

    nums = {'num0':0,'num1': '', 'num2': '', 'num3': '', 'num4': '', 'num5': '','num6':101,}

    #print the 'board' before the game starts, to make it look better.
    print("========================")
    for x in range(1,6): print(x,":")
    print("========================")

    while running:
        #generate the random number
        numgen = random.randint(1, 100)
        print("generated number: ", numgen)
        where = int(input("where to place? "))
        # make sure the selected place is valid
        if not 0 < where < 6:
            print("invalid number, please enter a number from 1 to 5! quitting...")
            running = False
        elif nums[f'num{where}'] != '':
            print("number already taken! quitting...")
            running = False
        #only run game if selected place is valid
        if running == True:
            print("========================")
            #repeat 5 times, every time x+1, if x=selected place, set nums.numx to generatednum, print nums.numx
            for x in range(1, 6):
                if where == x:
                    nums[f'num{x}'] = numgen
                    
                print(x, ":", nums[f'num{x}'])
            print("========================")
            #checks if the list is in order
            for x in range(1, 6):
                #make sure nums.numx nor nums.numx-1 is not empty
                if not (nums[f'num{(x-1)}'] == '' or nums[f'num{x}'] == ''):
                    #if nums.numx-1 > nums.numx: stop
                    if nums[f'num{(x-1)}'] > nums[f'num{x}']:
                        running = False
                #same as before, but - is +, and > is <
                if not(nums[f'num{(x+1)}'] == '' or nums[f'num{x}'] == ''):
                    if nums[f'num{(x+1)}'] < nums[f'num{x}']:
                        running = False
        #increase the count if a valid number was entered.
        if running == True:
            count +=1
        # check for win
        if int(count) == int("5"):
            print("you won!")
            running = False

    #play again?
    playagain = input("play again?(Y/n)")
    if playagain == "y" or playagain == '':
        print("========================")
        game()


game()