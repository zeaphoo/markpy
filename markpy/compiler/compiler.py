
import os
import parso
from parso.python.tree import PythonLeaf
import contextlib
from .cgenerator import CGenerator

def prettyformat(node, _indent=0):
    indent_str='    '
    if node is None:  # pragma: nocovrage
        return repr(node)
    elif isinstance(node, str):
        return repr(node)
    elif isinstance(node, PythonLeaf):
        return '{}({})'.format(type(node).__name__, repr(node.value))
    else:
        class state:
            indent = _indent

        @contextlib.contextmanager
        def indented():
            state.indent += 1
            yield
            state.indent -= 1

        def indentstr():
            return state.indent * indent_str

        def _pformat(el, _indent=0):
            return prettyformat(el, _indent=_indent)

        out = type(node).__name__ + '(\n'
        with indented():
            assert len(node.children) > 0
            for field in node.children:
                representation = _pformat(field, state.indent)
                out += '{}{}={},\n'.format(indentstr(), repr(field.type), representation)
        out += indentstr() + ')'
        return out

class Compiler(object):
    def __init__(self, source_path):
        super(Compiler, self).__init__()
        self.source_path = source_path
        with open(self.source_path) as f:
            self.source = f.read()
        self.ast_path = '{}.ast'.format(self.source_path)

    def compile(self):
        try:
            self.module = parso.parse(self.source)
            #self.dump_tree()
            generator = CGenerator(self)
            generator.gen()
        except:
            raise

    def dump_tree(self):
        print('Dumping syntax tree for module: {}\n', self.source_path)
        text = prettyformat(self.module)
        with open(self.ast_path, 'wb') as treeFile:
            treeFile.write(text.encode('utf-8'))
