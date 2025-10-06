def bubble_sort (arr) :
    n = len(arr)
    for i in range (n-1) :
        is_swapped = False
        for j in range(n-i-1) :
            if arr[j]>arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                is_swapped = True
        if not is_swapped :
            break
    return arr


nums = [2,1,8,5,2,3]
print(bubble_sort(nums))
