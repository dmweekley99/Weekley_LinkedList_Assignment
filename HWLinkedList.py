from Node import Node

class HWLinkedList:
    def __init__(self):
        # Initializes the linked list with no nodes (head is None)
        self.head = None

    def __str__(self):
        # Converts the linked list into a string representation
        return self._to_string(self.head)

    def _to_string(self, head):
        # Recursively builds the string representation of the list
        if head is None:
            return ""
        return str(head.data) + "\n" + self._to_string(head.next)

    def add(self, data):
        # Adds a new node to the list
        if self.head is None:
            # If list is empty, set the new node as the head
            self.head = Node(data)
        else:
            # Otherwise, recursively find the end and add the new node
            self._add(self.head, data)

    def _add(self, head, data):
        # Helper function to recursively add a new node to the end
        if head.next is None:
            head.next = Node(data)
        else:
            self._add(head.next, data)

    def addAtHead(self, data):
        # Adds a new node at the beginning of the list
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = Node(data)
        else:
            # Insert new node at the head and push the current head down
            new_node.next = self.head
            self.head = new_node
    
    def searchList(self, node, search):
        # Recursively searches the list for a node with the given data
        if node is None:
            return False
        if node.data == search:
            return True
        return self.searchList(node.next, search)

    def remove(self, head, pred, outdata):
        # Removes a node with the specified data
        if head is None:
            return False
        elif head.data == outdata:
            if pred is None:
                # If the node to be removed is the head, update the head
                self.head = head.next
            else:
                # Otherwise, bypass the current node in the list
                pred.next = head.next
            return True
        else:
            # Recursively search for the node to remove
            return self.remove(head.next, head, outdata)
