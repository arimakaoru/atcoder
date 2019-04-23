def main():
    S = input()
    odd_cnt = [0,0]
    even_cnt = [0,0]

    for i in range(len(S)):
        if i % 2 == 0 and S[i] == '0':
            even_cnt[0] += 1
        elif i % 2 == 0 and S[i] == '1':
            even_cnt[1] += 1
        elif i % 2 == 1 and S[i] == '0':
            odd_cnt[0] += 1
        elif i % 2 == 1 and S[i] == '1':
            odd_cnt[1] += 1

    if even_cnt[0] + odd_cnt[1] < even_cnt[1] + odd_cnt[0]:
        print(even_cnt[0] + odd_cnt[1])
    else:
        print(even_cnt[1] + odd_cnt[0])


if __name__ == '__main__':
    main()
