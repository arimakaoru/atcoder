n = int(input())
a_list = list(map(int, input().split()))

count = 0
flag = True
while flag:
    for i in range(n):
        if a_list[i] % 2 == 0:
            a_list[i] = a_list[i] // 2
        else:
            flag = False
            break
    if flag:
        count += 1

print(count)
