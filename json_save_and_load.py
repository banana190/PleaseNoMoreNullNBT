from module_graph import ModuleNode
from dependency_finder import *
from topological import topological_sort
import json


def json_generate(server_side_mod_path):

    module_graph = load_all_mods(server_side_mod_path)
    mod_data = {}
    for modId, node in modules.items():
        mod_data[modId] = node.to_dict()
    file_path = 'mod_data.json'
    with open(file_path, 'w') as f:
        json.dump(mod_data, f, indent=4)


def json_load():
    file_path = 'mod_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            mod_data_loaded = json.load(f)

        modules_recreated = {}
        for modId, data in mod_data_loaded.items():
            node = ModuleNode(modId)
            for key, value in data.items():
                if key not in {'parents', 'children'}:
                    setattr(node, key, value)
            modules_recreated[modId] = node

        for modId, data in mod_data_loaded.items():
            node = modules_recreated[modId]
            for parentId in data['parents']:
                parent_node = modules_recreated.get(parentId)
                if parent_node:
                    node.add_parent(parent_node)
            for childId in data['children']:
                child_node = modules_recreated.get(childId)
                if child_node:
                    node.add_child(child_node)

        return modules_recreated
    return {}

def json_save(module):
    mod_data = {}
    for modId, node in module.items():
        mod_data[modId] = node.to_dict()
    file_path = 'mod_data.json'
    with open(file_path, 'w') as f:
        json.dump(mod_data, f, indent=4)