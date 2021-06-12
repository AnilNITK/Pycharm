class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None
class doublyLL:
    def __init__(self):
        self.head=None
    def printl(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data, end='--->')
                n=n.nref
    def printl_prev(self):
        print()
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,end='--->')
                n=n.pref
    def add_begin(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def add_end(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def add_after(self,data,x):
        new_node=Node(data)

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print(x, "is not in the linked list")
            else:
                if n.nref is not None:
                    n.nref.pref = new_node

                new_node.nref = n.nref
                new_node.pref = n
                n.nref=new_node
    def add_before(self,data,x):
        new_node=Node(data)
        if self.head is None:
            print("likned list is empty")
        elif x==self.head.data:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
        else:
            n=self.head
            while n.nref is not None:
                if n.nref.data==x:
                    break
                n=n.nref
            if n.nref is None:
                print(x, "is not in the linked list")
            else:
                n.nref.pref = new_node
                new_node.nref = n.nref
                new_node.pref = n
                n.nref = new_node
    def del_begin(self):
        if self.head is None:
            print("likned list is empty")
        else:
            n=self.head
            n.nref.pref=None
            self.head=n.nref
    def del_end(self):
        if self.head is None:
            print("likned list is empty")
        else:
            n=slef.head
            while n.nref.nref is not None:
                n=n.nref
            n.nref=None
    def del_by_value(self,x):
        n=self.head
        if self.head is None:
            print("likned list is empty")
        elif n.data==x:
            n.nref.pref=None
            self.head=n.nref
        else:
            while n.nref is not None:
                if n.nref.data==x:
                    break
                n=n.nref
            if n.nref is None:
                print(print(x, "is not in the linked list"))
            elif n.nref.nref is None:
                n.nref=None
            else:
                n.nref=n.nref.nref
                n.nref.pref=n
LL2=doublyLL()
LL2.add_begin(12)
LL2.add_begin(132)
LL2.add_end(14)
LL2.add_end(21)
LL2.add_after(132,111)
LL2.add_before(150,12)
LL2.add_before(000,132)
LL2.del_begin()
LL2.del_by_value(21)
LL2.printl()
LL2.printl_prev()

