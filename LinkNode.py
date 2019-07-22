
class Node():
    def __init__(self, data, p=None):
        self.data = data
        self.next = p


class Link( ):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def add_head(self, val):
        node = Node(val)
        self.head = node
        self.length = 1

    def get(self, index):
        if index <= 0:
            return self.head.data
        node = self.head
        for _ in range(index):
            node = node.next
        return node.data

    def add_tail(self, val):
        if self.is_empty():
            self.add_head(val)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val)
            self.length += 1

    def add_index(self, val, index):
        if index <= 0:
            self.add_head(val)
        else:
            node = self.head
            for _ in range(index-1):
                if node is None:
                    raise Exception('index out of link')
                node = node.next
            old_next = node.next
            node.next = Node(val)
            node.next.next = old_next
        self.length += 1

    def delete_node(self, index):
        if self.is_empty():
            raise Exception('Link is None')
        if index <= 0:
            self.head = self.head.next
        node = self.head
        for _ in range(index-1):
            if node is None:
                raise Exception('index out of link')
            node = node.next
        if node.next is not None:
            node.next = node.next.next
        self.length -= 1

    def search_node(self, item):

        node = self.head
        if node.data == item:
            return 0
        for i in range(self.length-1):
            if node.next.data == item:
                return i+1
            node = node.next
        return -1


if __name__ == '__main__':
    link = Link()
    a = [0, 1,2,3,4,5,6,7]
    for k in a:
        link.add_tail(k)
    print(link.get(0))
    print(link.get(2))
    print(link.get(7))
    link.add_index(66, 6)

    print(link.get(6))
    print(link.get(7))
    link.delete_node(6)
    print(link.get(6))
    print(link.search_node(6))
    print(link.length)
