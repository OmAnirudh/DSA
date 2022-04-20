# def class Node:
#     data,Next 

class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.next = None      # why not self.next = Node 


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    #4:30 pm 
    def detectLoop(self):
        slow = self.head
        fast = self.head
        while(fast.next):
            fast = fast.next.next
            slow = slow.next      
            if (slow ==fast):
                return True

        # return None
    
    def addAtFront(self,data):
        # temp = self.head
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def append(self,data):
        temp = self.head
        if temp:
            # traverse till the last node
            # how to identify last node ?  it won't have a next 
            while (temp.next):
                temp=temp.next
        
        new = Node(data)
        temp.next = new
    
    def deleteNodeAt(self,pos):
        temp = self.head
        
        if not pos:
            self.head = temp.next
            temp = None
            return
        i=0
        while(temp and i!=pos):
            prev=temp
            temp=temp.next
            i+=1
        
        if not temp:
            return
        
        prev.next = temp.next
        temp = None
        return

    
    def deleteNode(self,key):
        temp = self.head

        # when head has the key we have to update the head 
        # 
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None 
                return
        
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if not temp:
            return 
        
        prev.next = temp.next
        temp = None
    
    def traverse(self):
        n=self.head
        s = ''
        while(n.next):   # while(n)  not good
            s+=str(n.data) + "->"
            n=n.next
        s+=str(n.data)
        return s
    
    def traverseBetter(self):
        n,s=self.head,''
        while(n):
            s+= str(n.data) + '->'
            n=n.next
        return s


if __name__=='__main__':
    A,B,C = Node(10),Node(20),Node(30)
    A.next=B
    B.next=C

    L = LinkedList()
    L.head = A

    # print(L.traverse())
    L.append(40)
    print(L.traverse())

    L.addAtFront(5)
    print(L.traverse())
    L.deleteNodeAt(5)
    print(L.traverse())
    