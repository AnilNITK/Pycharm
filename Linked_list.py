class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printl(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=self.head
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print(x,"is not in the linked list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print(x,"is not in the linked list")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
    def del_begin(self):
        if self.head is None :
            print("linked list is empty")
        else:
            self.head=self.head.ref
    def del_end(self):
        if self.head is None :
            print("linked list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def del_by_value(self,x):
        if self.head is None :
            print("linked list is empty")
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print(x,"is not in the linked list")
            else:
                n.ref=n.ref.ref
    def reverse(self):
        n=self.head
        prev=None
        while n is not None:
            next=n.ref
            n.ref=prev
            prev=n.ref
            n=next
        self.head=prev
LL1=Linkedlist()
LL1.add_begin(19)
LL1.add_begin(10)
LL1.add_end(12)
LL1.add_end(21)
LL1.add_begin(11)
LL1.add_after(45,11)
LL1.add_before(122,45)
#LL1.del_begin()
#LL1.del_end()
#LL1.del_by_value(45)
LL1.reverse()
LL1.printl()
