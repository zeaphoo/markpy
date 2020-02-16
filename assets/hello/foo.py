
import foo2
import re
import os.path
import os.path as opath
import os as yaos

from bar.module1 import BarClass as BBCLASS
from bar.module1 import BarClass, FooClass as BARCLASS, FOOCLASS
from bar.module1 import BarClass, FooClass
from bar.module4 import BarClass4
from .module import BaseClass
from .module.submodule import SomeClass
from ..module import SomeClassBase
from ..module.submodule import SomeClass
from . import BaseClass
from .. import SomeClass

class Foo(object):
    def __init__(self):
        self.a = "hello"
        self.b = 123
    
    def echo(self):
        from bar.module2 import BarClass2

    

from bar.module3 import BarClass3