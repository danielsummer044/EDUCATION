n = int(input('N = '))
mat = [[0] * n for i in range(n)]
st = 1
m = 0

mat[n//2][n//2] = n * n

for v in range(n//2):
    #top horizontal
    for i in range(n-m):
        mat[v][i+v] = st
        st += 1
    #right vertical
    for i in range(v + 1, n - v):
        mat[i][-v-1] = st
        st += 1
    #bottom horizontal
    for i in range(v + 1, n - v):
        mat[-v-1][-i-1] = st
        st += 1
    #left vertical
    for i in range(v + 1, n - (v + 1)):
        mat[-i-1][v] = st
        st += 1
    m += 2

#main
for i in mat:
    print(*i)
