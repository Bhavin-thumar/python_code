class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.load = None


class AVL_tree:

    def __init__(self):
        self.root = None


    def height(self, node):
        if not node:
            return -1

        else:
            return 1 + max(self.height(node.left), self.height(node.right))


    def update_load(self, node):
        if node:
            node.load = self.height(node.left) - self.height(node.right)

            self.update_load(node.left)
            self.update_load(node.right)


    def lowest_unbalance_node(self, node, parent=None, lowest=None):
        if node:
            if node.load > 1 or node.load < -1:
                lowest = (node, parent)

            a = self.lowest_unbalance_node(node.left, node)
            if a:
                lowest = a
            b = self.lowest_unbalance_node(node.right, node)
            if b:
                lowest = b

            return lowest


    def sub_tree(self, node):
        unbalance_reason = self.longest_path(node)
        unbalance_reason = unbalance_reason.strip()[:2]

        if unbalance_reason == 'LL':
            a, b, c = node, node.left, node.left.left
            a.left = b.right
            b.right = a
            return b

        elif unbalance_reason == 'RR':
            a, b, c = node, node.right, node.right.right
            a.right = b.left
            b.left = a
            return b

        elif unbalance_reason == 'LR':
            a, b, c = node, node.left, node.left.right
            prev_c_left = c.left
            prev_c_right = c.right
            c.left = a.left
            c.right = a
            b.right = prev_c_left
            a.left = prev_c_right
            return c

        elif unbalance_reason == 'RL':
            a, b, c = node, node.right, node.right.left
            prev_c_left = c.left
            prev_c_right = c.right
            c.left = a
            c.right = a.right
            a.right = prev_c_left
            b.left = prev_c_right
            return c

        else:
            print('Unbalance Reason not found.')



    def _insert(self,curr_node,data):

            if data < curr_node.data:
                if not curr_node.left:
                    curr_node.left = Node(data)

                else:
                    self._insert(curr_node.left, data)

            elif data > curr_node.data:
                if not curr_node.right:
                    curr_node.right = Node(data)

                else:
                    self._insert(curr_node.right, data)

            else:
                print("Data already present.")


    def longest_path(self, node, s = '', direction = ''):
        if node:
            s += direction
            l = self.longest_path(node.left, s, direction='L')
            r = self.longest_path(node.right, s, direction='R')
            if l is None:
                l = ''
            if r is None:
                r = ''

            return max(s, l, r, key=len)


    def insert(self, data):

        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

        self.update_load(self.root)
        result = self.lowest_unbalance_node(self.root)

        if result:
            node, parent = result
            if parent == None:
                self.root = self.sub_tree(node)

            else:

                if parent.left == node:
                    parent.left = self.sub_tree(node)
                else:
                    parent.right = self.sub_tree(node)

            self.update_load(self.root)




    def print_tree(self, node):
        if node:
            a = node.left.data if node.left else None
            b = node.right.data if node.right else None
            print(f'node : {node.data}, node.left : {a}, node.right : {b}')
            self.print_tree(node.left)
            self.print_tree(node.right)

    def search(self, node, search_item, parent=None):
        if node:
            if search_item < node.data:
                result = self.search(node.left, search_item, node)
            elif search_item > node.data:
                result = self.search(node.right, search_item, node)
            elif search_item == node.data:
                return (True, parent)

            return result

        else:
            return (False, None)



    def max_of_left_subtree(self, node, count=0):
        if count == 0:
            count += 1
            result = self.max_of_left_subtree(node.left, count)
            return result

        if node:
            result = self.max_of_left_subtree(node.right, count)
            if result is None:
                return node
            else:
                return result


    def min_of_right_subtree(self, node, count=0):
        if count == 0:
            count += 1
            result = self.min_of_right_subtree(node.right, count)
            return result

        if node:
            result = self.min_of_right_subtree(node.left, count)
            if result is None:
                return node
            else:
                return result

    def _node_exist(self, node):
        return node.right if node.right else node.left

    def deletion(self, item):
        status, parent_node = self.search(self.root, item)
        if parent_node.left.data == item:
            current_node = parent_node.left

        elif parent_node.right.data == item:
            current_node = parent_node.right

        if not current_node.left and not current_node.right:
            if parent_node.left.data == item:
                parent_node.left = None

            elif parent_node.right.data == item:
                parent_node.right = None

            current_node = None
            return

        elif (current_node.left and not current_node.right) or (not current_node.left and current_node.right):
            if parent_node.left.data == item:
                parent_node.left = self._node_exist(current_node)

            elif parent_node.right.data == item:
                parent_node.right = self._node_exist(current_node)

            current_node = None
            return

        elif current_node.left and current_node.right:
            substitute_node = self.max_of_left_subtree(current_node)
            status_2, substitute_node_parent = self.search(self.root, substitute_node.data)

            if not substitute_node.left and not substitute_node.right:
                if substitute_node_parent.left == substitute_node:
                    substitute_node_parent.left = None
                else:
                    substitute_node_parent.right = None

                substitute_node.left = current_node.left
                substitute_node.right = current_node.right
                if parent_node.left == current_node:
                    parent_node.left = substitute_node
                elif parent_node.right == current_node:
                    parent_node.right = substitute_node
                current_node = None

            else:
                substitute_node.right = current_node.right
                if parent_node.left == current_node:
                    parent_node.left = substitute_node
                elif parent_node.right == current_node:
                    parent_node.right = substitute_node
                current_node = None


        self.update_load(self.root)
        result = self.lowest_unbalance_node(self.root)

        if result:
            node, parent = result
            if parent == None:
                self.root = self.sub_tree(node)

            else:

                if parent.left == node:
                    parent.left = self.sub_tree(node)
                else:
                    parent.right = self.sub_tree(node)

            self.update_load(self.root)



avl = AVL_tree()
avl.insert(14)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(17)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(11)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(7)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(53)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(4)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(13)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(12)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(8)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(60)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(19)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(16)
avl.print_tree(avl.root)
print('-----------------------------')
avl.insert(20)
avl.print_tree(avl.root)
print('-----------------------------')
avl.deletion(11)
avl.print_tree(avl.root)
