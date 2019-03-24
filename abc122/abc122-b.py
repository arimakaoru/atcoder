# AC
input = input()
acgt = ['A', 'C', 'G', 'T']

input_len = len(input)
cnt = 0
max_cnt = 0
for i,s in enumerate(input):
    if s in acgt:
        cnt += 1
    elif cnt > max_cnt:
        max_cnt = cnt
        cnt = 0
    else:
        cnt = 0

    if i == input_len - 1 and cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
        
