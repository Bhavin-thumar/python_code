class ManagementTreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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


    def print_management_tree(self, arg):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if arg == 'name':
            string = prefix + self.name
        elif arg == 'designation':
            string = prefix + self.designation
        else:
            string = f'{prefix} {self.name} ({self.designation})'

        print(string)
        if self.children:
            for child in self.children:
                child.print_management_tree(arg)



def build_management_heirarchy_tree():
    ceo = ManagementTreeNode("Nilpul", "CEO")

    cto = ManagementTreeNode("Chinmay", "CTO")
    hr_head = ManagementTreeNode("Gels", "HR Head")

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    infra_head = ManagementTreeNode("Vishwa", "Infrastructure Head")
    appli_head = ManagementTreeNode("Aamir", "Application Head")

    cto.add_child(infra_head)
    cto.add_child(appli_head)

    recruit_man = ManagementTreeNode("Peter", 'Recruitment Manager')
    policy_man = ManagementTreeNode("Waqas", "Policy Manager")

    hr_head.add_child(recruit_man)
    hr_head.add_child(policy_man)

    cloud_man = ManagementTreeNode("Dhaval", "Cloud Manager")
    app_man = ManagementTreeNode("Abhijit", "App Manager")

    infra_head.add_child(cloud_man)
    infra_head.add_child(app_man)

    return ceo


root = build_management_heirarchy_tree()
root.print_management_tree("name")
root.print_management_tree("designation")
root.print_management_tree("both")
