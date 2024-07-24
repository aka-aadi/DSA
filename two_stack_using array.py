arr1=[]
capt=1000
top1=0
top2=-1
cap1=1000//2
cap2=-(1000//2)
for i in range(capt):
    arr1.append(None)

l1=int(input())
n=list(map(int,input().split()))
while(l1!=0):
    if arr1[top1+1]==None:
        arr1[top1]=n[top1]
    else:
        print("Stack Overflow")
    top1+=1
    l1-=1
top1-=1

l2=int(input())
k=list(map(int,input().split()))
x=0
while(l2!=0):
    if arr1[top2]==None:
        arr1[top2]=k[x]
    else:
        print("Stack Overflow")
    top2-=1
    l2-=1
    x+=1
top2+=1

pop1=int(input()) #no of pops on stack1
pop2=int(input()) #no of pops on stack2
ctr1=0
ctr2=0
for m in range(0,top1+1):
    ctr1+=1

for n in range(-1,top2-1,-1):
    ctr2+=1

print("Stack 1 Elements: ")
for x in range(top1,-1,-1):
    print(arr1[x],end=" ")

print("\nStack 2 Elements: ")
for y in range(top2,-1+1):
    print(arr1[y],end=" ")

if pop1>ctr1:
    print("\nStack underflow. pop from stack 1 failed")
    
    for a in range(pop1):
        if top1>=0:
            arr1.remove(arr1[top1])
            top1-=1
            ctr1-=1
    #top1=0
print("Stack 1 Elements: ")
for x in range(top1,-1,-1):
    print(arr1[x],end=" ")

if pop2>ctr2:
    print("Stack underflow. pop from stack 1 failed")
else:
    for b in range(pop2):
        arr1.remove(arr1[top2])
        top2+=1
        ctr2-=1

print("\nStack 2 Elements: ")
for y in range(top2,-1+1):
    print(arr1[y],end=" ")

