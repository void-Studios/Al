import os
import glob

module_files = glob.glob(os.path.join(os.path.dirname(__file__),"*.py"))

for module_file in module_files:
    if os.path.basename(module_file) != "__init__.py":
        module_name = os.path.splitext(os.path.basename(module_file))[0]
        __import__(".".join(["modules", module_name]))
        