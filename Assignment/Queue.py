class Queue :
    def __init__(self):
        self.my_list = []

    def is_empty (self) :
        return len(self.my_list) == 0

    def insert (self , data) :
        self.my_list.append(data)

    def delete (self ) :
        if not self.is_empty() :
            self.my_list.pop(0)

    def getFIFO (self) :
        if not self.is_empty() :
            return self.my_list[0]
        


if __name__ == "__main__" :
    q = Queue()
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)

    print(q.getFIFO())