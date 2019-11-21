
from .compiler import Compiler

def main():
    import sys
    source = sys.argv[1]
    c = Compiler(source)
    c.compile()
    #c.dumpTree()
