""" baseVPC class
"""

from troposphere import Join, Parameter
from troposphere.ec2 import VPC, Tag, Subnet


class BaseVPC(object):
    """ VPC class defining some basic defaults
    """

    def __init__(self):
        pass

    @staticmethod
    def par_cidrblock(title, description, default):
        """
        :return: Troposphere parameter object for a CIDR block
        """
        return Parameter(
            title,
            Description=description,
            Type='String',
            Default=default
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

    @staticmethod
    def res_subnet(title, namesuffix, vpcaz, cidrblock, vpcid, projectname,
                   environmentname):
        """
        :param title: Title for the JSON Subnet resource (string)
        :param namesuffix: Display name suffix for the subnet (string)
        :param vpcaz: AvailabilityZone for the subnet (string)
        :param cidrblock: CIDR block for the subnet e.g. 10.0.0.0/24 (string)
        :param vpcid: ID of the VPC this subnet should be linked to (string)
        :param projectname: Name of project (used to form name) (string)
        :param environmentname: Name of environment (used to form name) (string)
        :return: Troposphere Subnet object
        """
        return Subnet(
            title,
            AvailabilityZone=vpcaz,
            CidrBlock=cidrblock,
            Tags=[Tag('Name', Join('', [projectname,
                                        '-',
                                        environmentname,
                                        '-',
                                        namesuffix]))],
            VpcId=vpcid,
        )