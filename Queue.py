l=[]
n=int(input("Length of List: "))
l=list(map(int,input("Elements: ").split()))
print("Input List= ",l)
front=l[0]
rear=l[n-1]

def insert(n):
    l.append(n)
def pop():
    l.remove(l[0])
    front=l[0]
    

insert(9)
print("List after inserting= ",l)

pop()
print("List after poping= ",l)

pop()
print("List after poping= ",l)