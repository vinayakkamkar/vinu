queue=[]
def enqueue():
    element=input("Enter the number")
    queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop()
        print("removed element is ",e)
def desplay():
    print(queue)
while True:
    print("select the operation 1.add 2.remove 3.show 4.exit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        desplay()
    elif choice==4:
        break
    else:
        print("select the correct option")
    
    
