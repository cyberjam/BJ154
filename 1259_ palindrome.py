while True:
    N = input()
    
    if int(N)<=0:
        break
        
    if list(reversed(list(N)))==list(N):
        print("yes")
    else:
        print("no")
    