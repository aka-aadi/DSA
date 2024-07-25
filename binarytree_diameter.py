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
        
        self.root = root
        return root
        
    def height(self, root):
        if root is None:
            return 0
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return max(l_height, r_height) + 1
    
    def diameter(self, root):
        if root is None:
            return 0
        
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        
        l_diameter = self.diameter(root.left)
        r_diameter = self.diameter(root.right)
        
        return max(l_height + r_height + 1, max(l_diameter, r_diameter))


obj = Main()      
n = list(map(int, input().split()))
root = obj.build(n)
print(obj.diameter(root))
