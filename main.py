from module_graph import ModuleNode
from dependency_finder import *
import os
import glob

client_side_mod_path = ''
server_side_mod_path = 'D:/testing_server/mods'

module_graph = load_all_mods(server_side_mod_path)

