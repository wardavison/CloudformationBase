""" baseVPC class
"""

from troposphere import Join, Parameter
from troposphere.ec2 import VPC, Tag, Subnet, InternetGateway, \
    VPCGatewayAttachment, RouteTable, Route, SubnetRouteTableAssociation, \
    NetworkAcl, NetworkAclEntry, PortRange, SubnetNetworkAclAssociation


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

    @staticmethod
    def res_internet_gateway(title):
        """
        :param title: Title for the JSON InternetGateway resource (string)
        :return: Troposphere Internet Gateway object
        """
        return InternetGateway(title)

    @staticmethod
    def res_vpc_gateway_attachment(title, gatewayid, vpcid):
        """
        :param title: Title for the JSON VPCGatewayAttachment resource (string)
        :param gatewayid: ID of the InternetGateway resource (string)
        :param vpcid: ID of the VPC the Gateway should be attached to (string)
        :return: Troposphere VPCGatewayAttachment object
        """
        return VPCGatewayAttachment(
            title,
            InternetGatewayId=gatewayid,
            VpcId=vpcid
        )

    @staticmethod
    def res_route_table(title, vpcid, projectname, environmentname, namesuffix):
        """
        :param title: Title for the JSON RouteTable resource (string)
        :param vpcid: ID of the VPC the RouteTable should be created in (string)
        :param projectname: Name of project (used to form name) (string)
        :param environmentname: Name of environment (used to form name) (string)
        :param namesuffix: Display name suffix for the RouteTable (string)
        :return: Troposphere RouteTable object
        """
        return RouteTable(
            title,
            VpcId=vpcid,
            Tags=[Tag('Name', Join('', [projectname,
                                        '-',
                                        environmentname,
                                        '-',
                                        namesuffix]))],
        )

    @staticmethod
    def res_route(title, destcidrblock, gatewayid, routetableid,
                  vpcgatewayattachmenttitle):
        """
        :param title: Title for the JSON Route resource (string)
        :param destcidrblock: CIDR block for the destination match. (string)
        :param gatewayid: ID of the InternetGateway (string)
        :param routetableid: ID of the RouteTable to add this Route to (string)
        :param vpcgatewayattachmenttitle: Required for DependsOn (string)
        :return: Troposphere Route object
        """
        return Route(
            title,
            DestinationCidrBlock=destcidrblock,
            GatewayId=gatewayid,
            RouteTableId=routetableid,
            DependsOn=vpcgatewayattachmenttitle
        )

    @staticmethod
    def res_subnet_routetable_association(title, routetableid, subnetid):
        """
        :param title: Title for the JSON SubnetRouteTableAssociation resource
        :param routetableid: ID of the RouteTable to associate (string)
        :param subnetid: ID of the Subnet to associate (string)
        :return: Troposphere SubnetRouteTableAssociation object
        """
        return SubnetRouteTableAssociation(
            title,
            RouteTableId=routetableid,
            SubnetId=subnetid
        )

    @staticmethod
    def res_networkacl(title, vpcid, projectname, environmentname, namesuffix):
        """
        :param title: Title for the JSON NetworkAcl resource (string)
        :param vpcid: ID of the VPC the NetworkAcl should be created in (string)
        :param projectname: Name of project (used to form name) (string)
        :param environmentname: Name of environment (used to form name) (string)
        :param namesuffix: Display name suffix for the NetworkAcl (string)
        :return: Troposphere NetworkAcl object
        """
        return NetworkAcl(
            title,
            VpcId=vpcid,
            Tags=[Tag('Name', Join('', [projectname,
                                        '-',
                                        environmentname,
                                        '-',
                                        namesuffix]))],
        )

    @staticmethod
    def res_networkaclentry(title, cidrblock, egress, naclid, portrange,
                            protocol, action, rulenumber):
        """
        :param title: Title for the JSON NetworkAclEntry resource (string)
        :param cidrblock: The CIDR range to allow or deny (string)
        :param egress: Egress (true) or ingress (false) (boolean)
        :param naclid: ID of the ACL where the entry will be created. (string)
        :param portrange: The range of port numbers (EC2 PortRange Property)
        :param protocol: IP protocol the rule applies to. (number)
        :param action: allow or deny (string)
        :param rulenumber: rule order number (number)
        :return: Troposphere NetworkAclEntry object
        """
        return NetworkAclEntry(
            title,
            CidrBlock=cidrblock,
            Egress=egress,
            NetworkAclId=naclid,
            PortRange=portrange,
            Protocol=protocol,
            RuleAction=action,
            RuleNumber=rulenumber
        )

    @staticmethod
    def res_subnet_networkacl_association(title, networkaclid, subnetid):
        """
        :param title: Title for the JSON SubnetNetworkAclAssociation resource
        :param networkaclid: ID of the NetworkAcl to associate (string)
        :param subnetid: ID of the Subnet to associate (string)
        :return: Troposphere SubnetNetworkAclAssociation object
        """
        return SubnetNetworkAclAssociation(
            title,
            NetworkAclId=networkaclid,
            SubnetId=subnetid
        )

    @staticmethod
    def portrange(fromport, toport):
        """
        :param fromport: The start of the port range (integer)
        :param toport: The end of the port range (integer)
        :return: Troposphere PortRange parameter
        """
        return PortRange(
            From=fromport,
            To=toport
        )