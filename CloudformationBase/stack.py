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
        self.template = Template()

    def stack_template(self):
        return self.template

    @abc.abstractmethod
    def populate_template(self):
        return

    @abc.abstractmethod
    def output_template(self):
        print self.template.to_json()
        return
