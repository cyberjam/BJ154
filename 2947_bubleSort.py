input_line = input()
str_split = input_line.split()
str2int = map(int,str_split)
arr = list(str2int)
flag = 1

while flag:
    flag = 0
    
    for idx, elem in enumerate(arr[1:]):
        offset = 1

        if arr[idx] > arr[idx + offset]:
            arr[idx], arr[idx + offset] = arr[idx + offset], arr[idx]

            int2str = map(str,arr)
            str_combine = " ".join(int2str)
            print(str_combine)
            flag = 1