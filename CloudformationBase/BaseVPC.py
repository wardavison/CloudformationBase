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
        self.parameters = []
        self.mappings = []
        self.resources = []
        self.outputs = []
        self.basevpc = None
        self.set_resources()

    def res_vpc(self, title, cidrblock, dnssupport, dnshostnames,
                instancetenancy):
        """ Creates a Troposphere VPC resource object
        The name is generated from the projectname and environment name
        :param title: Title for the JSON VPC resource (string)
        :param cidrblock: CIDR block for the VPC e.g. 10.0.0.0/16 (string)
        :param dnssupport: The VPC has DNS support (boolean)
        :param dnshostnames: Enable DNS hostnames (boolean)
        :param instancetenancy: default or dedicated instance tenancy (string)
        """
        return VPC(
            title,
            CidrBlock=cidrblock,
            EnableDnsSupport=dnssupport,
            EnableDnsHostnames=dnshostnames,
            InstanceTenancy=instancetenancy,
            Tags=[Tag('Name', Join('', [self.projectname,
                                        '-',
                                        self.environmentname,
                                        '-VPC']))]
        )

    def set_parameters(self):
        pass

    def set_mappings(self):
        pass

    def set_resources(self):
        self.basevpc = self.res_vpc('BaseVPC', '10.0.0.0/16',
                                    True, True, 'default')
        self.resources.append(self.basevpc)

    def set_outputs(self):
        """
        :return:
        """
        pass

    @property
    @abc.abstractmethod
    def get_parameters(self):
        """ Return parameters for use by the VPC
        """
        return self.parameters

    @property
    @abc.abstractmethod
    def get_mappings(self):
        """ Return mappings for use in the template
        """
        return self.mappings

    @property
    @abc.abstractmethod
    def get_resources(self):
        """ Return resources that make up the VPC
        :return: list of Troposphere resource objects
        :rtype : list
        """
        return self.resources

    @property
    @abc.abstractmethod
    def get_outputs(self):
        """ Return outputs generated from VPC resources
        """
        return self.outputs