from module_graph import ModuleNode
from dependency_finder import *
from topological import topological_sort
import json_save_and_load as jsl
import file_dis_enable as fde
import os
import glob
import json

client_side_mod_path = ''
server_side_mod_path = 'D:/testing_server/mods'

jsl.json_generate(server_side_mod_path)

while(True):
    module_graph = jsl.json_load()
    sorted_modules = topological_sort(module_graph)
    fde.apply_disabled_mod(module_graph)

    #start server
    #server started

    #start client 10 times ReallyInnocent
    #if client get kickout from the server in 3 second continue else break and print sorted_modules

    fde.re_enable_mods(module_graph)
    jsl.json_save(module_graph)




