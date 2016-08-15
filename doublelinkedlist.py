class Node():
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

    def getData(self):
        return self.data

    def setData(self,data):
        self.data=data

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next=next

    def getPrev(self):
        return self.prev

    def setPrev(self,prev):
        self.prev = prev


class DoubleLL(Node):

    def __init__(self):
        self.head=Node()
        self.list_count=0

    def add_end(self,data):
        if self.head.getData()==None:
            node=Node(data)
            self.head=node

        else:
            current=self.head
            while current.getNext()!=None:
                current=current.getNext()
            node = Node(data)
            current.setNext(node)
            node.setPrev(current)
        self.list_count+=1

    def add_front(self,data):
        if self.head.getData() == None:
            node = Node(data)
            self.head = node

        else:
            current = self.head
            while current.getPrev() != None:
                current = current.getPrev()
            node = Node(data)
            current.setPrev(node)
            node.setNext(current)
            self.head=node
        self.list_count += 1

    def add_between(self,data,index):
        if index == 0:
            self.add_front(data)
        elif index == self.list_count-1:
            self.add_end(data)
        elif 0 < index < self.list_count-1:
            current = self.head

            for x in range(index-1):
                current=current.getNext()
            node = Node(data)

            current.getNext().setPrev(node)
            node.setNext(current.getNext())
            current.setNext(node)
            node.setPrev(current)
            self.list_count += 1
        else:
            print("index is out of range")

    def remove_between(self,index):
        if index == 0:
            self.remove_front()
        elif index == self.list_count-1:
            self.remove_end()
        elif 0 < index < self.list_count-1:
            current = self.head
            for x in range(index):
                current = current.getNext()
            current.getNext().setPrev(current.getPrev())
            current.getPrev().setNext(current.getNext())
            self.list_count -= 1
        else:
            print("index is out of range")



    def remove_end(self):
        if self.head.getData()==None:
            print("List is empty")
            return -1

        else:
            current=self.head
            while current.getNext()!=None:
                current=current.getNext()
            current.getPrev().setNext(None)
            current.setPrev(None)
        self.list_count-=1

    def remove_front(self):
        if self.head.getData() == None:
            print("List is empty")
            return -1

        else:
            current = self.head
            self.head = current.getNext()
            self.head.setPrev(None)
            current.setNext(None)


        self.list_count -= 1

    def display(self):
        if self.head.getData() == None:
            print("List is empty")
        else:
            current = self.head
            list=[]
            while current.getNext() != None:
                list.append(current.getData())
                current=current.getNext()
            list.append(current.getData())

            print(list)
    def search(self,value):
        i=[]
        j=0
        current = self.head
        while current.getNext() != None:
            if current.getData()==value:
                i.append(j)
            current = current.getNext()
            j=j+1
        if current.getData() == value:
            i.append(j)

        if not i:
            print ("value not found")
        else:
            print("%d found at position(s) %s" % (value, i))
    def size(self):
        print("Size of the list is %d" %self.list_count)

class Operations(DoubleLL):
    list = DoubleLL()
    while True:
        print("\n1.ADD at Front       4.REMOVE at Front       7.SEARCH\n2.ADD at End         5.REMOVE at End         8.DISPLAY\n"
              "3.ADD in Between     6.REMOVE in Between     9.SIZE 0.To EXIT\n")

        try:
            x=int(input ("Select the operation to perform\n"))
        except ValueError:
            print("Enter a number between 1 to 8 only")

        if (x==1):
            list.add_front(int(input("Enter data to Add: ")))
        elif(x==2):
            list.add_end(int(input("Enter data to Add: ")))
        elif (x==3):
            list.add_between(int(input("enter data to Add:")),int(input("Enter Index: ")))
        elif(x==4):
            list.remove_front()
        elif(x==5):
            list.remove_end()
        elif(x==6):
            list.remove_between(int(input("Enter Index: ")))
        elif(x==7):
            list.search(int(input("Enter Value to search: ")))
        elif(x==8):
            list.display()
        elif(x==9):
            list.size()
        elif(x==0):
            exit()
        else:
            print("Enter a number between 1 to 8 only")









