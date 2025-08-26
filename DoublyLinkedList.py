class Node :
    def __init__(self , prev=None , item=None , next=None):
        self.prev = prev
        self.item = item
        self.next = next
    
class DLL :
    def __init__(self , start=None):
        self.start = start
    
    def is_empty(self) :
        return self.start == None
    
    def insert_at_start (self, item) :
        n = Node(None, item, self.start)
        if self.start:          
            self.start.prev = n
        self.start = n
        
    
    def insert_at_last (self , item) :
        if self.is_empty():      
            return self.insert_at_start(item)
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = Node(temp, item, None)
    
    def insert_after(self, temp, item):
        if temp is None:
            return
        n = Node(temp, item, temp.next)
        if temp.next:             # if there was a node after temp, patch its prev
            temp.next.prev = n
        temp.next = n

    def insert_before(self, temp, item):
        if temp is None:
            return
        n = Node(temp.prev, item, temp)
        if temp.prev:             # middle/tail case
            temp.prev.next = n
        else:                     # inserting before the first node → update head
            self.start = n
        temp.prev = n

    def search (self , item) :
        temp = self.start
        while temp is not None :
            if temp.item == item :
                return temp
            temp = temp.next

        return None

    def delete_first (self) :
        if self.is_empty () :
            return
        self.start = self.start.next

    def delete_last (self) :
        temp = self.start
        if self.is_empty() :
            pass
        elif self.start.next is None :
            self.start.next = None
        else :
            while temp.next.next is not None :
                temp = temp.next
            temp.next = None

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

    

    def print_list (self) :
        temp = self.start
        while temp is not None :
            # print(f"prev : {temp.prev} , item : {temp.item} , next : {temp.next} , current : {temp}",end=" ")
            print(temp.item,end=" ")
            temp = temp.next
    

class DLLIterator :
    def __init__(self , start):
        self.current = start

    def __iter__ (self) : 
        return self

    def __next__ (self) :
        if not self.current :
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


a = DLL()
a.insert_at_start(10)
a.insert_at_start(20)
a.insert_at_start(40)
a.insert_at_last(50)
a.print_list()