N = int(input())
dp = list()

if N%5==0:
    elem = int(N/5)
    dp.append(elem)
    # for i in range(elem-1,0,-1):
    #     elem2 = 5*i
    #     elem3 = N-elem2
    #     if elem3%3==0:
    #         dp.append(i+int(elem3/3))

elif N%3==0:
    elem = int(N/3)
    dp.append(elem)
    # for i in range(elem-1,0,-1):
    #     elem2 = 3*i
    #     elem3 = N-elem2
    #     if elem3%5==0:
    #         dp.append(i+int(elem3/5))
else:
    for i in range(N//3):
        q_3 = 3*i
        r = N-q_3
        if r%5==0:
            q_5 = int(r/5)
        result = i+q_5
        dp.append(result)
if len(dp)==0:
    print("-1")
else:
    print(min(dp))