
import click

@click.group()
def markpy():
    pass

@markpy.command()
@click.argument('package_path')
def pack(package_path):
    click.echo(package_path)
    from markpy.packpy.pack import PythonPackage
    pp = PythonPackage(package_path)
    pp.pack()



if __name__ == '__main__':
    markpy()