""" Stack class
"""
import abc
from CloudformationBase.constants import REGION_AZ_MAPPINGS, REGION_AZ_MAP
from troposphere import Template, Parameter


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

        self.mappings.append([REGION_AZ_MAP, REGION_AZ_MAPPINGS])

    @abc.abstractmethod
    def populate_template(self):
        return

    def output_template(self):
        template = Template()
        for parameter in self.parameters:
            template.add_parameter(parameter)

        for mapping in self.mappings:
            template.add_mapping(mapping[0], mapping[1])

        for resource in self.resources:
            template.add_resource(resource)

        for output in self.outputs:
            template.add_output(output)

        print template.to_json()
        return

    @staticmethod
    def par_custom(title, par_type, par_default, description):
        return Parameter(
            title,
            Type=par_type,
            Default=par_default,
            Description=description
        )