
import parso

class CGenerator:
    def __init__(self, module):
        self.module = module
        self.visit(self.module)

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
