
import click
from loguru import logger
import sys
import os

logger.remove()
logger.add(sys.stdout, colorize=True, format="<green>[{time:YYYY-MM-DD HH:mm:ss}]</green> <level>{message}</level>")

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