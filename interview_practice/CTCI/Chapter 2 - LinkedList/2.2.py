# !/usr/bin/python3
# 2.2 CTCI Finding Kth element in list

from Data_structures import Node


def kth_element(head, k):
    """
        Function will return value of kth last element of singly LinkedList
        param 1 is the head Node of Singly linkedList
        param 2 is kth last element count
    """
    if k <= 0:
        raise ValueError("K Cannot be 0, or negative")
    kPointer = head
    pointer = head
    # Traverse linkedList k times on pointer var
    # index counter is not used, so it named _ apporpriately
    for _ in range(k):
        if pointer is not None:
            pointer = pointer.next
        else:
            raise ValueError('K is larger than list of elements')
    # Move pointer and kpointer at the same time, till pointer hits the end
    # This means that kPointer will be at the end, at kth from right
    while(pointer is not None):
            pointer = pointer.next
            kPointer = kPointer.next
    return kPointer.val


if __name__ in '__main__':
    head = Node(10)
    head.appendToTail(20, 's')
    head.appendToTail(46, 's')
    head.appendToTail(7654, 's')
    head.printLinkedList()
    print(kth_element(head, 2))
