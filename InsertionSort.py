if __name__ == "__main__" :
    def insertion_sort (list1) :
        for i in range(1 , len(list1)) :
            temp = list1[i]
            j = i-1

            while j >=0 and temp < list1[j] :
                list1[j+1] = list1[j]
                j -=1

            list1[j+1] = temp

    my_list = [25 , 67, 47 , 98 , 24]
    insertion_sort(my_list)
    print(my_list)