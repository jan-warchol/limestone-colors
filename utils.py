import os, sys, importlib

def import_module_from_path(path):
    """Dynamically import module from path."""
    module_dir = os.path.dirname(path)
    file_name = os.path.basename(path)
    module_name = file_name.replace(".py", "")

    if module_dir not in sys.path:
        sys.path.insert(0, module_dir)

    return importlib.import_module(module_name)
