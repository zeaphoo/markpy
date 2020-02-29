
import click
from basepy.log import logger
import sys
import os

logger.add('stdout')

@click.group()
def markpy():
    pass

@markpy.command()
@click.argument('package_path')
def pack(package_path):
    from markpy.compiler.pack import PythonPackage
    pp = PythonPackage(package_path)
    pp.pack()



if __name__ == '__main__':
    markpy()