# s=3
# y=int(input())-2018
# monthsRange = [12*y, 12*(y+1)]
# while s < monthsRange[0]:
#     s += 26
# if s > monthsRange[1]:
#     print("no")
# else:
#     print("yes")

#55
# print(["no","yes"][(((int(input())-2018)*12)+8)%26<12])

#48
# print(((12*(int(input())+2))%26<12)*"yes"or"no")

#46
# print(((6*(int(input())+2))%13<6)*"yes"or"no")

#45
# print('yneos'[(6*(int(input())+2))%13>=6::2])

# #45
# print('nyoe s'[(6*(int(input())+2))%13<6::2])

# #44
# print(['no','yes'][6*(int(input())+2)%13<6])

# #41
# print('nyoe s'[0<6*int(input())%13<7::2])

# print(['no','yes'][0<6*int(input())%13<7])

# print((0<6*int(input())%13<7)*"yes"or"no")

# print('yneos'[6*int(input())%13>7::2])


print('nyoe s'[0<int(input())%13<7::2])