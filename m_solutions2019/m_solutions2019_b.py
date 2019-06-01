def main():
    S = input()
    n = 15 - len(S)
    win = S.count('o') + n
    
    if win >= 8:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()