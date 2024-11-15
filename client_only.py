from dependency_finder import *
import json


def json_gen_client(client_side_mod_path):

    load_all_mods(client_side_mod_path)
    mod_data = {}
    for modId, node in modules.items():
        node.client = True
        mod_data[modId] = node.to_dict()
    file_path = 'client_mod_data.json'
    with open(file_path, 'w') as f:
        json.dump(mod_data, f, indent=4)

if __name__ == '__main__':
    json_gen_client('../mods')