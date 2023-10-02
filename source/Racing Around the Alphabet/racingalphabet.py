STEP_LENGTH = 6.731984257692413

def to_int(x):
    if x == ' ':
        return 26
    elif x == '\'':
        return 27
    else:
        return ord(x) - ord('A')

def shortest_route(a, b):
    if a == b:
        return 0
    _a = to_int(a)
    _b = to_int(b)
    if _b < _a:
        _a, _b = _b, _a
    return min(_b - _a, (28 - _b) + _a)

def run(string):
    length = len(string)
    counter = 0
    for i in range(length - 1):
        counter += shortest_route(string[i], string[i + 1])
    return counter

def read_line():
    line = input().strip()
    return line

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        line = read_line()
        result = run(line)
        output = result * STEP_LENGTH / 15 + len(line)
        print("{:.8f}".format(output))
