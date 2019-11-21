
from markpy.compiler.utils import ast

import os

from markpy.compiler.cgenerator import CGenerator

class Compiler(object):
    def __init__(self, sourcePath):
        super(Compiler, self).__init__()
        self.sourcePath = sourcePath
        with open(self.sourcePath) as f:
            self.source = f.read()
        self.treePath = '{}.ast'.format(self.sourcePath)

    def compile(self):
        try:
            self.parseTree = ast.parse (self.source)
            #self.dumpTree()
            generator = CGenerator(self)
            generator.gen()
        except:
            raise

    def dumpTree (self):
        print('Dumping syntax tree for module: {}\n', self.sourcePath)

        def walk (name, value, tabLevel):
            self.treeFragments .append ('\n{0}{1}: {2} '.format (tabLevel * '\t', name, type (value).__name__ ))
            if isinstance (value, ast.AST):
                for field in ast.iter_fields (value):
                    print(field)
                    walk (field [0], field [1], tabLevel + 1)
            elif isinstance (value, list):
                for element in value:
                    walk ('element', element, tabLevel + 1)
            else:
                self.treeFragments.append ('= {0}'.format (value))

        self.treeFragments = []
        walk ('file', self.parseTree, 0)
        self.textTree = ''.join (self.treeFragments) [1:]

        with open(self.treePath, 'wb') as treeFile:
            treeFile.write(self.textTree.encode('utf-8'))
