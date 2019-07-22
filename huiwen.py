

def solution1(arr):

    if len(arr)<2:
        return arr
    max_length = 0
    max_str = ''
    for i in range(len(arr)):
        for j in range(i+1, len(arr)-1):
            if arr[i: j+1] == arr[i: j+1][::-1]:
               if j+1-i>max_length:
                   max_str = arr[i: j+1]
                   max_length = j+1 -i


    return max_str

def solution2(arr):
    length = len(arr)
    if length <= 1:
        return arr
    max_len = 1
    max_ste = arr[0]
    dp = [[False]*length]*length

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] == arr[j] and (i-j <= 2 or dp[j+1][i-1]):
                dp[j][i] = True
                if i-j+1 > max_len:
                    max_len = i-j+1
                    max_ste = arr[j: i+1]
    return max_ste

def solution3(s1, s2):

    maxtir = [[0]*len(s2)]*len(s1)
    max_length = 0
    for i in range(1, len(s1)):
        a=2
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                maxtir[i][j] = maxtir[i-1][j-1]+1
                if maxtir[i][j] > max_length:
                    max_length = maxtir[i][j]
            else:
                maxtir[i][j] = max(maxtir[i-1][j], maxtir[i][j-1])

    return max_length

if __name__ == '__main__':
    print(solution3('basdffdsb', 'casdffdxs'))