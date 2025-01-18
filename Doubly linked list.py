class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLL:
    def __init__(self, head=None):
        self.head = head

    def insert_at_first(self, data):
        if self.head is None:
            new_node = Node(None, data, None)
            self.head = new_node
            print(f"{data} inserted successfully at first position")
            return
        else:
            new_node = Node(None, data, self.head)
            self.head = new_node
            print(f"{data} inserted successfully at first position")
            return

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_first(data)

        else:
            temp = self.head
            new_node = Node(temp.prev, data, None)
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            print(f"{data} inserted successfully at end position")
            return

    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_first(data)

        else:
            temp = self.head
            for i in range(position -2):
                if position < 0:
                    print("Invalid position")
                    return

                temp = temp.next
            new_node = Node(temp.prev, data, temp.next)
            temp.next = new_node
            print(f"{data} inserted successfully at {position} position")
            return

    def search_data(self, data):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    return temp
                temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(temp.prev, data, temp.next)
            temp.next = new_node
            print(f"{data} inserted successfully at given position")
            return

    def display(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.data, end='-->')
                temp = temp.next
            return

    def delete_at_first(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            temp.prev = None
            print("Data deleted successfully at first position")
            return

    def delete_at_end(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
            print("Data deleted successfully at end position")

        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            print("Data deleted successfully at end position")


my_list = DoublyLL()
my_list.insert_at_first(10)
my_list.display()
print()
my_list.insert_at_end(40)
my_list.display()
print()
my_list.insert_at_position(2, 20)
my_list.display()
print()
my_list.insert_at_position(3, 30)
my_list.display()
print()
my_list.insert_after(my_list.search_data(30), 35)
my_list.display()
print()
my_list.delete_at_first()
my_list.display()
print()
my_list.delete_at_end()
my_list.display()
print()