def c(a, b):
    m,n=len(a)+1,len(b)+1
    d=[[0]*n for _ in range(m)]
    for i in range(1,m):
        d[i][0]=i
    for j in range(1, n):
        d[0][j]=j
    for i in range(1, m):
        for j in range(1, n):
            c=0 if a[i-1]==b[j-1] else 1
            d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+c)
    return d,d[-1][-1]


# Use case example
# tableau, distance = c('monceau', 'monsieur')



