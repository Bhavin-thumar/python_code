class Node:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None


    def create(self, node = None):

        if self.root is None:
            ele = input("Enter root node :")
            node = Node(ele)
            self.root = node

        else:
            ele = node.element

        left_ele = input(f"Enter left node of {ele} : ")

        if left_ele != '-1':

            new_node = Node(left_ele)
            node.left = new_node
            self.create(new_node)

        right_ele = input(f"Enter right node of {ele} :")

        if right_ele != '-1':

            new_node = Node(right_ele)
            node.right = new_node
            self.create(new_node)

    def pre_order(self, root, s = ''):
        if not root:
            return s
        if root:
            s += root.element
            s = self.pre_order(root.left, s)
            s = self.pre_order(root.right, s)

        return s

    def level_order(self, root):
        if not root:
            return

        else:
            stack = []
            queue = []
            queue.append(root)

            while queue:
                node = queue.pop(0)
                stack.append(node.element)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return stack

    def height(self, node):
        if not node:
            return -1

        else:
            h = 1 + max(self.height(node.left), self.height(node.right))
            print(f'Height of {node.element} is :', h)
            return h


    def all_path(self, node=None, s= ''):
        if node:
            s += node.element + '-'
            if not node.right and not node.left:
                print(s)

            self.path(node.left, s)
            self.path(node.right, s)


    def search(self,node=None, element=None, parent=None):
        if node:
            if node.element == element:
                return (node, parent)
            else:
                left = self.search(node.left, element, node)
                if left:
                    return left
                right = self.search(node.right, element, node)
                if right:
                    return right


    def maximum(self, node, maxi=None):
        if node:
            if node is self.root:
                maxi = node.element
            else:
                if node.element > maxi:
                    maxi = node.element

            maxi = self.maximum(node.left, maxi)
            maxi = self.maximum(node.right, maxi)

            return maxi

        else:
            return maxi

    def minimum(self, node, mini=None):
        if node:
            if node is self.root:
                mini = node.element
            else:
                if node.element < mini:
                    mini = node.element

            mini = self.minimum(node.left, mini)
            mini = self.minimum(node.right, mini)

            return mini

        else:
            return mini


    def deepest_node(self, node, cur_level=None, max_level=None,element=None):
        if node:
            if node is self.root:
                cur_level = 0
                max_level = 0
                element = node.element

            else:
                cur_level += 1
                if cur_level > max_level:
                    max_level = cur_level
                    element = node.element


            max_level, element = self.deepest_node(node.left, cur_level, max_level, element)
            max_level, element = self.deepest_node(node.right, cur_level, max_level, element)

            return max_level, element

        else:
            return max_level, element


    def path(self, node, find, s = ''):
        if node is self.root:
            s = node.element
        # else:
        #     s += ',' + node.element
        if node:
            s += ',' + node.element
            if node.element == find:
                return  (s, True)

            else:
                result = self.path(node.left, find, s)
                if result[1]:
                    return (result[0], result[1])

                result = self.path(node.right, find, s)
                if result[1]:
                    return (result[0], result[1])

                return (None, False)

        return (None, False)


    def lca(self, first, second):
        first_path, f = self.path(self.root, first)
        second_path, f = self.path(self.root, second)

        first_path = first_path.split(',')
        second_path = second_path.split(',')

        if len(first_path) < len(second_path):
            first_path, second_path = second_path, first_path

        for i in first_path:
            if i not in second_path:
                return prev
            prev = i


    def lca_2(self, root, alpha, beta):

        if not root:
            return None
        if root.element == alpha or root.element == beta:
            return root

        left = self.lca_2(root.left, alpha, beta)
        right = self.lca_2(root.right, alpha, beta)

        if left and right:
            return root

        else:
            return left if left else right





tree = BinaryTree()
# tree.create()

tree.root = Node('1')
tree.root.left = Node('2')
tree.root.right = Node('3')
tree.root.left.left = Node('4')
tree.root.left.right = Node('5')
tree.root.left.right.left = Node('8')
tree.root.right.left = Node('6')
tree.root.right.right = Node('7')
tree.root.right.left.right = Node('9')
# tree.root.right.left.right.left = Node('10')
# tree.root.right.left.right.left.left = Node('11')
# tree.root.right.left.right.left.left.right = Node('12')

# tree.root = Node('1')
# tree.root.right = Node('3')
# tree.root.right.right = Node('5')

# print(tree.level_order(tree.root))
# tree.all_path(tree.root)
# result = tree.search(tree.root, element='5')
# if result:
#     node,parent = result
#     if node.right:
#         print(f'Right child of Node {node.element} :', node.right.element)
#     if node.left:
#         print(f'left child of Node {node.element} :', node.left.element)
#     if parent:
#         print(f'Parent of Node {node.element} :', parent.element)


# print(tree.minimum(tree.root))

# print(tree.deepest_node(tree.root))

print(tree.lca_2(tree.root, '2', '1').element)
