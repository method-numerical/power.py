"""
improving the previous code....
taking 2**X outside loops . . . .
"""
X=5
L=[]
for i in range(6):
    L.append(2**i)

a=L.index(2**X)    #now out of loop . . . .

if a>-1:
    print('found at',a,'.')
else:
    print('not found . . . .')
