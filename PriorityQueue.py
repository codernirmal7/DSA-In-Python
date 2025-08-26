class PriorityQueue :
    def __init__ (self) :
        self.my_list = []
    
    def is_empty (self) :
        return len(self.my_list) == 0
    
    def size (self) :
        return len(self.my_list)
 
    
    def insertion (self , data , priority ) :
        index = 0
        while index < len(self.my_list) and self.my_list[index][1] <= priority :
            index +=1
        self.my_list.insert(index , (data,priority))

    def deletion (self) :
        if self.is_empty() :
            raise IndexError("Priority Queue is empty")
        else :
            self.my_list.pop(0)


if __name__ == "__main__" :
    q1 = PriorityQueue()
    q1.insertion(10,8)
    q1.insertion(5,2)
    q1.insertion(8,0)
    print(q1.my_list)