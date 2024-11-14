import os

def apply_disabled_mod(modules):
    for module in modules.values():
        if module.disabled:
            if not module.filepath.endswith(".disable"):
                new_path = module.filepath + '.disable'
                os.rename(module.filepath,new_path)
                module.filepath = new_path

def re_enable_mods(modules):
    for module in modules.values():
        if module.disabled:
            if module.filepath.endswith(".disable"):
                new_path = module.filepath[:-8]
                os.rename(module.filepath,new_path)
                module.filepath = new_path
                module.disabled = False