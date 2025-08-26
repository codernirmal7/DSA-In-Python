class Node :
    def __init__(self , prev=None , item=None , next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DoublyLinkedList :
    def __init__(self , start=None):
        self.start = start

    def is_empty (self) :
        return self.start is None

    def insert_at_start (self , data) :
        if self.is_empty() :
            n = Node(item=data)
            self.start = n
            return
        
        n = Node(None , data , self.start)
        self.start.prev = n
        self.start = n
    
    def insert_at_last (self , data) :
        if self.is_empty() :
            self.insert_at_start()
            return
        
        temp = self.start
        while temp.next is not None :
            temp = temp.next

        n = Node(temp , data , None)
        temp.next = n

    def insert_after(self , temp , data) :
        if temp is not None :
            if temp.next is None :
                self.insert_at_last(data)
                return
            n = Node(temp , data , temp.next)
            temp.next.prev = n
            temp.next = n

    def insert_before (self , temp , data) :
        if temp is not None :
            if temp == self.start :
                self.insert_at_start(data)
                return
            n = Node(temp.prev , data , temp)
            temp.prev.next = n
            temp.prev = n

    def delete_first (self) :
        if self.start.next is None :
            self.start = None
            return
        
        self.start.next.prev = None
        self.start = self.start.next

    def delete_last (self) :
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
            return
        
        if self.start.next is None and self.start.item == data :
            self.start = None
            return
        
        temp = self.start
        if temp.item == data :
            self.delete_first()
        while temp.next is not None :
            if temp.next.next is None and temp.next.item == data :
                self.delete_last()
                break
            if temp.next.item == data :
                temp.next.next.prev = temp
                temp.next = temp.next.next
                break
            temp = temp.next

    def traverse (self) :
        temp =self.start
        while temp is not None :
            print(temp.item , end=" ")
            temp = temp.next
        
    def search (self , data) :
        temp = self.start
        while temp is not None :
            if temp.item == data :
                return temp
            temp = temp.next

    
            


if __name__ == "__main__" :
    d = DoublyLinkedList()
    d.insert_at_start(5)
    d.insert_at_start(3)
    d.insert_at_last(7)
    d.insert_before(d.search(7) , 6)
    d.insert_after(d.search(7) ,4)
    d.delete_first()
    d.delete_last()
    d.delete_item(7)
    d.traverse()