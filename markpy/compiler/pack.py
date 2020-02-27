import os
from .tree import PythonModule
from loguru import logger

class PythonPackage(object):
    def __init__(self, package_path, parent=None):
        self.package_path = os.path.abspath(package_path)
        name = os.path.basename(package_path)
        self.name = name if not parent else '{}.{}'.format(parent, name)
        self.modules = []
        self.packages = []
        self.main_module = None
        self.load()

    @property
    def valid(self):
        return self.main_module != None

    def load(self):
        module_path = os.path.join(self.package_path, '__init__.py')
        if os.path.exists(module_path):
            self.main_module = PythonModule.load(module_path, parent=self.name)

        with os.scandir(self.package_path) as it:
            for entry in it:
                if entry.name in ['__init__.py']:
                    continue
                if entry.is_dir():
                    try:
                        subpackage = PythonPackage(entry.path, parent=self.name)
                        if subpackage.valid:
                            self.packages.append(subpackage)
                    except:
                        raise

                if entry.is_file() and entry.name.endswith('.py'):
                    module = PythonModule.load(entry.path, parent=self.name)
                    if module:
                        self.modules.append(module)

    def pack(self):
        pass