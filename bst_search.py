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
            
    def search(self,node,k1):
        if node is None:
            print("false")
            return 
        else:
            if k1==node.data:
                print("true")
                return
            elif k1<node.data:
                self.search(node.left,k1)
            elif k1>node.data:
                self.search(node.right,k1)
            
   
obj = Main()
n=int(input())
key=list(map(int,input().split()))
k1=int(input())

root=Node(key[0])
for k in key:
    root = obj.build(root,k)
#print("Inorder traversal:")
#obj.printInorder(root)
obj.search(root,k1)
