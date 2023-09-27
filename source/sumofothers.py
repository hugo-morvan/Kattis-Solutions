while 1:
    try:
        a = list(map(int, input().split()))
        for i in a:
            if i == sum(a) - i:
                print(i)
                break
    except EOFError:
        break