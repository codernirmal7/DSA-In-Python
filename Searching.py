def liner_search (list1 , data) :
    for i in list1 :
        if data == i :
            return i
    return None

def binary_search(list1  , data) :
    sorted_list = sorted(list1)
    return binary_r(sorted_list , 0 , len(sorted_list) -1, data)

def binary_r (list1 , start , end  ,data ) :
    m = (start+end) // 2
    if start > end:
       return None

    if list1[m] == data :
        return list1[m]
    elif data < list1[m] :
        return binary_r(list1 , start , m-1 , data)
    else :
        return  binary_r(list1 , m+1 , end , data)

if __name__ == "__main__" :
    my_list = [2,3,4,5,1 , 6]
    # print(liner_search(my_list , 9))
    print(binary_search(my_list , 5))