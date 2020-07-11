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


    def print_tree(self, arg):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if self.get_level() <= arg:
            print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(arg)



def build_world_tree():
    glob = TreeNode("Global")

    india = TreeNode("India")
    usa = TreeNode("USA")

    glob.add_child(india)
    glob.add_child(usa)

    gujarat = TreeNode("Gujarat")
    karnatak = TreeNode("Karnatak")
    newjersey = TreeNode("New Jersey")
    california = TreeNode("California")
    ahmedabad = TreeNode("Ahmedabad")
    baroda = TreeNode("Baroda")
    benguluru = TreeNode("Bengulur")
    mysore = TreeNode("Mysore")
    princeton = TreeNode("Princeton")
    trenton = TreeNode("Trenton")
    sanfransisco = TreeNode("San Fransisco")
    mountainview = TreeNode("Mountain View")

    india.add_child(gujarat)
    india.add_child(karnatak)
    usa.add_child(newjersey)
    usa.add_child(california)
    gujarat.add_child(baroda)
    gujarat.add_child(ahmedabad)
    karnatak.add_child(benguluru)
    karnatak.add_child(mysore)
    newjersey.add_child(princeton)
    newjersey.add_child(trenton)
    california.add_child(sanfransisco)
    california.add_child(mountainview)

    return glob


root = build_world_tree()
root.print_tree(2)
