
class CNode(object):
    def __init__(self):
        self._children = []
    
    def add_children(self, child_node, *args):
        self._children.append(child_node)
        for node in args:
            self._children.append(node)

    def emit(self, emit_func=print):
        pass
    
    def children(self):
        return self._children

class FuncDeclaration(CNode):
    def __init__(self, name, args, return_value):
        pass
    
    def emit(self, emit_func=print):
        emit_func('{} {}({}){\n'.format(self.return_value, self.name, self.args))
        for stmt in self.children:
            stmt.emit(emit_func=emit_func)
        emit_func('}\n')
    
