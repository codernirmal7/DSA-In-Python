class Node :
    def __init__(self , prev=None , item=None , next=None):
        self.prev = prev
        self.item = item
        self.next = next
    

class CircularDoublyLinkedList :
    def __init__(self , start=None):
        self.start = start

    def is_empty (self) :
        return self.start is None
    
    def insert_at_start (self , data ) :
        if self.is_empty() :
            n = Node(item=data)
            n.next = n
            n.prev = n
            self.start = n
            return
        
        n = Node(self.start.prev , data , self.start)
        self.start.prev.next = n
        self.start.prev = n
        self.start = n

    def insert_at_last (self , data) :
        if self.is_empty() :
           self.insert_at_start(data)
           return
        
        n = Node(self.start.prev , data , self.start)
        self.start.prev.next = n
        self.start.prev = n
    
    def insert_after (self , temp , data) :
        if temp is not None :
            if temp == self.start.prev :
                self.insert_at_last(data)
                return
        
            n = Node(temp, data , temp.next)
            temp.next.prev = n
            temp.next = n
    
    def insert_before (self , temp , data ) :
        if temp is not None :
            if temp == self.start :
                self.insert_at_start(data)
                return

            n = Node(temp.prev , data , temp)
            temp.prev.next = n
            temp.prev= n

    def delete_first (self) :
        if self.is_empty() :
            return

        if self.start == self.start.prev :
            self.start = None
            return

        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next

    def delete_last (self) :
        if self.is_empty() :
            return
        
        if self.start == self.start.prev :
            self.start = None
            return

        self.start.prev.prev.next = self.start
        self.start.prev = self.start.prev.prev

    def delete_item (self , data) :
        if self.is_empty() :
            return

        if self.start == self.start.prev :
            if self.start.item == data :
                self.start= None
                return
        
        temp = self.start
        if self.start.item == data :
            self.delete_first()
            return
        temp = self.start.next

        while temp != self.start :
            if temp.item == data :
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                break
            
            temp = temp.next
                
    def traverse (self) :
        if self.is_empty():
            return None

        temp = self.start
        print(temp.item)
        temp = temp.next
        while temp != self.start :
            print(temp.item , end=" ")
            temp = temp.next
    
    def search (self , data) :
        if self.is_empty() :
            return

        temp = self.start 
        if temp.item == data :
            return temp
        temp = temp.next
        while temp != self.start :
            if temp.item == data :
                return temp
            temp = temp.next
    
    

if __name__ == "__main__" :
        d = CircularDoublyLinkedList()
        d.insert_at_start(3)
        d.insert_at_start(2)
        d.insert_at_start(1)
        # d.delete_first()
        # d.delete_last()
        # d.delete_item(2)
        # d.insert_before(d.search(1), 0)
        # d.insert_after(d.search(1), 0)

        d.traverse()