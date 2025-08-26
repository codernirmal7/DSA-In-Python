class Heap :
    def _init__ (self) :
        self.heap = []

    def createHeap (self , list1) :
        for e in list1 :
            self.insert(e)

    def insert(self , e) :
        index = len(self.heap)
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex] < e :
            if index == len(self.heap) :
                self.heap.append(self.heap[parentIndex])
            else :
                self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index -1)//2

        if index == len(self.heap) :
            self.heap.append(e)
        else :
            self.heap[index] = e

    def top (self) :
        if len(self.heap) == 0 :
            raise EmptyHeapException()
        return self.heap[0]

    def delete (self) :
        if len(self.heap) == 0 :
            raise EmptyHeapException()
        if len(self.heap) == 1 :
            return self.heap.pop()
        
        max_value = self.heap[0]
        temp = self.heap.pop()
        index = 0
        leftChildIndex = 2*index+1
        rightChildIndex = 2*index+2

        while leftChildIndex < len(self.heap) :
            if rightChildIndex < len(self.heap) :
                if self.heap[leftChildIndex] > self.heap[rightChildIndex] :
                    if self.heap[leftChildIndex] > temp :
                        self.heap[index] = self.heap[leftChildIndex]
                        index = leftChildIndex
                    else :
                        break
                else :
                    if self.heap[rightChildIndex] > temp :
                        self.heap[index] = self.heap[rightChildIndex]
                        index = rightChildIndex
                    else :
                        break
            else :
                if self.heap[leftChildIndex] > temp :
                    self.heap[index] = self.heap[leftChildIndex]
                    index = leftChildIndex
                else :
                    break
            leftChildIndex = 2*index+1
            rightChildIndex = 2*index+2
        self.heap[index] = temp

        return max_value

    def heap_sort (self , list1) :
        self.createHeap(list1)
        list2 = []
        try :
            while True :
                list2.insert(0 , self.delete())
        except EmptyHeapException :
            pass
        return list2

class EmptyHeapException(Exception) :
    def __init__(sel , msg="Empty Heap"):
        sel.msg = msg

    def __str__(self):
        return self.msg
    

if __name__ == "__main" :
    my_list = [32, 56 , 12  , 78 , 43 , 25 , 10 , 80 , 60]
    h = Heap()
    my_list = h.heap_sort(my_list)
    print(my_list)
