class stack:
    def __init__(self):
        self.s1=[]

class node:
    def __init__(self,d):
        self.data=d
        self.next=None
        
class main:
    def __init__(self):
        self.top=None
        
    def insert(self,d):
        newn=node(d)
        newn.next=self.top
        self.top=newn
    def prin(self):
        temp=self.top
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
obj=main()
n=int(input("Input: "))
while(n>0):
    obj.insert(n)
    n=int(input("Input: "))
obj.prin()
