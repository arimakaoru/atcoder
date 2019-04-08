def main():
    S = input()
    T = ['eraser', 'erase', 'dreamer', 'dream']
    
    for i in T:
        S = S.replace(i, '')

    if S == '':
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()