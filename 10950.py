line_cnt = int(input())
result = [sum(map(int, input().split())) for i in range(line_cnt)]
for elem in result:
    print(elem)
    

