class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def make_linked_list(self, data_list):
        data_list = data_list.split("->")
        self.head = Node(data_list[0])
        temp = self.head
        for i in range(1, len(data_list)):
            node = Node(data_list[i])
            temp.next = node
            temp = node
        return self.head

    def len_of_linked_list(self):
        if self.head is None:
            return 0
        count = 0
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def print(self):
        if self.head is None:
            print("There is no element in the linked list.")
            return
        temp = self.head
        while temp != None:
            print(temp.data, "->", end = " ")
            temp = temp.next
        print()
