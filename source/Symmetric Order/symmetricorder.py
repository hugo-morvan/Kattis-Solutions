case_num = 1
while True:
    n = int(input())
    if n == 0:
        break
        
    names = []
    for i in range(n):
        name = input()
        names.append(name)
        
    print(f"SET {case_num}")
    for i in range(n):
        if i % 2 == 0:
            print(names[i])
    for i in range(n-1, -1, -1):
        if i % 2 != 0:
            print(names[i])
    case_num += 1
