

def summ(N):
    lr = [1, 2, 3]
    value = [[0]*N]*(len(lr)-1)
    value[0][0] = 1
    value[0][1] = 2
    value[0][2] = 3
    value[1][0] = 1
    value[1][1] = 2
    value[1][2] = 4
    for i in range(len(lr)-1):
        for j in range(3,N):
            value[i][j] = value[i][j-1]+value[i][j-2]+value[i][j-3]

    return value[1][N-1]

if __name__ == '__main__':
    res = summ(4)
    print(res)

