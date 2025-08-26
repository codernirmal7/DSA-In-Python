# from array import *

# array1 = array("b" , [1,2,3,4])
# print(array1)
# for i in array1 :
#     print(i)
# array1.append(5)
# print(type(array1))

# questions

# 1. Reversing a list without using reverse built-in method
# def reverseList (_list) :
#     reversedList = []
#     for i in range(len(_list),0,-1) :
#         reversedList.append(i)
#     return reversedList

# print(reverseList([1,2,3,4]))

# 2. Sum of all elements of list

# def sum_of_all_elements (lst) :
#     totalSum = 0
#     for i in lst :
#         totalSum +=i
#     return totalSum

# print(sum_of_all_elements([1,2,3]))

# 3. Find Maximum and Minimum

def find_max_min (lst) :
    lst.sort()
    return lst[0] , lst[-1]
    
print(find_max_min([1,4,9,0]))