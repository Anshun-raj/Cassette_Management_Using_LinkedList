class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp:
            print("The phase of marriage is",temp.data,end=" ")
            temp=temp.next

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.next

        return print("Total phase is",count)

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                node = Node(data, temp.next)
                temp.next = node
                break

            temp = temp.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        temp = self.head
        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break

            temp = temp.next
            count+=1




obj=LinkedList()


while(True):
    print("There is a cassette of wedding")
    print("The person who want to make a cassette of their marriage wants some modification")
    print("The cassette maker try to organise the phase of marrige")
    print("He wants to organise it in such a way that after completion\nif any correction is required then he can easily do the modification")
    print("press 1 to insert at the beginning phase")
    print("press 2 to insert at any desired phase")
    print("press 3 to insert at the end")
    print("press 4 to remove the phase which is added incorrectly")
    print("press 5 to print total phase in the cassette")
    print("press 6 to print phase sequence at current situation")
    choice = int(input("Enter your choice:-"))
    if(choice==1):
        obj.insert_at_begining("haldi")
    elif(choice==2):
        obj.insert_at(2,"matkor")
    elif (choice == 3):
        obj.insert_at_end("jaymala")
    elif (choice == 4):
        obj.remove_at(2)
    elif(choice==5):
        obj.get_length()
    elif(choice==6):
        obj.printList()
    else:
        print("Invalid input")
        exit()






