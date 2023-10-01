SCORE=[[10,2,-5,-4],
       [2,12,-9,-3],
       [-4,-2,8,-5],
       [-7,2,2,12]]
score_dict = {'A':0, 'C':1, 'T':2, 'G':3,'X':-1}
SKIP = -5
DEL = -4
INF = -10**5
gene = input("Enter the gene: ")+" "
print('---------------------------')
frag = input("Enter the fragment: ")+" "
print('---------------------------')

table = [[INF for _ in range(len(gene))] for _ in range(len(frag)+1)]
for i in range(len(gene)):
    table[0][i] = 0
for i in range(len(frag)+1):
    table[i][0] = i*DEL

def print_table(table):
    print([let for let in gene])
    for i in range(len(frag)):
        print(frag[i], table[i])


for col in range(1,len(gene)):
    for row in range(1,len(frag)):
        match = INF
        delete = INF
        skip = INF
        
        
        gene_let_num = score_dict[gene[col-1]]
        frag_let_num = score_dict[frag[row-1]]
        match = table[row-1][col-1]+ SCORE[frag_let_num][gene_let_num]
        delete =  table[row-1][col] + DEL
        skip = table[row][col-1] + SKIP
            
        table[row][col] = max(match, delete, skip)
print_table(table)