class Dequeue :
    def __init__(self):
        self.my_list = []
    
    def is_empty (self) :
        return len(self.my_list) == 0
    
    def insert_at_rear (self , data) :
        self.my_list.append(data)

    def insert_at_front (self , data) :
        self.my_list.insert(0 , data)

    def delete_rear (self) :
        if not self.is_empty() :
            self.my_list.pop()

    def delete_front (self) :
        if not self.is_empty() :
            self.my_list.pop(0)

    def get_rear (self) :
        return self.my_list[-1]
    
    def get_front (self) :
        return self.my_list[0]
    

if __name__ == "__main__" :
    d = Dequeue()
    d.insert_at_front(1)
    d.insert_at_front(2)
    d.insert_at_rear(3)
    d.delete_front()
    d.delete_rear()
    print(d.get_front())
    print(d.get_rear())