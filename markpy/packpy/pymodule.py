
import parso
import os

class PythonModule(object):
    def __init__(self, name, module, parent):
        self.name = name
        self.module = module
        self.parent = parent
        print(self)
    
    @property
    def fullname(self):
        return self.name if not self.parent else '{}.{}'.format(self.parent, self.name)

    @classmethod
    def load(cls, file_path, parent=None):
        fpath = file_path
        name = os.path.splitext(os.path.basename(file_path))[0]

        with open(fpath, 'rb') as f:
            module = parso.parse(f.read())
            print(module)
            print(list(module.iter_imports()))
            return cls(name, module, parent)
    
    def __str__(self):
        return '<PythonModule: {}>'.format(self.fullname)
    

    def __repr__(self):
        return self.__str__()


