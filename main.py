a, b = map(int, input().split())
n = a #строки
m = b + 1 #длина строки
e = 1e-6

A = [[] for _ in range(n)]
for _ in A:
    lst = list(map(float, input().split()))
    for i in range(m):
        _.append(lst[i])

#вычисляем ранг матрицы
r1 = 0
for i in range(n):
    tmp = A[i][:(m - 1)]
    if any(abs(ele) > e for ele in tmp):
        r1 += 1

step = 0
for i in range(n - 1):
    step = step or i
    while step < m:
        pivot = A[i][step]
        pivot_row = i
        for j in range(i + 1, n):
            if abs(A[j][step]) > abs(pivot):
                pivot = A[j][step]
                pivot_row = j
        
        #меняем строки, если нужно        
        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            
        #зануляем нижние строки, если pivot не ноль
        if abs(pivot) > e:
            for j in range(i + 1, n):
                factor = A[j][step] / pivot
                for x in range(step, m):
                    A[j][x] -= A[i][x] * factor
            step += 1
            break
        step += 1
    
#вычисляем ранг матрицы после прямого прохода
r2 = 0
zeroes = []
flag = 0

for i in range(n):
    tmp = A[i][:(m - 1)]
    if any(abs(ele) > e for ele in tmp):
        r2 += 1
    else:
        zeroes.append(i)

if len(zeroes):
    for row in zeroes:
        if abs(A[row][-1]) > e:
            print('NO')
            break
    else:
        if (r2 < m - 1):
            print('INF')
        else:
            flag = 1
            
elif r1 == r2 and r1 < (m - 1):
    print('INF')
    
else:
    flag = 1
    
if flag == 1:
    print('YES')
    start = step if step < m - 1 else m - 2
    #обратный ход матрицы
    for x in range(n - 1, 0, -1):
        if abs(A[x][start]) < e:
            continue
        for i in range(x - 1, -1, -1):
            factor = A[i][start] / A[x][start] 
            for j in range(m - 1, start - 1, -1):
                A[i][j] -= A[x][j] * factor
        start -= 1

    #вывод результатов
    res = []
    for i in range(n - len(zeroes)):
        res.append(round((A[i][-1] / A[i][i]), 5))
    print(*res)
