class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Main:  
    def __init__(self):
        self.root = None
        
    def build(self,root,key):
        self.root=None
        if root==None:
            root=Node(key)
            return root
        elif (key<root.data):
            root.left=self.build(root.left,key)
        elif (key>root.data):
            root.right=self.build(root.right,key)
        return root
        
    def printInorder(self, node):
        if node is None:
            return
        else:
            self.printInorder(node.left)
            print(node.data, end=" ")
            self.printInorder(node.right)
   

obj = Main()      
key = list(map(int, input().split()))
root=Node(key[0])
for k in key:
    root = obj.build(root,k)
print("Inorder traversal:")
obj.printInorder(root)
