N = int(input())
for i in range(1,N+1):
    print(" "*(N-i)+"*"*i+"*"*N+"*"*(i-1)+" "*(N-i)+" "*(N-i)+"*"*i+"*"*N+"*"*(i-1)+" "*(N-i))

for i in range(N*3,0,-1):
    print(" "*(N*3-i)+"*"*i+"*"*(i-2))