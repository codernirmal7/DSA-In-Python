class Node :
    def __init__(self  , item=None , next=None):
        self.item = item
        self.next= next


class SinglyLinkedList :
    def __init__(self , start=None) :
        self.start = start

    def is_empty (self) :
        return self.start is None

    def insert_at_first (self , data) :
        if self.is_empty() :
            n = Node(data)
            self.start = n
            return
        
        n = Node(data , self.start)
        self.start = n

    def insert_at_last(self , data) :
        if self.is_empty() :
            self.insert_at_first(data)
            return
        
        temp = self.start
        while temp.next is not None :
            temp = temp.next
        n = Node(data)
        temp.next = n

    def insert_after (self , temp , data) :
        if temp is not None :
            n= Node(data , temp.next)
            temp.next = n
  

    def search (self , data) :
        if self.is_empty() :
           raise IndexError("Out of the range")
        temp = self.start
        while temp is not None :
            if temp.item == data :
                return temp
            temp = temp.next
    
        return None
    
    def traverse (self) :
        temp = self.start 
        while temp is not None :
            print(temp.item , end=" ")
            temp = temp.next

    def delete_first (self) :
        if self.is_empty() :
           raise IndexError("Out of the range")
        
        if self.start.next is None :
            self.start = None
            return

        self.start = self.start.next

    def delete_last (self) :
        if self.is_empty() :
           raise IndexError("Out of the range")
        
        if self.start.next is None :
            self.start = None
            return
        
        temp = self.start
        while temp.next is not None :
            if temp.next.next is None :
                temp.next = None
                return
            temp = temp.next
    
    def delete_item (self , data) :
        if self.is_empty() :
            pass
        elif self.start.next is None :
            if self.start.item == data :
                self.start = None
        else :
            temp = self.start
            if temp.item == data :
                self.start = temp.next
            else :
                while temp.next is not None :
                    if temp.next.item == data :
                        temp.next = temp.next.next
                        break
                    temp = temp.next
    

if __name__ == "__main__" :
    l1 = SinglyLinkedList()
    l1.insert_at_first(1)
    l1.insert_at_last(3)
    l1.insert_after(l1.search(1),2)
    l1.delete_item(2)
    l1.traverse()