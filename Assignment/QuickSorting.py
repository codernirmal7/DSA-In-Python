def partition (arr , low, high) :
    pivot = arr[high]
    i = low -1
    for j in range(low , high) :
        if arr[j] <= pivot :
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1] ,arr[high] = arr[high],arr[i+1]
    return i+1

def quick_sort_inplace (arr , low ,high) :
    if low < high :
        pi = partition(arr , low , high)
        quick_sort_inplace(arr , low , pi-1)
        quick_sort_inplace(arr , pi+1 , high)
        return arr

nums = [10, 7 , 8  , 9 , 1 , 5 ]
print("Sorted : ", quick_sort_inplace(nums , 0 , len(nums) -1))
