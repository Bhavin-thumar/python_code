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
        present_node = new_node

        return present_node


    def shift(self, blk, nod):

        next_node = nod.nextnode
        if next_node is None:

            new_node = Node()
            nod.nextnode = new_node
            new_node.blockhead = blk
            new_node.lastblock = blk
            blk.nextblock = None
            new_node.blockcount += 1
            return

        else:

            if next_node.blockhead is None:
                next_node.blockhead = blk
                next_node.lastblock = blk
                blk.nextblock = None
                next_node.blockcount += 1


            else:
                current_blockhead = next_node.blockhead
                next_node.blockhead = blk
                current_blockhead.nextblock = blk
                blk.nextblock = None
                next_node.blockcount += 1



            if next_node.blockcount > next_node.blocksize:

                next_node.blockcount -= 1
                temp = next_node.lastblock
                prev_block = temp.nextblock
                next_node.lastblock = prev_block
                self.shift(temp, next_node)




    def add_element(self, nod, element):

        if self.head is None:
            new_node = Node()
            self.head = new_node
            new_block = Block(element)
            new_node.blockhead = new_block
            new_node.lastblock = new_block
            new_node.blockcount += 1
            return

        else:
            count = 0
            current_node = self.head
            while count != nod:
                if current_node.nextnode is None:
                    current_node = self.create_node_after(current_node)
                    count += 1
                else:
                    current_node = current_node.nextnode
                    count += 1


        new_block = Block(element)

        if current_node.blockhead is None:

            current_node.blockhead = new_block
            current_node.lastblock = new_block
            current_node.blockcount += 1

        else:
            if current_node.blockcount < current_node.blocksize:
                last_block = current_node.lastblock
                new_block.nextblock = last_block
                current_node.lastblock = new_block
                current_node.blockcount += 1
            else:
                temp = current_node.lastblock
                prev_block = temp.nextblock
                current_node.lastblock = new_block
                new_block.nextblock = prev_block
                self.shift(temp, current_node)


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
ull.add_element(0, 11)
ull.add_element(2, 111)
ull.add_element(5, 22)
ull.add_element(0, 33)
ull.add_element(0, 44)
ull.add_element(0, 55)
ull.add_element(0, 66)
ull.add_element(1, 77)
ull.add_element(3, 88)
ull.add_element(3, 99)
ull.add_element(2, 222)
ull.display()
