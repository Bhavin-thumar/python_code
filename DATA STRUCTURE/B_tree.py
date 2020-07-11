class Node:

    def __init__(self, order):
        self.keys = [None] * order
        self.children = [None] * (order+1)


    def is_overflow(self, order):

        return self.size() >= order


    def is_leaf(self):

        return all(map(lambda x : x is None, self.children))


    def size(self):

        return len([k for k in self.keys if k])


class Btree:

    def __init__(self, order):

        self.root = None
        self.order = order


    def search(self, node, key, parent=None):

        if node.is_leaf():
            return node, parent

        index = 0
        for item in node.keys:
            if item:
                if item < key:
                    index += 1
                else:
                    return self.search(node.children[index], key, node)

            else:
                return self.search(node.children[index], key, node)


    def search_parent(self, node, parent=None):

        if parent is None:
            parent = self.root
            if parent == node:
                return

        for child in parent.children:
            if child:
                if node == parent:
                    return parent
                else:
                    parent = self.search_parent(node, child)

                    if parent:
                        return parent


    def split(self, node):
        median_index = round(node.size()/2) - 1
        median = node.keys[median_index]

        left_split_node, right_split_node = Node(self.order), Node(self.order)

        i = 0
        for key in node.keys[: median_index]:
            if key:
                left_split_node.keys[i] = key
                left_split_node.children[i] = node.children[i]
                i += 1

        left_split_node.children[i] = node.children[i]

        i = 0
        for key in node.keys[median_index+1 : ]:
            if key:
                right_split_node.keys[i] = key
                right_split_node.children[i] = node.children[i + median_index + 1]
                i += 1

        right_split_node.children[i] = node.children[i + median_index + 1]
        node = None

        return median, left_split_node, right_split_node


    def move_up(self, node, parent):

        if node.is_overflow(self.order):
            median, left_split_node, right_split_node = self.split(node)

            if parent is None:
                parent = Node(self.order)
                parent.keys.insert(0, median)
                parent.children[0] = left_split_node
                parent.children[1] = right_split_node
                self.root = parent

                return

            else:
                index = 0
                for k in parent.keys:
                    if not k:
                        parent.keys.insert(index, median)
                        break

                    if k > median:
                        parent.keys.insert(index, median)
                        break
                    index += 1

                parent.children.pop(index)
                parent.children.insert(index, left_split_node)
                parent.children.insert(index+1, right_split_node)

                if parent.is_overflow(self.order):
                    parent_of_parent = self.search_parent(parent)
                    self.move_up(parent, parent_of_parent)

        else:
            return


    def insert(self, key):

        if self.root is None:
            new_node = Node(self.order)
            self.root = new_node

        node, parent = self.search(self.root, key)

        index = 0
        for k in node.keys:
            if not k:
                node.keys.insert(index, key)
                break

            if k > key:
                node.keys.insert(index, key)
                break
            index += 1

        self.move_up(node, parent)


    def print_tree(self, node):

        print(node.keys)
        for child in node.children:
            if child:
                self.print_tree(child)


bt = Btree(4)
bt.insert(5)
# bt.print_tree(bt.root)
bt.insert(3)
# bt.print_tree(bt.root)
bt.insert(21)
# bt.print_tree(bt.root)
bt.insert(9)
bt.insert(1)
bt.insert(13)
bt.insert(2)
bt.insert(7)
bt.insert(10)
bt.insert(12)
bt.insert(4)
bt.insert(8)
bt.print_tree(bt.root)
