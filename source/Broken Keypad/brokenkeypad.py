#Get the digit for each decimal number
#for each digit, if it is greater than 7, add corresponding number of 7 to the result

#a, b = map(int, input().split())

#num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#ct_7= [0,0,0,0,0,0,1,1,1,1 ,1 ,1 ,1 ,1 ,1 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,3 ,3 ,3 ,3 ]

#count += (n-7)//10

def count_sevens(n):
    n = str(n)
    count = 0
    while(n):
        pow_ten = len(n)-1
        digit = list(n).pop()
        digit = int(digit)
        if digit >= 7:
            count += 10**pow_ten
        else:
            count += (digit-7)//10 * 10**pow_ten
        n = n[1:]
    return count
print("8:")
print(count_sevens(8))
print("78:")
print(count_sevens(78))
print("77:")
print(count_sevens(77))