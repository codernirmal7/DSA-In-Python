class Node :
    def __init__(self ,prev=None , item=None , priority=None , next=None):
        self.item = item
        self.priority = priority
        self.next = next
        self.prev = prev


class PriorityQueue :
    def __init__(self):
        self.start = None
        self.___item_count = 0


    def is_empty (self) :
        return self.___item_count == 0
    
    def size (self) :
        return self.___item_count
    

    def ___insert_at_last (self , data , priority) :
        n = Node(item=data , priority=priority)
        if self.is_empty() :
            n.next = n
            n.prev = n
            self.start = n
        else :
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def ___insert_at_first (self , data , priority) :
        n = Node(item=data , priority=priority)
        if self.is_empty() :
            n.next = n
            n.prev = n
        else :
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
    
        self.start = n
       
    def ___insert_after (self , temp, data , priority) :
        if temp is None :
            return
        
        n = Node(temp , data , priority , temp.next)
        temp.next.prev = n
        temp.next = n

    def ___insert_before (self , temp , data , priority ) :
        if temp is None :
            return
        if temp == self.start :
            self.___insert_at_first(data , priority)
        else :
            n = Node(temp.prev , data , priority , temp)
            temp.prev.next = n
            temp.prev = n
            
    
    def ___delete_first (self) :
        if self.start == self.start.prev :
            self.start = None
        else :
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def insert (self , data , priority) :
        if self.is_empty() :
            print("Empty")
            self.___insert_at_first(data , priority)
        else :
            if self.start == self.start.prev :
                if self.start.priority <= priority :
                    self.___insert_after(self.start , data ,priority)
                else :
                    self.___insert_before(self.start , data ,priority)
            else :
                temp = self.start
                while temp != self.start.prev and temp.priority <= priority :
                    temp = temp.next
                
                if temp.priority >= priority :
                    self.___insert_before(temp , data ,priority)
                else :
                    self.___insert_after(temp , data ,priority)
                
        
        self.___item_count +=1

    def delete (self) :
        self.___delete_first()

    def print_items (self) :
        if self.is_empty() :
            print("Priority Queue is empty")
            return
        
        temp = self.start
        print(f"data : {temp.item} , priority : {temp.priority}")
        temp = temp.next
        
        while temp != self.start:
            print(f"data : {temp.item} , priority : {temp.priority}")
            temp = temp.next
        print() 



if __name__ == "__main__" :
    p1 = PriorityQueue()
    p1.insert("Sagar",1)    
    p1.insert("Nirmal" , 2)
    p1.insert("bam" , 3)
    p1.insert("goma" , 4)
    p1.insert("gima" , 5)
    p1.insert("giba" , 1)
    p1.insert("khem" , 3)
    p1.print_items()
    p1.delete()
    print("After delting")
    p1.print_items()