class Stack :
    def __init__(self):
         self.my_list = []
    
    def is_empty(self) :
        return len(self.my_list) == 0
    
    def insert(self , data) :
        self.my_list.insert(0 , data)
    
    def pop (self) :
        if not self.is_empty() :
            self.my_list.pop(0)
        
    def get_front (self) :
        if not self.is_empty() :
            print(self.my_list[0])
    
    def get_rear (self):
        if not self.is_empty() :
            print(self.my_list[-1])
            
    def length (self) :
        print(len(self.my_list))
        


    
if __name__ == "__main__" :
    s = Stack()
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.pop()
    s.get_front()
    s.get_rear()
    s.length()