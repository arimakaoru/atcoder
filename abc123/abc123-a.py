def main():
    antenna = [0] * 5
    for i in range(5):
        antenna[i] = int(input())
    k = int(input())

    for i in range(5):
        for j in range(i+1, 5):
            if antenna[j] - antenna[i] > k:
                print(':(')
                return
    
    print('Yay!')


if __name__ == '__main__':
    main()