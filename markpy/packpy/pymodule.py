
import parso
import os
from loguru import logger

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
            logger.debug(type(imp))

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


