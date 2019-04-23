# WA
def main():
    N = int(input())
    S = input()

    bw_cnt = S.count('#.')

    if bw_cnt == 0:
        print(0)
    else:
        black_cnt = S.count('#')
        white_cnt = S.count('.')
        print(min(black_cnt, white_cnt))


if __name__ == '__main__':
    main()
