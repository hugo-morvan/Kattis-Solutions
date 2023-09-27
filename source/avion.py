c=1
for i in range(5):
 if 'FBI' in input():
  print(i+1,end=' ');c=0
print('HE GOT AWAY!' if c else '')
