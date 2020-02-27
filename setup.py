import re
import ast
from setuptools import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('markpy/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='markpy',
    version=version,
    url='https://github.com/zeaphoo/markpy/',
    license='MIT',
    author='Wei Zhuo',
    author_email='zeaphoo@qq.com',
    description='A static type compiler for python',
    long_description='A program style using python write static program and a compiler',
    packages=['markpy'],
    include_package_data=False,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'sh',
        'parso',
        'click',
        'loguru'
    ],
    extras_require={
        'dev': [
            'pytest>=3',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points='''
        [console_scripts]
            markpy=markpy.main:markpy
    '''
)
