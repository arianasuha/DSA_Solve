from base_structure import LinkedList, Node

#Subclass to add the new method
class MoveNodeLinkedList(LinkedList):

    def move_node(self):
        if self.head is None or self.head.next is None:
            return

        temp = self.head
        while temp != None:
            if temp.next.next == None:
                break
            temp = temp.next
        move_node = temp.next
        temp.next = None
        move_node.next = self.head
        self.head = move_node

L1 = MoveNodeLinkedList()

#test case 1
linked_list = L1.make_linked_list("3->8->1->5->7->12")
print("Original List:")
L1.print()
L1.move_node()
print("After move_node():")
L1.print()

#test case 2
linked_list = L1.make_linked_list("1->2->3->4->5")
print("Original List:")
L1.print()
L1.move_node()
print("After move_node():")
L1.print()