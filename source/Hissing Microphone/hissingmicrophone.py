def solve():
    word = input()
    for i in range(len(word)-1) :
        if(word[i]==word[i+1] and word[i]=='s'):
            print("hiss")
            return 
    print("no hiss")
solve()