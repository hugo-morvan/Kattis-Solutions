knight_chart = [[0,3,2,3,2,3,4,5],
                 [3,2,1,2,3,4,3,4],
                [2,1,4,3,2,3,4,5],
                [3,2,3,2,3,4,3,4],
                [2,3,2,3,4,3,4,5],
                [3,4,3,4,3,4,5,4],
                [4,3,4,3,4,5,4,5],
                [5,4,5,4,5,4,5,6]]

centered_knight_chart = [[6,5,4,5,4,5,4, 5 ,4,5,4,5,4,5,6],
                         [5,4,3,4,3,4,3, 4 ,3,4,3,4,3,4,5],
                         [4,3,2,3,2,3,2, 3 ,2,3,2,3,2,3,4],
                         [5,4,3,4,3,2,3, 2 ,3,2,3,4,3,4,5],
                         [4,3,2,3,4,3,4, 3 ,4,3,4,3,2,3,4],
                         [5,4,3,2,3,4,1, 2 ,1,4,3,2,3,4,5],
                         [4,3,4,3,2,1,2, 3 ,2,1,2,3,4,3,4],
                         [5,4,3,2,3,2,3, 0 ,3,2,3,2,3,4,5],
                         [4,3,4,3,2,1,2, 3 ,2,1,2,3,4,3,4],
                         [5,4,3,2,3,4,1, 2 ,1,4,3,2,3,4,5],
                         [4,3,2,3,4,3,4, 3 ,4,3,4,3,2,3,4],
                         [5,4,3,4,3,2,3, 2 ,3,2,3,4,3,4,5],
                         [4,3,2,3,2,3,2, 3 ,2,3,2,3,2,3,4],
                         [5,4,3,4,3,4,3, 4 ,3,4,3,4,3,4,5],
                         [6,5,4,5,4,5,4, 5 ,4,5,4,5,4,5,6]]

chess_board=[["a1","b1","c1","d1","e1","f1","g1","h1"],
             ["a2","b2","c2","d2","e2","f2","g2","h2"],
             ["a3","b3","c3","d3","e3","f3","g3","h3"],
             ["a4","b4","c4","d4","e4","f4","g4","h4"],
             ["a5","b5","c5","d5","e5","f5","g5","h5"],
             ["a6","b6","c6","d6","e6","f6","g6","h6"],
             ["a7","b7","c7","d7","e7","f7","g7","h7"],
             ["a8","b8","c8","d8","e8","f8","g8","h8"]]

n=int(input())
for i in range(n):
    start = input()
    