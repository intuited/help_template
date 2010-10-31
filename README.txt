``help_template``
=================

Simple template that extends `string.Template`
to provide a convenient way to embed help documentation.

The module's functionality is provided by way of the class
`help_template.HelpTemplate`.

This is mostly useful for single functions.

For example, the line

${help_template.HelpTemplate.substitute}

will appear as follows:

Help on method substitute in help_template.HelpTemplate:

help_template.HelpTemplate.substitute = substitute(self) unbound help_template.HelpTemplate method
    Substitute help documentation for embedded template identifiers.
    
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



Usage
-----

As an example of how to use this module,
consult the files ``README.template`` and ``wscript``.
These files are used to build this readme file.

License
-------

`help_template` is licensed under the FreeBSD license.
See the file COPYING for details.
