def bubbleSort (my_list) :
    sorted_list = []
    count = 0
    while len(sorted_list) < len(my_list) -1 :
        if count == (len(my_list) - len(sorted_list))-1 :
            sorted_list.insert(0,my_list[count])
            count = 0
        

        if len(my_list) -1  == len(sorted_list) :
            sorted_list.insert(0 , my_list[0])
            return sorted_list

        num1 = my_list[count]
        num2 = my_list[count+1]
        if num1 > num2 and num2 not in sorted_list :
            my_list[count] = num2
            my_list[count+1] = num1

        count +=1

my_list = [7,10,4,8,3,5,9,2,1,6]
print(bubbleSort(my_list))