class Block:

    def __init__(self, data):
        self.data = data
        self.nextblock = None

class Node:

    DEFAULT_CAPACITY = 3

    def __init__(self):
        self.blocksize = Node.DEFAULT_CAPACITY
        self.blockhead = None
        self.blockcount = 0
        self.lastblock = None
        self.nextnode = None


class UnrolledLinkedList:

    def __init__(self):
        self.head = None


    def create_node_after(self, current_node):

        new_node = Node()
        current_node.nextnode = new_node

        return new_node


    def shift(self, block, node):

        current_node = node.nextnode
        if current_node is None:

            new_node = Node()
            node.nextnode = new_node
            new_node.blockhead = block
            new_node.lastblock = block
            block.nextblock = None
            new_node.blockcount += 1
            return

        else:

            if current_node.blockhead is None:
                current_node.blockhead = block
                current_node.lastblock = block
                block.nextblock = None
                current_node.blockcount += 1


            else:
                current_blockhead = current_node.blockhead
                current_node.blockhead = block
                current_blockhead.nextblock = block
                block.nextblock = None
                current_node.blockcount += 1

            if current_node.blockcount > current_node.blocksize:

                current_node.blockcount -= 1
                last_block = current_node.lastblock
                prev_block = last_block.nextblock
                current_node.lastblock = prev_block
                self.shift(last_block, current_node)


    def search_node(self, node_position):
        count = 0
        current_node = self.head
        while count <= node_position:
            if current_node is None:
                current_node = Node()
                self.head = current_node
                if count == node_position:
                    return current_node

            else:
                if count < node_position:
                    if current_node.nextnode is None:
                        current_node = self.create_node_after(current_node)

                    else:
                        current_node = current_node.nextnode

                count += 1
        return current_node


    def add_element(self, node_position, element):

        current_node = self.search_node(node_position)

        new_block = Block(element)

        if current_node.blockcount < current_node.blocksize:
            last_block = current_node.lastblock
            new_block.nextblock = last_block
            current_node.lastblock = new_block
            current_node.blockcount += 1
        else:
            last_block = current_node.lastblock
            prev_block = last_block.nextblock
            current_node.lastblock = new_block
            new_block.nextblock = prev_block
            self.shift(last_block, current_node)


    def display(self):
        node = self.head
        while node != None:
            block = node.lastblock
            print(f'Node is {node}')

            while block != None:
                print(f'Elements are: {block.data}')
                block = block.nextblock
            print('---------------------------------------------------')

            node = node.nextnode





ull = UnrolledLinkedList()
ull.add_element(2, 11)
ull.add_element(5, 22)
ull.add_element(0, 33)
ull.add_element(0, 44)
ull.add_element(0, 55)
ull.add_element(0, 66)
ull.add_element(1, 77)
ull.add_element(3, 88)
ull.add_element(3, 99)
ull.display()
