
import parso
import os
from loguru import logger
from collections import namedtuple

AbsoluteImport = namedtuple('AbsoluteImport', ['module', 'imported', 'alias'])
RelativeImport = namedtuple('RelativeImport', ['relative', 'module', 'imported', 'alias'])

class PythonImportFrom(object):
    def __init__(self, import_from):
        self.imports = []
        self.finalize(import_from)

    def finalize(self, import_from):
        children = import_from.children
        if len(children) < 4:
            raise Exception('import from statement right?')
        module_nodes = []
        import_nodes = []
        for idx, child in enumerate(children):
            if child.type == 'keyword' and child.value == 'import':
                module_nodes = children[1:idx]
                import_nodes = children[idx+1:]
                break
        relative, module_name = self._finalize_from_module(module_nodes)
        assert len(import_nodes) == 1
        imported = self._finalize_imported(import_nodes[0])
        for imp in imported:
            if relative == None:
                pyimport = AbsoluteImport(module=module_name,
                    imported=imp[0], alias=imp[1])
            else:
                pyimport = RelativeImport(relative=relative, module=module_name,
                    imported=imp[0], alias=imp[1])
            self.imports.append(pyimport)
        print(self.imports)

    def _finalize_from_module(self, module_nodes):
        relative = None
        first = module_nodes[0]
        module_node = module_nodes[0]
        node_num = len(module_nodes)
        if first.type == 'operator' and first.value == ".":
            if node_num == 1:
                return (".", None)
            else:
                second = module_nodes[1]
                if second.type == 'operator' and second.value == ".":
                    relative = ".."
                    if node_num == 2:
                        return (relative, None)
                    module_node = module_nodes[2]
                else:
                    relative = "."
                    module_node = second

        if module_node.type == 'dotted_name':
            name = []
            for node in module_node.children:
                if node.value != ".":
                    name.append(node.value)
        elif module_node.type == 'name':
            name = [str(module_node)]

        return (relative, name)

    def _finalize_import_as_names(self, node):
        children = node.children
        imports = []
        for child in children:
            _type = child.type
            if _type == 'name':
                imports.append((child.value, None))
            elif _type == 'import_as_name':
                imports.append((child.children[0].value, child.children[2].value))
            elif _type == 'operator':
                pass
            else:
                raise Exception('unhandled child type {}'.format(child.type))
        return imports

    def _finalize_imported(self, imported):
        _type = imported.type
        if _type == 'import_as_names':
            return self._finalize_import_as_names(imported)
        elif _type == 'name':
            return [(imported.value, None)]
        elif _type == 'import_as_name':
            return [((imported.children[0].value, imported.children[2].value))]
        else:
            raise Exception('unhandled imported type {}'.format(imported.type))
        return



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
        logger.debug('python module load ', file_path)
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


