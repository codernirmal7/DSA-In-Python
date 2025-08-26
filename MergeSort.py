def merge_sort(arr) :
    if len(arr) > 1 :
        mid=len(arr)//2
        leftlist = arr[:mid]
        rightlist = arr[mid:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i < len(leftlist) and j < len(rightlist) :
            if leftlist[i] < rightlist[j] :
                arr[k] = leftlist[i]
                i +=1
            else :
                arr[k] = rightlist[j]
                j+=1
            k +=1

        while i < len(leftlist) :
            arr[k] = leftlist[i]
            i +=1
            k +=1
        
        while j < len(rightlist) :
            arr[k] = rightlist[j]
            j +=1
            k +=1


if __name__ == "__main__" :
    my_list = [2,3,1,4,8,1,4]
    merge_sort(my_list)
    print(my_list)