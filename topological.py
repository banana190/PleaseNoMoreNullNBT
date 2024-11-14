from module_graph import *

visit_count = 0
batch = 3

def topological_sort(modules):
    sorted_modules = []     #just to see the order
    global visit_count
    def dfs(module):
        global visit_count
        if module.isVisited is True:
            return
        module.isVisited = True
        module.disable()
        sorted_modules.append(module)
        visit_count = visit_count+1
        if visit_count > batch:
            return

        for child in module.children:
            if visit_count<=batch:
                dfs(child)


    for module in modules.values():
        if not module.children and visit_count<=batch :
            dfs(module)
    visit_count = 0
    return sorted_modules


