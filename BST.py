class Node :
    def __init__(self , item=None , left=None , right=None):
        self.item = item
        self.left = left
        self.right = right


class BST :
    def __init__(self):
        self.root = None
        self.size = 0

    def insert (self , data) :
        self.root = self.rinsert(self.root , data)
        self.size +=1

    def rinsert (self , root , data) :
        if root is None :
            return Node(data)
        
        if data < root.item :
            root.left = self.rinsert(root.left , data)
        elif data > root.item :
            root.right = self.rinsert(root.right, data)

        return root
    
    def search (self , data) :
        return self.rsearch(self.root, data)

    def rsearch (self , root , data) :
        if root is None or root.item == data :
            return root
        
        if data < root.item :
            return self.rsearch(root.left, data)
        else :
            return self.rsearch(root.right , data)
        
    def delete (self , data) :
        self.root = self.rdelete(self.root , data)
        self.size -=1

    def rdelete (self , root , data) :
        if root is None :
            return
        
        if root.left :
            # one child condition
            if root.left.item == data  :
               if root.left.right is None and root.left.left is not None :
                  root.left = root.left.left
               else :
                   if root.left.right is not None and root.left.left is None :
                       root.left = root.left.right

            # No child condition
            if root.left.item == data :
                if root.left.left is None and root.left.right is None :
                    root.left = None

     

        if root.right :
            # One child condition
            if root.right.item == data  :
               if root.right.right is None and root.right.left is not None :
                  root.right = root.right.left
               else :
                   if root.right.right is not None and root.right.left is None :
                      root.right = root.right.right

            # No child condition
            if root.right.item == data :
                if root.right.left is None and root.right.right is None :
                    root.right = None
        
        if root.item == data and root.left is not None and root.right is not None :
            temp = root.left
            if temp.right.right is not None :
               temp = self.rdelete(temp.right , data)
            if temp.right.right is None :
                root.item = temp.right.item
                if temp.left is not None :
                    temp.right = temp.right.left
                else :
                    temp.right = None
        
        if data < root.item :
             self.rdelete(root.left , data)
        else :
             self.rdelete(root.right , data)

        return root
        
    
    def inorder (self) :
        result = []
        self.rinorder(self.root , result)
        return result
    
    def rinorder (self , root , result) :
        if root :
            self.rinorder(root.left , result)
            result.append(root.item)
            self.rinorder(root.right , result)
            result.append(root.item)


    def preorder (self) :
        result = []
        self.rpreorder(self.root , result)
        return result
    
    def rpreorder (self , root , result) :
        if root :
            result.append(root.item)
            self.rpreorder(root.left , result)
            self.rpreorder(root.right , result)

    def postorder (self) :
        result = []
        self.rpostorder(self.root , result)
        return result
    
    def rpostorder (self , root , result) :
        if root :
            result.append(root.item)
            self.rpostorder(root.left , result)
            self.rpostorder(root.right , result)

    def get_size (self) :
        return self.size
    
    def min_value (self , temp) :
        current = temp
        while current.left is not None :
            current = current.left
        return current.item
    
    def max_value (self , temp) :
        current = temp
        while current.right is not None :
            current = current.right
        
        return current.item





b1 = BST()
b1.insert(50)
b1.insert(8)
b1.insert(9)
b1.insert(80)
b1.insert(90)
# b1.insert(50)
# b1.insert(30)
# b1.insert(10)
# b1.insert(40)
# b1.insert(35)
# b1.insert(80)
# b1.insert(70)
# b1.insert(60)
# b1.insert(75)
# b1.insert(74)
# b1.insert(55)
# b1.insert(57)
# b1.insert(100)
# b1.insert(90)
print(b1.preorder())
b1.delete(8)
b1.delete(80)
b1.delete(9)
b1.delete(90)
print(b1.preorder())
print(b1.get_size())