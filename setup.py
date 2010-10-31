# Require setuptools for script installation
try:
    from setuptools import setup
except ImportError:
    from sys import stderr
    print >> stderr, (
        'Sorry, you must install the ``setuptools`` module'
        ' in order to install this package.\n'
        '``setuptools`` can be installed with the command\n'
        '    easy_install setuptools\n'
        'or by download from <http://pypi.python.org/pypi/setuptools>.\n'
        )
    raise


from textwrap import dedent, fill

def format_desc(desc):
    if len(desc) > 200:
        raise ValueError("Description cannot exceed 200 characters.")
    return fill(dedent(desc), 200)

def format_classifiers(classifiers):
    return dedent(classifiers).strip().split('\n')

def split_keywords(keywords):
    return dedent(keywords).strip().replace('\n', ' ').split(' ')

def file_contents(filename):
    with open(filename) as f:
        return f.read()

setup(
    name = "help_template",
    version = "0.2",
    author = "Ted Tibbetts",
    author_email = "intuited@gmail.com",
    url = "http://github.com/intuited/help_template",
    description = format_desc("""
        Simple template that extends `string.Template`
        to provide a convenient way to embed help documentation.
        """),
    long_description = file_contents('README.txt'),
    classifiers = format_classifiers("""
        Development Status :: 4 - Beta
        Intended Audience :: Developers
        License :: OSI Approved :: BSD License
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 2
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Utilities
        """),
    keywords = split_keywords("""
        templates template documentation docs help
        """),
    py_modules = ['help_template'],
    )
