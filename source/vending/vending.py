states = ["0 cents","10 cents","20 cents","25 cents","30 cents","35 cents","40 cents","45 cents","50 cents or more"]
stateIdx = 0
#Transition table determines the next state based on the current state and the input
#                  d, q, C, D
transitionTable = [[1,3,0,0], # 0 cents
                   [2,5,0,1], # 10 cents
                   [4,7,0,2], # 20 cents
                   [5,8,0,3], # 25 cents
                   [6,8,0,4], # 30 cents
                   [7,8,0,5], # 35 cents
                   [8,8,0,6], # 40 cents
                   [8,8,0,7], # 45 cents
                   [8,8,0,0]] # 50 cents or more
print("Welcome to the vending machine! You need to insert 50 cents or more to get a drink.")
userInput = ""
while True:
    userInput = input("Insert a [d]ime, a [q]uarter, [C]ancel order or request [D]rink or type 'quit' to quit: ")

    if userInput == "d": stateIdx = transitionTable[stateIdx][0] #transition to next state

    elif userInput == "q": stateIdx = transitionTable[stateIdx][1] #transition to next state

    elif userInput == "C":
        print("Order cancelled!")
        stateIdx = transitionTable[stateIdx][2] #transition to next state

    elif userInput == "D":
        print("Enjoy your drink!" if stateIdx == 8 else "You need to insert more money!") 
        stateIdx = transitionTable[stateIdx][3] #transition to next state

    elif userInput == "quit": #quit the program
        print("Goodbye!")
        break

    else: 
        print("Invalid input!") 
    print("Current state: ", states[stateIdx]) 

