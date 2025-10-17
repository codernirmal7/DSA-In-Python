def pair_sum_bruteforce (arr , target) :
    n = len(arr)
    pairs = []
    for i in range(n) :
        for j in range(i+1 , n) :
            if arr[i] + arr[j] == target :
                pairs.append((arr[i] ,arr[j]))
    return pairs




def pair_sum_hash (arr , target) :
    seen = set()
    pairs = []
    for num in arr :
        complement = target - num
        if complement in seen :
            pairs.append((complement, num))
        seen.add(num)
    
    return pairs




def pair_sum_twopointer (arr , target) :
    arr.sort()
    pairs = []
    left , right = 0 , len(arr)-1
    while left < right :
        s = arr[left] + arr[right]
        if s == target :
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif s < target :
            left +=1
        else :
            right -=1

    return pairs


if __name__ == "__main__" :
    print(pair_sum_twopointer([2, 7, 11, 15, 4, 5], 9))
    print(pair_sum_hash([2, 7, 11, 15, 4, 5], 9))
    print(pair_sum_bruteforce([2,7,11,15],9))
