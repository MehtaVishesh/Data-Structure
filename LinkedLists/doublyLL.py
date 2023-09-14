class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__ (self, value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return True

    def pop(self):

        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepop(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < (self.length/2):
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length +=1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepop()
        if index == self.length-1:
            return self.pop()
        
        before = self.get(index-1)
        temp = before.next
        after = temp.next

        temp.next = None
        temp.prev = None
        before.next = after
        after.prev = before

        self.length -=1
        return temp
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

dll = DoublyLinkedList(10)
dll.append(20)
dll.append(30)
dll.append(40)
print(dll.insert(100,4))
dll.print_list()


