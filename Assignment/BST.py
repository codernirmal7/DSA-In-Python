class Node :
    def __init__(self ,  item=None , left=None ,right=None):
        self.left = left
        self.item = item
        self.right = right


class BST :
    def __init__(self):
        self.root = None

    def insert (self , data) :
        self.root = self.rinsert(self.root , data)

    def rinsert (self , root , data) :
        if root is None :
            return Node(data)
        
        if data < root.item :
            root.left = self.rinsert(root.left , data)
        elif data > root.item :
            root.right = self.rinsert(root.right, data)

        return root
    
    def search (self , data) :
        return 
    
    def rsearch (self , root , data) :
        if root is None or root.item == data :
            return root
        
        if data < root.item :
            return self.rinsert(root.left , data)
        elif data > root.item : 
            return self.rinsert(root.right , data)
        
    def delete (self , data) :
        self.root = self.rdelete(self.root , data)

    def rdelete (self , root , data) :
        if root is None :
            return
        

        # If No child present

        # For left branch
        if root.left and data == root.left.item :
            if root.left.left is None and root.left.right is None :
                root.left = None

        # For right branch
        elif root.right and data == root.right.item :
            if root.right.right is None and root.right.left is None :
                root.right = None

        # If only One child present

        # For left branch
        if root.left and data == root.left.item :
            if root.left.left is not None and root.left.right is None :
                root.left = root.left.left
            elif root.left.left is  None and root.left.right is not None :
                root.left = root.left.right

        # For right branch
        elif root.right and data == root.right.item :
            if root.right.left is not None and root.right.right is None :
                root.right = root.right.left
            elif root.right.left is  None and root.right.right is not None :
                root.right = root.right.right

        

        # If Both child Present

        # For left branch
        if root.left and data == root.left.item :
            if root.left.left is not None and root.left.right is not None :
                temp = root.left
                while temp.right.right is not None :
                    temp = temp.right
                    
                root.left.item = temp.right.item
                temp.right = None

        # For right branch
        elif root.right and data == root.right.item :
            if root.right.left is not None and root.right.right is not None :
                temp = root.right
                while temp.right.right is not None :
                    temp = temp.right
                    
                root.right.item = temp.right.item
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

    def min_value (self) :
        temp = self.root
        while temp.left is not None :
            temp = temp.left

        print(temp.item)

    def max_value (self) :
        temp = self.root
        while temp.right is not None :
            temp = temp.right

        print(temp.item)
        

if __name__ == "__main__" :
    bst = BST()
    bst.insert(10)
    bst.insert(7)
    bst.insert(8)
    bst.insert(6)
    bst.insert(12)
    bst.insert(11)
    bst.insert(13)
    bst.delete(12)
    bst.min_value()
    bst.max_value()
    
    print(bst.preorder())