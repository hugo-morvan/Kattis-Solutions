#134
# h,k,v,s=map(int,input().split());d=0
# while h:
#  v+=s;v-=max(1,v//10)
#  h+=(-1)**(v<k);v*=h!=0
#  if v<=0:h=v=0
#  d+=v;s-=s>0
# print(d)


h,k,v,s=map(int,input().split());d=0
while h:v+=s;v-=max(1,v//10);h+=(-1)**(v<k);v*=h!=0;h*=v>0;d+=v;s-=s>0
print(d)

