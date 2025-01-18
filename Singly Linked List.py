class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_at_first(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        print(f"{data} inserted successfully at first position")

    def insert_at_end(self, data):
        if self.head is not None:
            new_node = Node(data, None)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            print(f"{data} inserted successfully at last position")

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
            new_node = Node(data, temp.next)
            temp.next = new_node
            print(f"{data} inserted successfully at given position")

    def insert_at_position(self, position, data):
        if position == 0:
            new_node = Node(data, self.head.next)
            self.head.next = new_node
            print(f"{data} inserted successfully at {position} position")
            return
        else:
            temp = self.head
            for _ in range(position -2):
                if temp is None:
                    print("Invalid position")
                    return
                temp = temp.next
            new_node = Node(data, temp.next)
            temp.next = new_node
            print(f"{data} inserted successfully at {position} position")

    def display_data(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.data, end="-->")
                temp = temp.next

    def delete_at_first(self):
        if self.head is not None:
            temp = self.head
            self.head = temp.next
            print("Data deleted successfully from first position")

    def delete_at_end(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            print("Data deleted successfully from last position")

    def delete_data(self, data):
        if self.head is None:
            pass
        elif self.head.next is None:
            if self.head.data == data:
                self.head = None
                print(f"{data} deleted successfully from given data")
        else:
            temp = self.head
            if temp.data == data:
                self.head = temp.next
            else:
                while temp.next is not None:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
                print(f"{data} deleted successfully from given data")

    def delete_at_position(self, position):
        if self.head is None:
            print("Linked list is empty")

        elif position == 0:
            self.head.next = None
            print(f"Data deleted successfully at {position} position")
            return

        else:
            temp = self.head
            for i in range(position -2):
                if temp is None:
                    print("Invalid position for deletion")
                    return

                temp = temp.next
            temp.next = temp.next.next
            print(f"Data deleted successfully at {position} position")

    def length_of_LList(self):
        if self.head is None:
            return 0

        else:
            temp = self.head
            i = 0
            while temp is not None:
                i += 1
                temp = temp.next
            print(f"Total length of list is {i}")

    def sorted_list(self):
        data = []
        temp = self.head
        while temp is not None:
            data.append(temp.data)
            temp = temp.next
        for i in data:
            print(i, end=" ")
        # for i in sorted(my_list):
        #     print(i, end="-->")

    def max_element(self):
        x = max(my_list)
        print(f"Maximum element in the Linked list is {x}")

    def min_element(self):
        x = min(my_list)
        print(f"Minimum element in the list is {x}")

    def __iter__(self):
        return LLIterator(self.head)


class LLIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

# driven code


my_list = LinkedList()
my_list.insert_at_first(80)
my_list.display_data()
print()
my_list.insert_at_end(40)
my_list.display_data()
print()
my_list.insert_after(my_list.search_data(80), 20)
my_list.display_data()
print()
my_list.insert_after(my_list.search_data(20), 10)
my_list.display_data()
print()
my_list.insert_after(my_list.search_data(10), 35)
my_list.display_data()
print()
my_list.insert_at_position(2, 85)
my_list.display_data()
print()
my_list.length_of_LList()
my_list.sorted_list()
print()
my_list.max_element()
my_list.min_element()
print()
my_list.delete_at_first()
my_list.display_data()
print()
my_list.delete_at_end()
my_list.display_data()
print()
my_list.delete_data(30)
my_list.display_data()
print()
my_list.insert_at_first(2)
my_list.display_data()
print()
my_list.delete_at_position(2)
my_list.display_data()
print()
my_list.insert_after(my_list.search_data(35), 40)
my_list.display_data()
print()
for i in my_list:
    print(i)
print()
my_list.length_of_LList()
