


def max_sum(arr):
    max = arr[0]
    part_maz = arr[0]

    for i in range(1, len(arr)):
        if part_maz+arr[i] > arr[i]:
            part_maz = part_maz+arr[i]
            if max < part_maz:
                max = part_maz
        else:
            part_maz = arr[i]

    return max

if __name__ == '__main__':
    print(max_sum([-10,2,3,4,-5,6,7,8,-9]))