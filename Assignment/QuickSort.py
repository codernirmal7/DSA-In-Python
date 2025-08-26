if __name__ == "__main__" :
    def quickSort (list1) :
        right = len(list1)-1
        left  = 0
        los = 0

        while los != right and los != left :   
            if list1[los] < list1[right] :
                right =-1
            else :
                list1[right] = list1[los] 
                list1[los] = list1[right]
                print("Conditon 1")
                print(list1)
                los = right

            if list1[left] < list1[los] :
                left +=1
            else :
                list1[left] , list1[los] = list1[los] , list1[left]
                los = left

        # return quickSortRecursion(list1 , 0 , len(list1)-1 , 0)

    # def quickSortRecursion (list1 , left , right , los) :
    #     my_list = list1
        
    #     if los == right and los == left :
    #         return my_list
    #     print(my_list)
        
    #     if my_list[los] < my_list[right] :
    #         quickSortRecursion(my_list , left , right-1 , los)
    #     else :
    #         my_list[right] = my_list[los] 
    #         my_list[los] = my_list[right]
    #         los = right

    #     if my_list[left] < my_list[los] :
    #         quickSortRecursion(my_list , left+1, right , los)
    #     else :
    #         my_list[left] , my_list[los] = my_list[los] , my_list[left]
    #         los = left




    my_list = [5,1,4,2,9,3]    
    print(quickSort(my_list))