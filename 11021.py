input_line = int(input())
for line in range(input_line):
    a,b = map(int, input().split())
    print(f"Case #{line+1}: ", a+b)