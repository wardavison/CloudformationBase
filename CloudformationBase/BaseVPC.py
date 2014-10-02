""" baseVPC class
"""

from troposphere import Join, Parameter
from troposphere.ec2 import VPC, Tag


class BaseVPC(object):
    """ VPC class defining some basic defaults
    """

    def __init__(self):
        pass

    @staticmethod
    def par_vpccidrblock(title):
        """
        :return: Troposphere parameter object for the VPC CIDR block
        """
        return Parameter(
            title,
            Description="VPC CIDR Block",
            Type="String",
            Default="10.0.0.0/16"
        )

    @staticmethod
    def res_vpc(title, cidrblock, dnssupport, dnshostnames,
                instancetenancy, projectname, environmentname):
        """
        :param title: Title for the JSON VPC resource (string)
        :param cidrblock: CIDR block for the VPC e.g. 10.0.0.0/16 (string)
        :param dnssupport: The VPC has DNS support (boolean)
        :param dnshostnames: Enable DNS hostnames (boolean)
        :param instancetenancy: default or dedicated instance tenancy (string)
        :param projectname: Name of project (used to form name) (string)
        :param environmentname: Name of environment (used to form name) (string)
        :return: Troposphere VPC resource object
        """
        return VPC(
            title,
            CidrBlock=cidrblock,
            EnableDnsSupport=dnssupport,
            EnableDnsHostnames=dnshostnames,
            InstanceTenancy=instancetenancy,
            Tags=[Tag('Name', Join('', [projectname,
                                        '-',
                                        environmentname,
                                        '-VPC']))]
        )