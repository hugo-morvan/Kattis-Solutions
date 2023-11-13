guess=""
n=int(input())

while(len(guess)<n):

    print(guess+"P",sep="",flush=True)
    answer=input()
    if answer=="0":

        print(guess+"I",sep="",flush=True)
        answer=input()
        if answer=="0":

            print(guess+"Z",sep="",flush=True)
            answer=input()
            if answer=="0":

                guess+="A"
                if len(guess)==n:
                    print(guess,flush=True)
                    break
                else:
                    continue

            elif answer=="1":
                guess+="Z"
                continue
            elif answer=="2":
                break
           
        elif answer=="1":
            guess+="I"
            continue
        elif answer=="2":
            break
    
    elif answer=="1":
        guess+="P"
        continue
    elif answer=="2":
        break
