if __name__ == '__main__':
    n = int(input())
    if(n>=1 and n<=20):
        for i in range(0, n):
            print(pow(i,2))
    else:
        print('n should be between 1 and 20')
