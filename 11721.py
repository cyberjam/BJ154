line = input()
# print(line[0:10])
last_iter = len(line)//10
print(last_iter)
init_iter = 0
for i in range(1,last_iter+1):
    print(line[init_iter:i*10])
    init_iter=i*10
print(line[init_iter:])