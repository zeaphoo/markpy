import sys

from types import ModuleType

def add_module(name, submod):
    sys.modules[__name__ + "." + name] = submod(name)

class submod1(ModuleType):
    class subsubmod1(ModuleType):
        class foofoo:
            pass

    foofoo2 = subsubmod1.foofoo
    class foo:
        pass

add_module('submod1', submod1)
add_module('submod1.subsubmod1', submod1.subsubmod1)
submod1.foofoo = submod1.subsubmod1.foofoo


class submod2(ModuleType):
    foofoo = submod1.subsubmod1.foofoo
    class bar:
        pass

print(submod1)
print(submod1.subsubmod1)
