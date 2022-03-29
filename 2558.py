from unittest import result


result = [input() for i in range(2)]
result = map(int, result)
print(sum(result))