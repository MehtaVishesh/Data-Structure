class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
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
            self.head = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
    def prepop(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -=1 
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    
    def set_value(self, index, value):
        temp = self.get(index) 
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepop()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index-1)
        curr = prev.next

        prev.next = curr.next
        curr.next = None
        self.length -= 1
        return curr

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



ll = LinkedList(0)
ll.append(20)
ll.append(40)
ll.append(60)
ll.append(80)
print(ll.insert(5,100))
ll.print_list()


