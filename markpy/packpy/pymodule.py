
import parso
import os
from loguru import logger

class PythonImportFrom(object):
    def __init__(self, import_from):
        self.import_from = import_from
        self.children = import_from.children


class PythonImportName(object):
    def __init__(self, import_name):
        self.import_name = import_name
        self.children = import_name.children


class PythonModule(object):
    def __init__(self, name, module, parent):
        self.name = name
        self.module = module
        self.parent = parent
        self.imports = []
        self.format_imports()
    
    @property
    def fullname(self):
        return self.name if not self.parent else '{}.{}'.format(self.parent, self.name)

    def format_imports(self):
        imports = list(self.module.iter_imports())
        if len(imports) == 0:
            return
        logger.debug(imports)
        for imp in imports:
            if isinstance(imp, parso.python.tree.ImportFrom):
                pyimport = PythonImportFrom(imp)
            elif isinstance(imp, parso.python.tree.ImportName):
                pyimport = PythonImportName(imp)
            else:
                raise Exception('New import type [{}] not handled. '.format(type(imp)))
            self.imports.append(pyimport)

    @classmethod
    def load(cls, file_path, parent=None):
        fpath = file_path
        name = os.path.splitext(os.path.basename(file_path))[0]

        with open(fpath, 'rb') as f:
            module = parso.parse(f.read())
            pymodule = cls(name, module, parent)
            logger.info('create module {}'.format(pymodule))
            return pymodule
    
    def __str__(self):
        return '<PythonModule: {}>'.format(self.fullname)
    

    def __repr__(self):
        return self.__str__()


