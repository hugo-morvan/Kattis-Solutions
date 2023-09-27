while True:
    n = int(input())
    if n == -1:
        break
    
    adj_matrix = [list(map(int, input().split())) for _ in range(n)]
    
    weak_vertices = []
    for i in range(n):
        is_weak = True
        for j in range(n):
            if adj_matrix[i][j] == 1:
                for k in range(n):
                    if adj_matrix[i][k] == 1 and adj_matrix[j][k] == 1:
                        is_weak = False
                        break
                if not is_weak:
                    break
        if is_weak:
            weak_vertices.append(i)
    
    print(*weak_vertices)
