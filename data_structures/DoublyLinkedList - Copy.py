class DoublyLinkedList:

    class Node:
        def __init__(self, elem = None, next = None, prev = None):
            self.data = elem
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None

    def __init__(self):
        self.header = self.Node()
        self.trailer = self.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_after(self, node, elem): # theta(1)
        prev_node = node
        next_node = node.next

        new_node = self.Node(elem)
        new_node.next = next_node
        new_node.prev = prev_node
        prev_node.next = new_node
        next_node.prev = new_node

        self.size += 1
        return new_node

    def add_first(self, elem): # theta(1)

        return self.add_after(self.header, elem)

    def add_last(self, elem): # theta(1)
        return self.add_after(self.trailer.prev, elem)

    def add_before(self, node, elem): # theta(1)
        return self.add_after(node.prev, elem)

    def delete_node(self, node): # theta(1)
        if(self.is_empty()):
            raise Exception("LinkedList is Empty!!!")

        return_value = node.data
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.disconnect()

        self.size -= 1
        return return_value

    def delete_first(self): # theta(1)

        return self.delete_node(self.header.next)

    def delete_last(self): # theta(1)
        return self.delete_node(self.trailer.prev)


    def __iter__(self):
        cursor = self.header.next
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next


    def __repr__(self):
        #[100 <---> 200 <---> 500]
        return "["+ " <---> ".join([str(each) for each in self])+"]"




def remove_all(doublylinkedlist1, data):
    cursor = doublylinkedlist1.header.next
    while cursor is not doublylinkedlist1.trailer:
        if cursor.data == data:
            next_node = cursor.next
            doublylinkedlist1.delete_node(cursor)
            cursor = next_node

        else:
            cursor = cursor.next

    


# =============================================================================
#
#
# dll = DoublyLinkedList()
# node_1 = dll.add_first(100)
# node_2 = dll.add_after(node_1,200)
# node_3 = dll.add_last(500)
# node_4 = dll.add_after(node_3,200)
# node_5 = dll.add_last(100)
# node_3 = dll.add_last(500)
#
#
# print(dll)
#
# remove_all(dll, 100)
#
# print(dll)
#
#
# =============================================================================
