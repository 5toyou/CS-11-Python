class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Added: {value}")

    def delete(self, value):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted: {value}")
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:
            current.next = current.next.next
            print(f"Deleted: {value}")
        else:
            print("Value not found")

    def sort(self):
        if not self.head or not self.head.next:
            return
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        values.sort()

        self.head = None
        for value in values:
            self.insert(value)
        print("List sorted")

    def merge(self, values):
        for value in values:
            self.insert(value)
        print("Lists merged and sorted")
        self.sort()

    def show(self):
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.next
        else:
            print(None)


def menu():
    print("Add = 1")
    print("Delete = 2")
    print("Sort = 3")
    print("Merge = 4")


linked_list = LinkedList()

while True:
    menu()
    linked_list.show()

    choice = input("Choose func: ")
    match choice:
    
        case "1":
            value = input("What to add: ")
            linked_list.insert(value)

        case "2":
            value = input("What to delete: ")
            linked_list.delete(value)

        case "3":
            linked_list.sort()

        case "4":
            number = int(input("How many to add in merge: "))
            new_values = []
            for _ in range(number):
                new_values.append(input("Enter value: "))
            linked_list.merge(new_values)

        case _:
            break

print("You skipped")
