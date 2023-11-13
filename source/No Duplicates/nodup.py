sentence = input().split()
if len(sentence) != len(set(sentence)):
    print("no")
else:
    print("yes")