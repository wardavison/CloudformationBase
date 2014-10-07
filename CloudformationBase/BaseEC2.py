"""  baseEC2 class
"""
from troposphere import Join
from troposphere.ec2 import SecurityGroup, Tag, SecurityGroupRule, Instance, \
    NetworkInterfaceProperty


class BaseEC2(object):
    """ EC2 class defining some basic defaults
    """

    def __init__(self):
        pass

    @staticmethod
    def res_security_group(title, sgegress, sgingress, projectname,
                           environmentname, namesuffix, vpcid, groupdesc):
        """
        :param title: Title for the JSON SecurityGroup resource (string)
        :param sgegress: List of Egress SecurityGroupRule resources (list)
        :param sgingress: List of Ingress SecurityGroupRule resources (list)
        :param projectname: Name of project (used to form name) (string)
        :param environmentname: Name of environment (used to form name) (string)
        :param namesuffix: Display name suffix for the subnet (string)
        :param vpcid: VPC ID to create this SecurityGroup in (string)
        :param groupdesc: A Description for this SecurityGroup (string)
        :return: Troposphere SecurityGroup object
        """
        return SecurityGroup(
            title,
            SecurityGroupEgress=sgegress,
            SecurityGroupIngress=sgingress,
            Tags=[Tag('Name', Join('', [projectname,
                                        '-',
                                        environmentname,
                                        '-',
                                        namesuffix]))],
            VpcId=vpcid,
            GroupDescription=groupdesc
        )

    @staticmethod
    def res_ssg_security_group_rule_in(fromport, toport, protocol, ssgid):
        """
        :param fromport: The start of the port range (integer)
        :param toport: The end of the port range (integer)
        :param protocol: An IP protocol name or number (string)
        :param ssgid: ID of the EC2 SecurityGroup to allow access (string)
        :return: Troposphere SecurityGroupRule parameter
        """
        return SecurityGroupRule(
            FromPort=fromport,
            ToPort=toport,
            IpProtocol=protocol,
            SourceSecurityGroupId=ssgid
        )

    @staticmethod
    def res_cidr_security_group_rule_in(fromport, toport, protocol, cidrip):
        """
        :param fromport: The start of the port range (integer)
        :param toport: The end of the port range (integer)
        :param protocol: An IP protocol name or number (string)
        :param cidrip: CIDR IP range to allow access (string)
        :return: Troposphere SecurityGroupRule parameter
        """
        return SecurityGroupRule(
            FromPort=fromport,
            ToPort=toport,
            IpProtocol=protocol,
            CidrIp=cidrip
        )

    @staticmethod
    def res_dsg_security_group_rule_out(fromport, toport, protocol, dsgid):
        """
        :param fromport: The start of the port range (integer)
        :param toport: The end of the port range (integer)
        :param protocol: An IP protocol name or number (string)
        :param dsgid: GroupId of the destination VPC SecurityGroup (string)
        :return: Troposphere SecurityGroupRule parameter
        """
        return SecurityGroupRule(
            FromPort=fromport,
            ToPort=toport,
            IpProtocol=protocol,
            DestinationSecurityGroupId=dsgid
        )

    @staticmethod
    def res_cidr_security_group_rule_out(fromport, toport, protocol, cidrip):
        """
        :param fromport: The start of the port range (integer)
        :param toport: The end of the port range (integer)
        :param protocol: An IP protocol name or number (string)
        :param cidrip: CIDR IP range to allow access (string)
        :return: Troposphere SecurityGroupRule parameter
        """
        return SecurityGroupRule(
            FromPort=fromport,
            ToPort=toport,
            IpProtocol=protocol,
            CidrIp=cidrip
        )

    @staticmethod
    def res_instance(title, imageid, instancetype, keyname,
                     networkinterfaceprops, projectname, environmentname,
                     namesuffix):
        """
        :param title: Title for the JSON Instance resource (string)
        :param imageid: AMI ID of an image to launch (string)
        :param instancetype: EC2 instance type (string)
        :param keyname: EC2 Keypair Name to launch the instance under (string)
        :param networkinterfaceprops: NetworkInterfaceProperties for this (list)
        :param projectname: Name of project (used to form name) (string)
        :param environmentname: Name of environment (used to form name) (string)
        :param namesuffix: Display name suffix for the subnet (string)
        :return: Troposphere Instance object
        """
        return Instance(
            title,
            ImageId=imageid,
            InstanceType=instancetype,
            KeyName=keyname,
            NetworkInterfaces=networkinterfaceprops,
            Tags=[Tag('Name', Join('', [projectname,
                                        '-',
                                        environmentname,
                                        '-',
                                        namesuffix]))]
        )

    @staticmethod
    def res_networkinterfaceproperty(associatepublicip, deviceindex,
                                     securitygroupids, subnetid):
        """
        :param associatepublicip: Associate a Public IP Address (boolean)
        :param deviceindex: e.g. eth0 or eth1 as '0' or '1' etc (string)
        :param securitygroupids: List of SecurityGroup IDs to associate (list)
        :param subnetid: Subnet to associate the interface with
        :return: Troposphere NetworkInterfaceProperty object
        """
        return NetworkInterfaceProperty(
            AssociatePublicIpAddress=associatepublicip,
            DeviceIndex=deviceindex,
            GroupSet=securitygroupids,
            SubnetId=subnetid
        )