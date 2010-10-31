"""waf script to build the README file from the template."""
def configure(conf):
    pass

def build(bld):
    def build_readme(task):
        import help_template
        template_text = task.inputs[0].read()
        template = help_template.HelpTemplate(template_text)
        task.outputs[0].write(template.substitute())
    
    bld(rule=build_readme,
        source='README.template help_template.py',
        target='../README.txt')
