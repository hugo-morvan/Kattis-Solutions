n = int(input())

for i in range(n):
    command = input()
    if command.startswith("Simon says"):
        print(command.replace("Simon says ", ""))
