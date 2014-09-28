""" baseVPC class
"""
import abc
from troposphere import Join
from troposphere.ec2 import VPC, Tag


class BaseVPC(object):
    """ VPC class defining some basic defaults
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, projectname, environmentname):
        self.projectname = projectname
        self.environmentname = environmentname

    @property
    @abc.abstractmethod
    def res_vpc(self):
        return VPC(
            'BaseVPC',
            CidrBlock='10.0.0.0/16',
            EnableDnsSupport=True,
            EnableDnsHostnames=True,
            InstanceTenancy='default',
            Tags=[Tag('Name', Join('', [self.projectname,
                                        '-',
                                        self.environmentname,
                                        '-VPC']))]
        )

    #@abc.abstractmethod
    #def set_parameters(self):
    #    """ Define parameters for use by the VPC
    #    """
    #    return

    #@abc.abstractmethod
    #def set_mappings(self):
    #    """ Define mappings for use in the template
    #    """
    #    return

    #@abc.abstractmethod
    #def set_resources(self):
    #    """ Define resources that make up the VPC
    #    """
    #    return

    #@abc.abstractmethod
    #def set_outputs(self):
    #    """ Define outputs to generated from VPC resources
    #    """