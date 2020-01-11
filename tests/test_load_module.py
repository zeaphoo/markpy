from markpy.pymodule import PythonModule

def test_load_module():
    m = PythonModule.load('foo', "assets/hello/foo.py")