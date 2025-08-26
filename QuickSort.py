def quickSort (arr) :
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)


my_list = [4,3,1,8,3,9,2]
print(quickSort(my_list))