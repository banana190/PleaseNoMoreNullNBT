class ModuleNode:
    def __init__(self, modId):
        self.modId = modId
        self.parents = []
        self.children = []
        self.disabled = False
        self.client = False
        self.server = False

    def add_parent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
            parent.add_child(self)

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)

    def disable(self):
        if not self.disabled:
            self.disabled = True
            print(f"Disabling {self.modId}")
            for child in self.children:
                child.disable()

    def is_in_client(self):
        self.client = True

    def is_in_server(self):
        self.server = True


