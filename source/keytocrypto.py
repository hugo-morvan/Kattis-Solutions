n=input;a=""
m,k=n(),n()
for i in range(len(m)):a+=chr((ord(m[i])-ord(k[i])+26)%26+65);k+=a[-1]
print(a)
