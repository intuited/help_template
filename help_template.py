"""Enables the use of Python identifiers in templates."""
import string, contextlib

@contextlib.contextmanager
def borrow_stdout(new_out):
    import sys
    orig = sys.stdout
    sys.stdout = new_out
    yield new_out
    sys.stdout = orig

def compile_help(identifier):
    """Return the help information normally printed to `sys.stdout`."""
    # The replacement of `sys.stdout` is necessary for the (common) case
    # where `pydoc.help` calls `pydoc.doc`.
    # Otherwise we could just use a pydoc.Helper object.
    import StringIO
    with borrow_stdout(StringIO.StringIO()) as docs:
        help(identifier)
    return docs.getvalue()

class HelpTemplate(string.Template):
    r"""A Template whose identifiers are help entries"""
    idpattern = r'[_a-z][_a-z0-9]*(\.[_a-z][_a-z0-9]*)*'

    def convert(self, match_object):
        for group in ('invalid', 'escaped', 'named', 'braced'):
            identifier = match_object.group(group)
            if identifier is not None:
                return getattr(self, group)(match_object, identifier)
        raise ValueError('Unrecognized named group in pattern', self.pattern)

    def named(self, match_object, identifier):
        return compile_help(identifier)
    braced = named

    def escaped(self, match_object, identifier):
        return self.delimiter

    def invalid(self, match_object, identifier):
        return super(HelpTemplate, self)._invalid(match_object)

    def substitute(self):
        r"""Substitute help documentation for embedded template identifiers.
        
        Examples::

            >>> def test_fn():
            ...     '''This is the docstring for the test_fn function.'''
            ...     pass
            >>> from textwrap import dedent
            >>> template = HelpTemplate(dedent('''\
            ...     HelpTemplate makes it convenient to embed help
            ...     for functions, classes, and modules.
            ...     For example, documentation for the `compile_help` function
            ...     in this module can be embedded with
            ...     
            ...     ${help_template.compile_help}'''))
            >>> print template.substitute()
            HelpTemplate makes it convenient to embed help
            for functions, classes, and modules.
            For example, documentation for the `compile_help` function
            in this module can be embedded with
            <BLANKLINE>
            Help on function compile_help in help_template:
            <BLANKLINE>
            help_template.compile_help = compile_help(identifier)
                Return the help information normally printed to `sys.stdout`.
            <BLANKLINE>
            <BLANKLINE>
        """
        return self.pattern.sub(self.convert, self.template)

    def safe_substitute(self):
        """This is not really supported.

        It will just substitute "Documentation not found..."
        for any identifiers that don't have help documentation.

        This is how `help` works,
        and fixing it would involve re-implementing most of its routing code
        to handle modules, symbols, etc.
        """
        try:
            real_invalid = self.invalid
            self.invalid = self.escaped
            return self.substitute()
        finally:
            self.invalid = real_invalid
