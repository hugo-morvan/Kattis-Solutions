#201
testCases = input()
for i in range(int(testCases)): #for each test case

    list = input().split(" ")[1:] #get the list of numbers, ignoring the first number (the number of numbers)
    list = [int(x) for x in list] #convert the list of strings to a list of ints

    for j in range(len(list)-1): #for each number in the list

        if list[j+1] != list[j]+1: #if the next number is not one more than the current number
            print(j+2) #print the index of the next number
            break #stop looping


#
#125
#for _ in[0]*int(input()):
# m=list(map(int,input().split()[1:]))
# print(m.index(next(x for x in m if x!=m[0]+m.index(x)))+1)
