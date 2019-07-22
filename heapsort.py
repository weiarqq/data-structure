

def heap_sort(input_list):

    def heapjust(input_list, parent, length):
        temp = input_list[parent]
        child_index = 2 * parent+1
        while child_index < length:
            if child_index + 1 < length and input_list[child_index] < input_list[child_index+1]:
                child_index += 1

            if temp > input_list[child_index]:
                break

            input_list[parent] = input_list[child_index]
            parent = child_index
            child_index = 2 * child_index + 1
        input_list[parent] = temp
        print(input_list)

    if len(input_list) == 0:
        return input_list
    sorted_list = input_list

    length = len(input_list)

    for i in range(0, length//2)[::-1]:
        print(i)
        heapjust(sorted_list, i, length)

    for j in range(1, length)[::-1]:
        temp = sorted_list[j]
        sorted_list[j] = sorted_list[0]
        sorted_list[0] = temp
        heapjust(sorted_list, 0, j)
        #print('%dth' % (length - j))
        #print(sorted_list)
    return sorted_list


if __name__ == '__main__':
	input_list = [50,123,543,187,49,30,0,2,11,100]
	print("input_list:")
	print(input_list)
	sorted_list = heap_sort(input_list)
	print("sorted_list:")
	print(input_list)
