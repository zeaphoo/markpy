
from markpy.compiler.utils import ast

class CGenerator(ast.NodeVisitor):
    def __init__(self, module):
        self.module = module
        self.visit(self.module.parseTree)

    def visit_FunctionDef(self, node):
        pass
    
    
    def visit(self, node):
        try:
            self.lineNr = node.lineno
        except:
            pass
        ast.NodeVisitor.visit (self, node)

    def gen(self):
        return ''
