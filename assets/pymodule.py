import sys

from types import ModuleType

def add_module(name, submod):
    sys.modules[name] = submod(name)

def get_module(name):
    return sys.modules[name]

class submod1__subsubmod1(ModuleType):
    class foofoo:
        x = 1

add_module('submod1.subsubmod1', submod1__subsubmod1)


class submod3_meta(type):
    def __init__(cls, name, bases, attrs):
        super(submod3_meta, cls).__init__(name, bases, attrs)
        foofoo2 = get_module("submod1.subsubmod1").foofoo
        cls.foofoo2 = foofoo2
        class foo:
            print('submod3 inner foofoo2', foofoo2)
            pass
        cls.foo = foo
        print('submod3 creating')
        print('submod3_meta foofoo2', cls.foofoo2)
        print(attrs)


class submod3(ModuleType, metaclass=submod3_meta): pass
add_module('submod3', submod3)

f = submod3.foo()
print(type(f))
print(submod3.foo)

class submod1(ModuleType):
    def __init__(self, name):
        super(submod1, self).__init__(name)
        foofoo2 = get_module("submod1.subsubmod1").foofoo
        self.foofoo2 = foofoo2
        class foo:
            print('inner foofoo2', foofoo2)
            pass
        self.foo = foo


add_module('submod1', submod1)

import submod1
f = submod1.foo()
print(type(f))
print(submod1.foo)
import submod1.subsubmod1

submod1.foofoo = get_module("submod1.subsubmod1").foofoo
submod1.subsubmod1 = get_module("submod1.subsubmod1")

class submod2(ModuleType):
    def __init__(self, name):
        super(submod2, self).__init__(name)
        foofoo = get_module("submod1.subsubmod1").foofoo
        self.foofoo = foofoo
        class bar:
            y = foofoo.x
        self.bar = bar

#import submod1
print(submod1)
print(submod1.subsubmod1)
