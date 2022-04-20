from cgi import print_arguments
from linkedlist import*

def testDetectLoop():
    A,B,C = Node(10),Node(20),Node(30)
    A.next=B
    B.next=C
    C.next=A
    L = LinkedList()
    L.head = A
    assert(L.detectLoop() is True)
    C.next = None
 #   assert(L.detectLoop() is False)
    print(L.traverse())
    print(L.detectLoop())
    


if __name__ == '__main__':
    testDetectLoop()