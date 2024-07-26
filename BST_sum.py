class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

class Main:  
    def __init__(self):
        self.root = None
    def build(self, n):
        if not n:
            return None
        root = Node(n[0])
        q = [root]
        i = 1
        while len(q) != 0 and i < len(n):
            node = q.pop(0)
            if n[i] != -1:
                node.left = Node(n[i])
                q.append(node.left)
            i += 1
            if i < len(n) and n[i] != -1:
                node.right = Node(n[i])
                q.append(node.right)
            i += 1  
        return root
    def printInorder(self, node, l):
        if node is None:
            return
        else:
            self.printInorder(node.left,l)
            l.append(node.data)
            self.printInorder(node.right,l)
        return l

obj = Main() 

l=[]
n=int(input())
l.append(n)
while(n>0):
    n=int(input())
    if n>0:
        l.append(n)
root = obj.build(l)
k=obj.printInorder(root,l)
print(k)
#print(sum(k))
