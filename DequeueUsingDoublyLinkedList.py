class Node :
    def __init__(self , prev=None, item=None , next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DEQUEUE :
    def __init__(self):
        self.rear = None
        self.front = None
        self.item_count = 0

    def is_empty(self) :
        return self.item_count == 0
    
    def insert_at_rear(self , data) :
        n = Node(item=data , prev=self.rear)
        if self.is_empty() :
            self.front = n
        else :
            self.rear.next = n
        self.rear = n
        self.item_count +=1

    
    def insert_at_front (self , data) :
        n= Node (item=data , next=self.front)
        if self.is_empty() :
            self.rear = n
        else :
            self.front.prev = n

        self.front = n
        self.item_count +=1

    def delete_rear (self) :
        if self.is_empty() :
            raise IndexError("Dequeue is empty")
        
        if self.rear == self.front :
            self.front = None
            self.rear = None
        else :
            self.rear = self.rear.prev
            self.rear.prev = None

        self.item_count -=1

    
    def delete_front (self) :
        if self.is_empty() :
            raise IndexError("Dqueue is empty")
        
        if self.rear == self.front :
            self.front = None
            self.rear = None
        else :
            self.front = self.front.next
            self.front.prev = None

        self.item_count -=1


    def get_rear (self) :
        if self.is_empty() :
            raise IndexError("Dequeue is empty")
        else :
            return self.rear.item
        

    def get_front (self) :
        if self.is_empty() :
            raise IndexError("Dequeue is empty")
        else :
            return self.front.item
        
    
    def size (self) :
        return self.item_count
    

if __name__ == "__main__" :
    d1 = DEQUEUE()
    d1.insert_at_rear(1)
    d1.insert_at_rear(2)
    d1.insert_at_front(3)
    d1.insert_at_front(4)
    print(f"front value : {d1.get_front()} , rear value : {d1.get_rear()}")
    d1.delete_rear()
    print(f"After dequeued : front value : {d1.get_front()} , rear value : {d1.get_rear()}")