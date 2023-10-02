word=input()
per="PER"*(len(word)//3)
print(sum([1 for i in range(len(word)) if word[i]!=per[i]]))