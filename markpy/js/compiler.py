
import parso

class JSNodeVisitor:
    def visit(self, node):
        """Visit a node."""
        print('visit:', node)
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def visit_leaf(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, None)
        if visitor:
            return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for child in node.children:
            if isinstance(child, parso.tree.BaseNode):
                self.visit(child)
            elif isinstance(child, parso.tree.NodeOrLeaf):
                self.visit_leaf(child)

class MarkpyJSCompiler:
    def __init__(self, script_path, code=None, offset=(0, 0)):
        self.script_path  = script_path
        self.code = code
        self.offset = offset
        if not self.code:
            with open(self.script_path, 'rb') as sf:
                self.code = sf.read()
                self.offset = (0, 0)


    def compile(self):
        tree = parso.parse(self.code)
        print(type(tree))

        visitor = JSNodeVisitor()
        visitor.visit(tree)

if __name__ == '__main__':
    py_code = '''
def test():
    return 16
'''
    spc = MarkpyJSCompiler('', py_code)
    spc.compile()

