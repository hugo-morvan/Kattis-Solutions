r, c, zr, zc = map(int, input().split())
lines = [input() for _ in range(r)]

for line in lines:
    new_line = ""
    for char in line:
        new_line += char * zc
    for i in range(zr):
        print(new_line)

