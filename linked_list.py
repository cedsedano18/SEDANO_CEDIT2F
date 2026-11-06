# ASSESSMENT 3.2 - LINEAR DATA STRUCTURE
# 2. LINKED LIST
# Name: CED HILLARY M. SEDANO
#
# Based on Assessment 3.1:
# Insert S, E, D, A, N, O at the end, then delete the head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_first_node(self):
        if self.head is None:
            return None

        removed = self.head.data
        self.head = self.head.next
        return removed

    def display(self):
        if self.head is None:
            print("Current Linked List: EMPTY")
            return

        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        print("Current Linked List:", " -> ".join(elements), "-> None")

def main():
    linked_list = LinkedList()

    print("================================")
    print("     LINKED LIST DATA STRUCTURE")
    print("================================")

    print("\nADDING LETTERS AT THE END")
    for letter in ["S", "E", "D", "A", "N", "O"]:
        linked_list.insert_at_end(letter)
        print(f"Inserted: {letter}")
        linked_list.display()

    print("\nREMOVING LETTERS FROM THE BEGINNING")
    while linked_list.head is not None:
        removed = linked_list.delete_first_node()
        print(f"Deleted first node: {removed}")
        linked_list.display()

    print("\nLinked List is now empty.")
    print("Program ended.")

if __name__ == "__main__":
    main()
