def bubble_sort(data_list) :
    for r in range(1 , len(data_list)) :
        for i in range(len(data_list)-r) :
            if data_list[i] > data_list[i+1] :
                data_list[i] , data_list[i+1] = data_list[i+1] , data_list[i]

def modified_bubble_sort(data_list) :
    flag= False
    for r in range(1 , len(data_list)) :
        flag = False
        for i in range(len(data_list)-r) :
            if data_list[i] > data_list[i+1] :
                data_list[i] , data_list[i+1] = data_list[i+1] , data_list[i]
                flag = True

        if not flag :
            True




if __name__ == "__main__" :
    l = [5,1,4,8,3,9,2]
    # bubble_sort(l)
    modified_bubble_sort(l)
    print(l)