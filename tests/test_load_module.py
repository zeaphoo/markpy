from markpy.compiler.tree import PythonModule

def test_load_module():
    m = PythonModule.load("assets/hello/foo.py")