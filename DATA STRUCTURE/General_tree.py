class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_product_tree():
    electronic = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    phone = TreeNode("Cell Phones")
    tv = TreeNode("Television")

    electronic.add_child(laptop)
    electronic.add_child(phone)
    electronic.add_child(tv)

    mac = TreeNode("Macbook")
    surface = TreeNode("Ms Surface")
    thinkpad = TreeNode("Thinkpad")
    iphone = TreeNode("Iphone")
    gpixel = TreeNode("Google Pixel")
    vivo = TreeNode("Vivo")
    samsung = TreeNode("Samsung")
    lg = TreeNode("LG")

    laptop.add_child(mac)
    laptop.add_child(surface)
    laptop.add_child(thinkpad)

    phone.add_child(iphone)
    phone.add_child(gpixel)
    phone.add_child(vivo)

    tv.add_child(samsung)
    tv.add_child(lg)

    return electronic


root = build_product_tree()
root.print_tree()

