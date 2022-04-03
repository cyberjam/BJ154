N = int(input())
for i in range(1,N+1):
    if i == 1:
        print(" "*(N-i)+"*")
    elif i == N:
        print(" "*(N-i)+"*"+"*"*(i-1)+"*"*(i-2)+"*")
    else:
        print(" "*(N-i)+"*"+" "*(i-1)+" "*(i-2)+"*")
