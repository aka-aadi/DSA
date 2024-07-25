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
    def printInorder(self, node):
        if node is None:
            return
        else:
            self.printInorder(node.left)
            print(node.data, end=" ")
            self.printInorder(node.right)
    def printpreorder(self,node):
        if node is None:
            return
        else:
            print(node.data, end=" ")
            self.printpreorder(node.left)
            self.printpreorder(node.right)
    def printpreorder(self,node):
        if node is None:
            return
        else:
            self.printpreorder(node.left)
            self.printpreorder(node.right)
            print(node.data, end=" ")

obj = Main()      
n = list(map(int, input().split()))
root = obj.build(n)
print("Inorder traversal:")
obj.printInorder(root)
print("\nPreorder traversal:")
obj.printpreorder(root)