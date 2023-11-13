r,f = map(int,input().split())
flips = f//r + (f/r*10%10>=5) 
print("up" if flips%2==0 else "down")
    
