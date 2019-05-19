def main():
    M = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    S = input()

    S1 = S[:2]
    S2 = S[2:4]

    if S1 in M and S2 in M:
        print('AMBIGUOUS')
    elif S1 in M:
        print('MMYY')
    elif S2 in M:
        print('YYMM')
    else:
        print('NA')


if __name__ == '__main__':
    main()