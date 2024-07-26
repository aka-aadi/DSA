class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

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

    def no_node(self,root):
        if root == None:
            return 0    
        l = self.no_node(root.left)
        r = self.no_node(root.right)
        return l+r+1
    def h(self,root):
        if root == None:
            return 0    
        l = self.h(root.left)
        r = self.h(root.right)
        return max(l,r)+1
    def diameter(self,root): 
        if root == None:
            return 0
        l = self.h(root.left)
        r = self.h(root.right)
        return l+r


obj = Main()    
key=[]
n=int(input()) 
key.append(n)
while(n>0):
    n=int(input())
    key.append(n)
root=Node(key[0])
for k in key:
    root = obj.build(root,k)
print("Diameter of the given binary tree is",obj.diameter(root))