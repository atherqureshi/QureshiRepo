# !/usr/bin/python3
# Remove Dupes with LinkedList
# How to do if Temporary Buffer not allowed?

from Data_structures import Node


def remove_dupes_singly(head):
    """
    Using Doubly LinkedList functionality (using Prev), all in place
    """
    pointer = head
    my_set = set()  # Hash Set
    while(pointer):
        if pointer.val in my_set:
            if pointer.next is None:
                pointer.prev.next = None
                break
            else:
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
        else:
            my_set.add(pointer.val)
        pointer = pointer.next
    return head


def removes_dupes_singly(head):
    """
    Using two pointers to keep track of previous node
    """
    # If LinkedList with only 1 element
    if head.next is None:
        return head
    pointer = head
    my_set = set()
    my_set.add(pointer.val)
    pointer_prev = pointer
    pointer = pointer.next
    while(pointer):
        # Seen this value before
        if pointer.val in my_set:
            # If End of LinkedList
            if pointer.next is None:
                pointer_prev.next = None
                break
            else:
                pointer_prev.next = pointer.next
        # Not seen before
        else:
            my_set.add(pointer.val)
            pointer_prev = pointer
        pointer = pointer.next
    return head


if __name__ == '__main__':
    head = Node(10)
    head.appendToTail(20)
    head.appendToTail(50)  # Dupe
    head.appendToTail(30)
    head.appendToTail(120)
    head.appendToTail(50)  # Dupe
    head.appendToTail(10)
    head.appendToTail(15)
    head.printLinkedList()
    remove_dupes_singly(head)  # Should remove Dupes from LinkedList
    head.printLinkedList()
