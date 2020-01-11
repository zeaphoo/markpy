
import parso
import os

class PythonModule(object):
    def __init__(self, name, module):
        pass
    
    @classmethod
    def load(cls, name, file_path):
        if os.path.isdir(file_path):
            fpath = '{}/__init__.py'.format(file_path)
        else:
            fpath = file_path

        with open(fpath, 'rb') as f:
            module = parso.parse(f.read())
            print(module)
            print(list(module.iter_imports()))
            return cls(name, module)


