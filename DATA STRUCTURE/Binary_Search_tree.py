class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self, data):

        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)


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


    def preorder(self, node, lst=None):
        if lst is None:
            lst = []
        if node:
            lst.append(node.data)
            # print(node.data,'-->',end='\t')
            self.preorder(node.left, lst)
            self.preorder(node.right, lst)

            return lst


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






bst = BinarySearchTree()
bst.insert(8)
bst.insert(5)
bst.insert(10)
bst.insert(3)
bst.insert(6)
bst.insert(9)
bst.insert(12)
bst.insert(1)
bst.insert(4)
bst.insert(7)
bst.insert(8.5)
bst.insert(11)
bst.insert(-1)




# print(bst.preorder(bst.root))
# print(bst.search(bst.root, 7)[1].data)

# print(bst.min_of_right_subtree(bst.root.left).data)

# bst.deletion(9)
print(bst.preorder(bst.root))
