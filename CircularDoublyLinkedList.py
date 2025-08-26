class Node :
    def __init__(self , prev=None , item=None , next=None):
        self.prev = prev
        self.item = item
        self.next = next


class CDLL :
    def __init__(self , start=None):
        self.start = start
    
    def is_empty (self) :
        return self.start is None
    
    def insert_at_start (self , data) :
        n = Node(item=data)
        if self.is_empty() :
            n.prev = n
            n.next = n
            self.start = n
        else :
            n.prev = self.start.prev
            n.next = self.start
            if self.start == self.start.next :
                self.start.next = n
            else :
                self.start.prev.next = n
            self.start.prev = n
            self.start = n

    def insert_at_last (self , data) :
        if self.is_empty() :
            self.insert_at_start(data)
        else :
            n = Node (self.start.prev , data , self.start)
            if self.start == self.start.next :
                self.start.next = n
            else :
                self.start.prev.next = n
            self.start.prev = n
            

    def search (self , data) :
        if self.is_empty() :
            return None
        
        temp = self.start
        if temp.item == data :
            return temp
        temp = temp.next
        while temp != self.start :
            if temp.item == data :
                return temp
            temp = temp.next

        return None
        
    def insert_after (self , temp , data) :
        if temp is not None :
            n= Node(temp , data , temp.next)
            temp.next.prev = n
            temp.next = n
    
    def insert_before (self , temp , data) :
        if temp is not None :
            if temp == self.start :
                self.insert_at_start(data)
            else :
                n = Node(temp.prev , data , temp)
                temp.prev.next = n
                temp.prev = n


    def delete_first (self) :
        if not self.is_empty() :
            if self.start == self.start.next :
                self.start = None
            else :
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next

    def delete_last (self) :
        if not self.is_empty() :
            if self.start == self.start.next :
                self.start = None
            else :
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    
    def delete_item (self , data) :
        if self.is_empty() :
            return
        if self.start.item == data:
            self.delete_first()
            return
        temp = self.start.next
        while temp !=  self.start :
            if temp.item == data :
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            temp = temp.next

            
    def print_list (self) :
        if self.is_empty() :
            print("List is empty")
            return
        
        temp = self.start
        print(temp.item, end=" ")
        temp = temp.next
        
        while temp != self.start:
            print(temp.item, end=" ")
            temp = temp.next
        print() 

    def __iter__ (self) :
        if self.start == None :
           return CDLLIterator(None)
        else :
            return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.first_iteration = True

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        if not self.first_iteration and self.current == self.start:
            raise StopIteration
        
        data = self.current.item
        self.current = self.current.next
        self.first_iteration = False
        return data
    

if __name__ == "__main__":
    list1 = CDLL()
    
    # Test insertions
    list1.insert_at_last(1)
    list1.insert_at_last(10)
    list1.insert_at_start(3)
    list1.insert_at_start(4)
    list1.insert_at_start(5)
    
    print("After initial insertions:")
    list1.print_list()  # Should print: 5 4 3 1 10
    
    # Test insert_after
    node_10 = list1.search(10)
    if node_10:
        list1.insert_after(node_10, 11)
    
    print("After inserting 11 after 10:")
    list1.print_list()  # Should print: 5 4 3 1 10 11
    
    # Test insert_before
    node_10 = list1.search(10)
    if node_10:
        list1.insert_before(node_10, 9)
    
    print("After inserting 9 before 10:")
    list1.print_list()  # Should print: 5 4 3 1 9 10 11
    
    # Test iterator
    print("Using iterator:")
    for item in list1:
        print(item, end=" ")
    print()
    
    # Test deletions
    list1.delete_first()
    print("After deleting first:")
    list1.print_list()  # Should print: 4 3 1 9 10 11
    
    list1.delete_last()
    print("After deleting last:")
    list1.print_list()  # Should print: 4 3 1 9 10
    
    list1.delete_item(9)
    print("After deleting item 9:")
    list1.print_list()  # Should print: 4 3 1 10