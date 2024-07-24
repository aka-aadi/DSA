class node:
    def __init__(self,d):
        self.data=d
        self.next=None   
class main:
    def __init__(self):
        self.head=None
        self.tail=None
    
    #INSERT AT FIRST
    def insert(self,d):
        newN=node(d)
        if self.head==None:
            self.head=newN
            self.tail=newN
        else:
            newN.next=self.head
            self.head=newN
    #DELETE AT LAST
    def dele(self):
        temp=self.head
        temp.next=None
        while(temp.next!=None):
            temp=temp.next
 
    def prnt(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
obj= main()
n=int(input("Insert:"))        
while(n>0):
    obj.insert(n)
    n=int(input("Input:"))
obj.prnt()  