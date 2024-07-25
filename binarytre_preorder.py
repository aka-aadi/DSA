class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    
    return root

def preOrder(root):
    if root:
        print(root.val, end=" ")
        preOrder(root.left)
        preOrder(root.right)

if __name__ == '__main__':
    arr = list(map(int, input( ).split()))
    for i in arr:
            arr.remove(-1)
    n = len(arr)
    
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    preOrder(root)
