class node:
    def __init__(self,d):
        self.data=d
        self.next=None   
class main:
    def __init__(self):
        self.head=None
        self.tail=None
        
    #INSERT AT LAST
    def insert(self,d):
        newN=node(d)
        if self.head==None:
            self.head=newN
            self.tail=newN
        else:
            self.tail.next=newN
            self.tail=newN
    #DELETE AT FIRST
    def pop(self):
        if(self.head!=None):
            self.head=self.head.next
 
    def prnt(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
            print("->",end=" ")
obj= main()
n=int(input("Insert:"))        
while(n>0):
    obj.insert(n)
    n=int(input("Input: "))
print('\nList before pop:',)
obj.prnt()

obj.pop()
print('\nList after pop:',)
obj.prnt()