class Node :
    def __init__(self , item=None , next=None):
        self.item = item
        self.next = next


class CLL :
    def __init__(self , last=None):
        self.last = last

    def is_empty (self) :
        return self.last is None
    
    def insert_at_start (self , data) :
        if self.is_empty() :
            n = Node(data)
            self.last = n
            n.next = n
            return
        
        n = Node(data , self.last.next)
        self.last.next = n

    def insert_at_last (self  , data) :
        if self.is_empty() :
            n = Node(data)
            self.last = n
            n.next = n
            return
        
        n = Node(data , self.last.next)
        self.last.next = n
        self.last = n

    def insert_after (self , temp , data) :
        if temp is not None :
            if self.last == temp :
                self.insert_at_last(data)
                return
            n = Node(data , temp.next)
            temp.next = n
    def search (self , data) :
        if self.is_empty() :
            return
        
        temp = self.last.next
        while temp != self.last :
            if temp.item == data :
                return temp
            temp = temp.next
        # for last item
        if temp.item == data :
            return temp
    
    def delete_first (self) :
        if self.is_empty() :
            return
        
        if self.last.next is None :
            self.last = None
            return
        
        self.last.next = self.last.next.next

    def delete_last (self) :
        if self.is_empty() :
            return
        if self.last.next is None :
            self.last = None
            return
        
        temp = self.last.next
        while temp.next != self.last :
            temp = temp.next

        temp.next = temp.next.next
        self.last = temp
    
    def delete_item (self , data) :
        if self.is_empty() :
            return
        
        if self.last.next is None and self.last.item == data :
            self.last = None
            return
        
        if self.last.item == data :
            self.delete_last()
            return
        
        if self.last.next.item == data :
            self.delete_first()
            return
        
        temp = self.last.next
        while temp != self.last :
            if temp.next.item == data :
                temp.next = temp.next.next
                break
            temp = temp.next

    def traverse (self) :
        if not self.is_empty() :
            temp = self.last.next
            while temp != self.last :
                print(temp.item , end=" ")
                temp = temp.next
            print(temp.item)

            
if __name__ == "__main__" :
    c = CLL()
    c.insert_at_last(6)
    c.insert_at_last(7)
    # c.insert_at_start(5)
    # c.insert_at_start(4)
    # c.insert_at_start(3)
    c.traverse()