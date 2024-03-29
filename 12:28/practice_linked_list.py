class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SiglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    
    def get_data_index(self, data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1
    
    def insert_node_at_index(self, idx, node):
        curn = self.head
        prevn = None
        cur_i = 0

        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        
        else:
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1
    
    def insert_node_at_data(self, data, node):
        index = self.get_data_index(data)
        if 0 <= index:
            self.insert_node_at_index(index, node)
        else:
            return -1
    
    def delete_at_index(self, idx):
        curn_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next

        if idx == 0:
            self.head = nextn
        else:
            while curn_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                curn_i += 1
            if curn_i == idx:
                prevn.next = nextn
            else:
                return -1

    def clear(self):
        self.head = None
    
    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
                curn = curn.next
        print(string)

if __name__ == "__main__":
    sl = SiglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))
    sl.append(Node(5))
    sl.insert_node_at_index(3, Node(4))
    sl.print()
    print(sl.get_data_index(1))
    print(sl.get_data_index(2))
    print(sl.get_data_index(3))
    print(sl.get_data_index(4))
    print(sl.get_data_index(5))
    sl.insert_node_at_data(1, Node(0))
    sl.print()

