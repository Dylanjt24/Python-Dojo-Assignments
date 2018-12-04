class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node
    
    def printAllValues(self, msg=""):
        runner = self.head
        print("Printing values in the list ---", msg, "---")
        while runner.next != None:
            print(runner.value)
            runner = runner.next
        print(runner.value)
    
    def removeNode(self, val):
        runner = self.head
        if runner.value == val:
            self.head = runner.next
        while runner.next != None:
            if runner.next.value == val:
                runner.next = runner.next.next
            else:
                previous = runner
                runner = runner.next
        if runner.value == val:
            previous.next = None
        
    def length(self):
        runner = self.head
        total = 0
        while runner.next != None:
            total+=1
            runner = runner.next
        return total
    
    def insertNode(self, val, index):
        if index > self.length() + 1:
            print("Index not in range of list")
        node = Node(val)
        current_index = 1
        runner = self.head
        if index == 0:
            node.next = self.head
            self.head = node
        while runner.next != None:
            if current_index == index:
                node.next = runner.next
                runner.next = node
                return
            else:
                runner = runner.next
                current_index += 1
        if current_index == index:
            runner.next = node
            node.next = None
