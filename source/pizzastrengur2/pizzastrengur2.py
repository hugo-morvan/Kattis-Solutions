guess=""
n=int(input())
chunk_size = 1
l="PIZA"
li=0
while True:
    if li==4:li=0
    
    print(guess+l[li]*(chunk_size),sep="",flush=True)
    answer=input()
    
    






