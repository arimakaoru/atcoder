# WA
def main():
    N, A, B, C, D = map(int, input().split())
    S = input()
    
    if '##' in S:
        print('No')
        return
    
    if S[B-2] == '#' or S[B] == '#':
        if D != N and S[B-1:D+1].count('...') == 0:
            print('No')
            return
    
    print('Yes')

    
if __name__ == '__main__':
    main()