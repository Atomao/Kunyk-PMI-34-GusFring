import random


def RandomGaussElimination(n, left, right):
    if left > right:
        raise Exception()
    if n > 1000:
        raise Exception()

    a = [[0 for _i in range(n+1)] for _i in range(n)]
    x = [0 for _ in range(n)] 

    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(random.randint(left, right))

    
    for i in range(n):
        if a[i][i] == 0.0:
            raise Exception('Zero division')
            
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i]/a[i][i]

    return x