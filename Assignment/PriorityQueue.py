class PriorityQueue :
    def __init__(self):
        self.my_list = []

    def insert (self , data , priority) :
        index = 0
        while index < len(self.my_list) and self.my_list[index][1] <= priority :
            index +=1
        self.my_list.insert(index , (data,priority))

    def delete (self) :
        if not self.is_empty() :
            self.my_list.pop(0)


if __name__ == "__main__" :
    p = PriorityQueue()
    p.insert(2,1)
    p.insert(3,2)
    print(p.my_list)