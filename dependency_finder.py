import zipfile
import toml
import glob
import os
import re
from module_graph import *

modules = {}
i = 0
j = 0

# get_module is to make sure not to create a new node when there is already exist one
def get_module(modId):
    global i , j
    if modId not in modules:
        i = i + 1
        print('creating a new mod',modId,i)
        modules[modId] = ModuleNode(modId)
    j = j + 1
    print('now is mod ', j)
    return modules[modId]

# toml_reader is to read all the mods.toml in jar and append into the graph
def toml_reader(jar_path):
    with zipfile.ZipFile(jar_path, 'r') as jar:
        # print("Files in jar:", jar.namelist())
        i = 0

        if 'META-INF/mods.toml' in jar.namelist():
            with jar.open('META-INF/mods.toml') as toml_file:
                temp = toml_file.read().decode('utf-8')
                toml_content = toml.loads(temp)
                # self
                modId = toml_content['mods'][0]['modId'].lower()
                mod_node = get_module(modId)
                mod_node.setpath(jar_path)
                # parent if needed you can ignore forge and minecraft
                if 'dependencies' in toml_content:
                    case_insensitive_dependencies = \
                        {key.lower(): value for key, value in toml_content['dependencies'].items()}
                    for dep in case_insensitive_dependencies[modId]:
                        dep_modId = dep['modId'].lower()
                        if dep['mandatory'] and dep_modId not in {'minecraft', 'forge'}:
                            dep_node = get_module(dep_modId)
                            mod_node.add_parent(dep_node)
                    return mod_node
                else:
                    print('Wrong toml format file at:' ,modId)
                    dep_pattern = r'\[\[dependencies\.(.*?)\]\](.*?)modId="(.*?)"(.*?)mandatory=(true|false)'
                    matches = re.findall(dep_pattern, temp, re.DOTALL)
                    for match in matches:
                        if match[4] == 'true' and match[2].strip() not in {'minecraft', 'forge'}:
                            dep_modId = match[2].strip()
                            dep_node = get_module(dep_modId)
                            mod_node.add_parent(dep_node)
                    return mod_node

        else:
            print(f"[Error] Cannot find {jar_path}'s mods.toml!!!")
            return None


def load_all_mods(directory):
    mod_files = glob.glob(os.path.join(directory, '*.jar'))
    all_mods = []
    for jar_file in mod_files:
        print(f"Reading: {jar_file}")
        mod_toml_content = toml_reader(jar_file)
        if mod_toml_content:
            all_mods.append(mod_toml_content)

    return all_mods
