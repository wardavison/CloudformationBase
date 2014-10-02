""" Stack class
"""
import abc
from troposphere import Template


class Stack(object):
    """ Stack object for generating the Cloudformation template
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, projectname, environmentname):
        self.projectname = projectname
        self.environmentname = environmentname
        self.parameters = []
        self.mappings = []
        self.resources = []
        self.outputs = []

    @abc.abstractmethod
    def populate_template(self):
        return

    def output_template(self):
        template = Template()
        for parameter in self.parameters:
            template.add_parameter(parameter)

        for mapping in self.mappings:
            template.add_mapping(mapping)

        for resource in self.resources:
            template.add_resource(resource)

        for output in self.outputs:
            template.add_output(output)

        print template.to_json()
        return