# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-USER-AAA-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:57 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressPrefixLength, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType")
( Ipv6Address, Ipv6AddressIfIdentifier, Ipv6AddressPrefix, ) = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address", "Ipv6AddressIfIdentifier", "Ipv6AddressPrefix")
( EnabledStatus, ) = mibBuilder.importSymbols("JUNIPER-MIMSTP-MIB", "EnabledStatus")
( jnxUserAAAMibRoot, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxUserAAAMibRoot")
( Bits, Counter32, Counter64, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")

# Types

class JnxAccountingType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(0,1,5,3,2,4,)
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5), )
    
class JnxAuthenticateType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(0,1,5,3,2,4,)
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5), )
    
class JnxAuthorizationType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(0,1,5,3,2,4,)
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5), )
    
class JnxProvisioningType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(0,1,5,3,2,4,)
    namedValues = NamedValues(("none", 0), ("radius", 1), ("local", 2), ("ldap", 3), ("securid", 4), ("jsrc", 5), )
    

# Objects

jnxUserAAAMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1)).setRevisions(("2013-03-18 00:00","2012-12-29 00:00","2010-12-08 00:00","2010-11-23 00:00","2010-02-09 11:10","2007-08-21 00:00","2007-05-14 00:00",))
if mibBuilder.loadTexts: jnxUserAAAMib.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxUserAAAMib.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\n\nE-mail: support@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: jnxUserAAAMib.setDescription("This module defines the objects pertaining to User authentication,\nauthorization and accounting")
jnxUserAAANotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0))
jnxUserAAAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1))
jnxUserAAAGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1))
jnxTotalAuthenticationRequests = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTotalAuthenticationRequests.setDescription("Total authentication requests received.")
jnxTotalAuthenticationResponses = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxTotalAuthenticationResponses.setDescription("Total authentication responses.")
jnxUserAAAAccessAuthStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2))
jnxUserAAAStatTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1))
if mibBuilder.loadTexts: jnxUserAAAStatTable.setDescription("This table exposes the user authentication statistics.")
jnxUserAAAStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1)).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAAStatAuthType"))
if mibBuilder.loadTexts: jnxUserAAAStatEntry.setDescription("Statistic entry collects for authentication.")
jnxUserAAAStatAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 1), JnxAuthenticateType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAAStatAuthType.setDescription("The entry indicates the authentication type.  It\nuniquely identifies the statistics counters related to\nits authentication.")
jnxUserAAAStatRequestReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAStatRequestReceived.setDescription("The number of request received.")
jnxUserAAAStatAccessAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAStatAccessAccepted.setDescription("The number of access granted.  It is an aggregated \nstatistics for this type of authenticaiton.")
jnxUserAAAStatAccessRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAStatAccessRejected.setDescription("This number of access request rejected.  It is an aggregated \nstatistics for this type of authentication.")
jnxUserAAATrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3))
jnxUserAAAServerName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3, 1), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxUserAAAServerName.setDescription("The server name which identifies the authentication server.")
jnxUserAAAAddressPoolName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3, 2), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxUserAAAAddressPoolName.setDescription("The address pool name which identifies the local address pool.")
jnxUserAAAAccessPool = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4))
jnxUserAAAAccessPoolGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1))
jnxUserAAAAccessPoolTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1))
if mibBuilder.loadTexts: jnxUserAAAAccessPoolTable.setDescription("The entries in this table specify the address pools.")
jnxUserAAAAccessPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1)).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAAAccessPoolIdent"))
if mibBuilder.loadTexts: jnxUserAAAAccessPoolEntry.setDescription("A read-only description of the local address pools.")
jnxUserAAAAccessPoolIdent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolIdent.setDescription("The address identifier key.")
jnxUserAAAAccessPoolRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolRoutingInstance.setDescription("The routing instance of the address pool.")
jnxUserAAAAccessPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolName.setDescription("The address pool name.")
jnxUserAAAAccessPoolLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolLinkName.setDescription("The address pool link name.")
jnxUserAAAAccessPoolFamilyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolFamilyType.setDescription("The family type of this pool.")
jnxUserAAAAccessPoolInetNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 6), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(2, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolInetNetwork.setDescription("The Match criteria for this pool. Network or Prefix")
jnxUserAAAAccessPoolInetPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 7), InetAddressPrefixLength()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolInetPrefixLength.setDescription("The Prefix Length for an IPv6 pool")
jnxUserAAAAccessPoolOutOfMemory = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolOutOfMemory.setDescription("The Number of times this pool has flagged an Out of Memory condition.")
jnxUserAAAAccessPoolOutOfAddresses = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolOutOfAddresses.setDescription("The Number of times this pool has flagged an Out of Address condition.")
jnxUserAAAAccessPoolAddressTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressTotal.setDescription("The total number of Addresses or prefixes in this pool.")
jnxUserAAAAccessPoolAddressesInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressesInUse.setDescription("The total number of Addresses or prefixes given out from this pool.")
jnxUserAAAAccessPoolAddressUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressUsage.setDescription("The percentage of addresses used in this pool or linked pool.\nIf this pool is the head of a linked chain of pools, this number\nreflects the Usage for the whole chain. Conversely, if this pool\nit part of a linked chain of pools but not the head of the chain,\nthe value will not be used.")
jnxUserAAAAccessPoolAddressUsageHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressUsageHigh.setDescription("The configured high percentage threshold of addresses used in this\npool or linked pool. An SNMP trap is generated when this threshold\nis exceeded. This trap will only be generated for unlinked pools or\npools that are the head of a linked chain of pools Conversely, if \nthis pool it part of a linked chain of pools but not the head of the\nchain, then no traps will be generated.")
jnxUserAAAAccessPoolAddressUsageAbate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessPoolAddressUsageAbate.setDescription("The configured abate percentage threshold of addresses used in this\npool or linked pool. An SNMP trap clear is generated when address use\nfalls below this threshold percentage. This trap will only be generated\nfor unlinked pools or pools that are the head of a linked chain of\npools Conversely, if this pool it part of a linked chain of pools but\nnot the head of the chain, then no traps will be generated.")
jnxUserAAAAssignment = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5))
jnxUserAAAGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1))
jnxUserAAADomainDelimiters = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainDelimiters.setDescription("The list of delimiters used to separate the user's name from the\nuser's domain in the username field.  The default is '@'.")
jnxUserAAADomainParseDirection = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("rightToLeft", 1), ("leftToRight", 2), )).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainParseDirection.setDescription("The direction in which the user's name is parsed: either search\nfor domain delimiter from left to right or right to left; first\ndelimiter marks boundry. The default is right to left.")
jnxUserAAADomain = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2))
jnxUserAAADomainTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1))
if mibBuilder.loadTexts: jnxUserAAADomainTable.setDescription("The entries in this table specify the assignment of a remote access\nuser to a logical system, based on the user's domain.")
jnxUserAAADomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1)).setIndexNames((1, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainName"))
if mibBuilder.loadTexts: jnxUserAAADomainEntry.setDescription("A specification of the logical system to which users on a specified\ndomain should be assigned.")
jnxUserAAADomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAADomainName.setDescription("The domain name uniquely identifying this entry.")
jnxUserAAADomainStripDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainStripDomain.setDescription("Enables/disables the domain name stripping feature, which causes\nthe system to strip the domain name before sending the\naccess-request to RADIUS for authentication.")
jnxUserAAADomainLogicalSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 3), DisplayString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainLogicalSystem.setDescription("The name of the logical system, which will be used by the AAA\nsubsystem for this session. If not specified, will be mapped to\ndefault.")
jnxUserAAADomainRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 4), DisplayString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainRoutingInstance.setDescription("The name of the routing instance, which will be used by the AAA\nsubsystem for this session. If not specified, will be mapped to\ndefault.")
jnxUserAAADomainAddrPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainAddrPoolName.setDescription("The configured the address-pool-name for the domain name.")
jnxUserAAADomainDynamicPorfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 6), DisplayString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainDynamicPorfile.setDescription("The configured dynamic-profile which will be used for this session\nupon succeeding validation.")
jnxUserAAADomainTargetLogicalSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTargetLogicalSystem.setDescription("The configured target logical-system that this session will need to\nbe mapped to. If not specified, will be mapped to default.")
jnxUserAAADomainTargetRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTargetRoutingInstance.setDescription("The configured routing-instance that this session will need to be\nmapped to.")
jnxUserAAADomainTunnelProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelProfile.setDescription("The associated tunnel profile.")
jnxUserAAADomainDynamicProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 10), DisplayString().clone('')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainDynamicProfile.setDescription("The configured dynamic-profile to be used for this session.")
jnxUserAAADomainTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2))
if mibBuilder.loadTexts: jnxUserAAADomainTunnelTable.setDescription("The entries in this table specify the tunnels associated with a\ndomain.")
jnxUserAAADomainTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1)).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainTunnelName"), (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainTunnelDefId"))
if mibBuilder.loadTexts: jnxUserAAADomainTunnelEntry.setDescription("A specification of the tunnels associated with a domain.")
jnxUserAAADomainTunnelName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelName.setDescription("The domain name associated with this entry.")
jnxUserAAADomainTunnelDefId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelDefId.setDescription("The tunnel definition id value associated with this entry.")
jnxUserAAADomainTunnelPreference = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelPreference.setDescription("The tunnel's preference value associated with this entry. ")
jnxUserAAADomainTunnelRemoteGwName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelRemoteGwName.setDescription("This name specifies the hostname expected from the peer (the LNS)\nwhen a tunnel is setup.")
jnxUserAAADomainTunnelRemoteGwAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelRemoteGwAddress.setDescription("IP address of LNS tunnel endpoint")
jnxUserAAADomainTunnelSourceGwName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelSourceGwName.setDescription("This name specifies the hostname expected from the peer (the LNS)\nwhen a tunnel is setup.")
jnxUserAAADomainTunnelSourceGwAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelSourceGwAddress.setDescription("The source address of the tunnel (overrides the default address for\nthis LS/RI.) ")
jnxUserAAADomainTunnelSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelSecret.setDescription("The tunnel password associated with this entry.")
jnxUserAAADomainTunnelLogicalSystems = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelLogicalSystems.setDescription("The logical systems associated with this entty.")
jnxUserAAADomainTunnelRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelRoutingInstance.setDescription("The routing instance associated with this entty.")
jnxUserAAADomainTunnelMedium = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 11), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("tunnelMediumIPv4", 1), ("tunnelMediumUnknown", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelMedium.setDescription("The tunnel medium associated with this entry.  The medium dictates\nthe format of the tunnel address.")
jnxUserAAADomainTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 12), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("tunnelL2tp", 1), ("tunnelUnknown", 2), ("tunnelL2f", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelType.setDescription("The tunnel type associated with this entry.")
jnxUserAAADomainTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelId.setDescription("The tunnel identifier associated with this entry.")
jnxUserAAADomainTunnelMaxSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainTunnelMaxSessions.setDescription("The maximum number of tunnel sessions allowed in this tunnel\nentry.")
jnxUserAAADomainPadnTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3))
if mibBuilder.loadTexts: jnxUserAAADomainPadnTable.setDescription("The entries in this table specify the PPPoE active discovery\nnetwork (PADN) parameters associated with a domain.")
jnxUserAAADomainPadnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1)).setIndexNames((0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainName"), (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainPadnIpAddress"), (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainPadnIpMask"))
if mibBuilder.loadTexts: jnxUserAAADomainPadnEntry.setDescription("A specification of the PPPoE active discovery network parameters\nassociated with a domain.")
jnxUserAAADomainPadnIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 1), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAADomainPadnIpAddress.setDescription("The IP address of this entry.")
jnxUserAAADomainPadnIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 2), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAADomainPadnIpMask.setDescription("The IP mask of this entry.")
jnxUserAAADomainPadnDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAADomainPadnDistance.setDescription("The administrative distance metric of this entry.")
jnxUserAAAAccessProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6))
jnxUserAAAAccessProfileGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1))
jnxUserAAAAccessProfileTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1))
if mibBuilder.loadTexts: jnxUserAAAAccessProfileTable.setDescription("The entries in this table specify the assignment of authentication\nmethods for a particular subscriber type.")
jnxUserAAAAccessProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1)).setIndexNames((1, "JUNIPER-USER-AAA-MIB", "jnxUserAAAAccessProfileName"))
if mibBuilder.loadTexts: jnxUserAAAAccessProfileEntry.setDescription("A specification of the authentication methods for a particular\nsubscriber type.")
jnxUserAAAAccessProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileName.setDescription("The access profile name.")
jnxUserAAAAccessProfileAuthenticationOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAuthenticationOrder.setDescription("The set of authentication mechanisms configured on this system.  Each\noctet in this object contains one of the values defined in the\nJnxAuthenticateType TEXTUAL-CONVENTION.\n\nThe system will sequence through each octet of this object starting at\noctet 1 and attempt to use the corresponding authentication protocol\ndefined by JnxAuthenticateType.\n\nIf an authentication protocol is configured and attempts to reach the\nauthentication server fail, the system will move to the next octet in\nthis object and retry the authentication in the form dictated by the\ncorresponding authentication protocoltype. The process of sequencing\nthru each octet will stop if the authentication server is successfully\ncontacted, or there are no more configured octets in this object.")
jnxUserAAAAccessProfileAccountingOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAccountingOrder.setDescription("The set of accounting mechanisms configured on this system.  Each\noctet in this object contains one of the values defined in the\nJnxAccountingType TEXTUAL-CONVENTION.\n\nThe system will sequence through each octet of this object starting at\noctet 1 and attempt to use the corresponding accounting protocol\ndefined by JnxAccountingType.\n\nIf an accounting protocol is configured and attempts to reach the\naccounting server fail, the system will move to the next octet in\nthis object and retry the accounting in the form dictated by the\ncorresponding accounting protocoltype. The process of sequencing\nthru each octet will stop if the accounting server is successfully\ncontacted, or there are no more configured octets in this object.")
jnxUserAAAAccessProfileAuthorizationOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAuthorizationOrder.setDescription("The set of accounting mechanisms configured on this system.  Each\noctet in this object contains one of the values defined in the\nJnxAuthorizationType TEXTUAL-CONVENTION.\n\nThe system will sequence through each octet of this object starting at\noctet 1 and attempt to use the corresponding accounting protocol\ndefined by JnxAuthorizationType.\n\nIf an accounting protocol is configured and attempts to reach the\naccounting server fail, the system will move to the next octet in\nthis object and retry the accounting in the form dictated by the\ncorresponding accounting protocoltype. The process of sequencing\nthru each octet will stop if the accounting server is successfully\ncontacted, or there are no more configured octets in this object.")
jnxUserAAAAccessProfileProvisioningOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileProvisioningOrder.setDescription("The set of provisioning mechanisms configured on this system.  Each\noctet in this object contains one of the values defined in the\nJnxProvisioningType TEXTUAL-CONVENTION.\n\nThe system will sequence through each octet of this object starting at\noctet 1 and attempt to use the corresponding accounting protocol\ndefined by JnxProvisioningType.\n\nIf an accounting protocol is configured and attempts to reach the\naccounting server fail, the system will move to the next octet in\nthis object and retry the accounting in the form dictated by the\ncorresponding accounting protocoltype. The process of sequencing\nthru each octet will stop if the accounting server is successfully\ncontacted, or there are no more configured octets in this object.")
jnxUserAAAAccessProfileAccStopOnFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAccStopOnFailure.setDescription("Enables/disables the Acct-Stop message if a user fails\nauthentication, but AAA-server grants access.")
jnxUserAAAAccessProfileAccStopOnDeny = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileAccStopOnDeny.setDescription("Enables/disables the Acct-Stop message if AAA-server denies\naccess.")
jnxUserAAAAccessProfileImmediateUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileImmediateUpdate.setDescription("Enables/disables the Acct-Update message on receipt of a\nAcct-response for the Acct-Start message.")
jnxUserAAAAccessProfileCoaImmediateUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileCoaImmediateUpdate.setDescription("Enables/disables the Acct-Update message on completion of\nprocessing a change of authorization.")
jnxUserAAAAccessProfileInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileInterval.setDescription("The interval in minutes between accounting updates(Interim-stats\noff, if not specified).")
jnxUserAAAAccessProfileStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 11), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("time", 0), ("volume-time", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxUserAAAAccessProfileStatType.setDescription("The type of statistics are collected. These are the configured\ntypes:\n   time         - the option to report only uptime\n   volume-time  - the option to report both volume and uptime")

# Augmentions

# Notifications

jnxAccessAuthServiceUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 1)).setObjects(*() )
if mibBuilder.loadTexts: jnxAccessAuthServiceUp.setDescription("An access authentication trap signifies that the \nspecified service has started. ")
jnxAccessAuthServiceDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 2)).setObjects(*() )
if mibBuilder.loadTexts: jnxAccessAuthServiceDown.setDescription("An access authentication trap signifies that the \nspecified service has been stopped.")
jnxAccessAuthServerDisabled = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 3)).setObjects(*(("JUNIPER-USER-AAA-MIB", "jnxUserAAAServerName"), ) )
if mibBuilder.loadTexts: jnxAccessAuthServerDisabled.setDescription("An access authentication trap signifies that \nthe External authentication server is not responding.")
jnxAccessAuthServerEnabled = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 4)).setObjects(*(("JUNIPER-USER-AAA-MIB", "jnxUserAAAServerName"), ) )
if mibBuilder.loadTexts: jnxAccessAuthServerEnabled.setDescription("An access authentication trap signifies that the \nAAA client has changed the status of the External authentication server to UP.")
jnxAccessAuthAddressPoolHighThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 5)).setObjects(*(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"), ) )
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolHighThreshold.setDescription("An access authentication trap signifies that \nthe address pool has reached its high threshold.")
jnxAccessAuthAddressPoolAbateThreshold = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 6)).setObjects(*(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"), ) )
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolAbateThreshold.setDescription("An access authentication trap signifies that \nthe address pool has reached its abate threshold")
jnxAccessAuthAddressPoolOutOfAddresses = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 7)).setObjects(*(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"), ) )
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolOutOfAddresses.setDescription("An access authentication trap signifies that \nan Out Of Addresses event occured on the pool.")
jnxAccessAuthAddressPoolOutOfMemory = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 8)).setObjects(*(("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName"), ) )
if mibBuilder.loadTexts: jnxAccessAuthAddressPoolOutOfMemory.setDescription("An access authentication trap signifies that \nan Out Of Memory event occured on the pool.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-USER-AAA-MIB", PYSNMP_MODULE_ID=jnxUserAAAMib)

# Types
mibBuilder.exportSymbols("JUNIPER-USER-AAA-MIB", JnxAccountingType=JnxAccountingType, JnxAuthenticateType=JnxAuthenticateType, JnxAuthorizationType=JnxAuthorizationType, JnxProvisioningType=JnxProvisioningType)

# Objects
mibBuilder.exportSymbols("JUNIPER-USER-AAA-MIB", jnxUserAAAMib=jnxUserAAAMib, jnxUserAAANotifications=jnxUserAAANotifications, jnxUserAAAObjects=jnxUserAAAObjects, jnxUserAAAGlobalStats=jnxUserAAAGlobalStats, jnxTotalAuthenticationRequests=jnxTotalAuthenticationRequests, jnxTotalAuthenticationResponses=jnxTotalAuthenticationResponses, jnxUserAAAAccessAuthStats=jnxUserAAAAccessAuthStats, jnxUserAAAStatTable=jnxUserAAAStatTable, jnxUserAAAStatEntry=jnxUserAAAStatEntry, jnxUserAAAStatAuthType=jnxUserAAAStatAuthType, jnxUserAAAStatRequestReceived=jnxUserAAAStatRequestReceived, jnxUserAAAStatAccessAccepted=jnxUserAAAStatAccessAccepted, jnxUserAAAStatAccessRejected=jnxUserAAAStatAccessRejected, jnxUserAAATrapVars=jnxUserAAATrapVars, jnxUserAAAServerName=jnxUserAAAServerName, jnxUserAAAAddressPoolName=jnxUserAAAAddressPoolName, jnxUserAAAAccessPool=jnxUserAAAAccessPool, jnxUserAAAAccessPoolGeneral=jnxUserAAAAccessPoolGeneral, jnxUserAAAAccessPoolTable=jnxUserAAAAccessPoolTable, jnxUserAAAAccessPoolEntry=jnxUserAAAAccessPoolEntry, jnxUserAAAAccessPoolIdent=jnxUserAAAAccessPoolIdent, jnxUserAAAAccessPoolRoutingInstance=jnxUserAAAAccessPoolRoutingInstance, jnxUserAAAAccessPoolName=jnxUserAAAAccessPoolName, jnxUserAAAAccessPoolLinkName=jnxUserAAAAccessPoolLinkName, jnxUserAAAAccessPoolFamilyType=jnxUserAAAAccessPoolFamilyType, jnxUserAAAAccessPoolInetNetwork=jnxUserAAAAccessPoolInetNetwork, jnxUserAAAAccessPoolInetPrefixLength=jnxUserAAAAccessPoolInetPrefixLength, jnxUserAAAAccessPoolOutOfMemory=jnxUserAAAAccessPoolOutOfMemory, jnxUserAAAAccessPoolOutOfAddresses=jnxUserAAAAccessPoolOutOfAddresses, jnxUserAAAAccessPoolAddressTotal=jnxUserAAAAccessPoolAddressTotal, jnxUserAAAAccessPoolAddressesInUse=jnxUserAAAAccessPoolAddressesInUse, jnxUserAAAAccessPoolAddressUsage=jnxUserAAAAccessPoolAddressUsage, jnxUserAAAAccessPoolAddressUsageHigh=jnxUserAAAAccessPoolAddressUsageHigh, jnxUserAAAAccessPoolAddressUsageAbate=jnxUserAAAAccessPoolAddressUsageAbate, jnxUserAAAAssignment=jnxUserAAAAssignment, jnxUserAAAGeneral=jnxUserAAAGeneral, jnxUserAAADomainDelimiters=jnxUserAAADomainDelimiters, jnxUserAAADomainParseDirection=jnxUserAAADomainParseDirection, jnxUserAAADomain=jnxUserAAADomain, jnxUserAAADomainTable=jnxUserAAADomainTable, jnxUserAAADomainEntry=jnxUserAAADomainEntry, jnxUserAAADomainName=jnxUserAAADomainName, jnxUserAAADomainStripDomain=jnxUserAAADomainStripDomain, jnxUserAAADomainLogicalSystem=jnxUserAAADomainLogicalSystem, jnxUserAAADomainRoutingInstance=jnxUserAAADomainRoutingInstance, jnxUserAAADomainAddrPoolName=jnxUserAAADomainAddrPoolName, jnxUserAAADomainDynamicPorfile=jnxUserAAADomainDynamicPorfile, jnxUserAAADomainTargetLogicalSystem=jnxUserAAADomainTargetLogicalSystem, jnxUserAAADomainTargetRoutingInstance=jnxUserAAADomainTargetRoutingInstance, jnxUserAAADomainTunnelProfile=jnxUserAAADomainTunnelProfile, jnxUserAAADomainDynamicProfile=jnxUserAAADomainDynamicProfile, jnxUserAAADomainTunnelTable=jnxUserAAADomainTunnelTable, jnxUserAAADomainTunnelEntry=jnxUserAAADomainTunnelEntry, jnxUserAAADomainTunnelName=jnxUserAAADomainTunnelName, jnxUserAAADomainTunnelDefId=jnxUserAAADomainTunnelDefId, jnxUserAAADomainTunnelPreference=jnxUserAAADomainTunnelPreference, jnxUserAAADomainTunnelRemoteGwName=jnxUserAAADomainTunnelRemoteGwName, jnxUserAAADomainTunnelRemoteGwAddress=jnxUserAAADomainTunnelRemoteGwAddress, jnxUserAAADomainTunnelSourceGwName=jnxUserAAADomainTunnelSourceGwName, jnxUserAAADomainTunnelSourceGwAddress=jnxUserAAADomainTunnelSourceGwAddress, jnxUserAAADomainTunnelSecret=jnxUserAAADomainTunnelSecret, jnxUserAAADomainTunnelLogicalSystems=jnxUserAAADomainTunnelLogicalSystems, jnxUserAAADomainTunnelRoutingInstance=jnxUserAAADomainTunnelRoutingInstance, jnxUserAAADomainTunnelMedium=jnxUserAAADomainTunnelMedium, jnxUserAAADomainTunnelType=jnxUserAAADomainTunnelType, jnxUserAAADomainTunnelId=jnxUserAAADomainTunnelId, jnxUserAAADomainTunnelMaxSessions=jnxUserAAADomainTunnelMaxSessions, jnxUserAAADomainPadnTable=jnxUserAAADomainPadnTable, jnxUserAAADomainPadnEntry=jnxUserAAADomainPadnEntry, jnxUserAAADomainPadnIpAddress=jnxUserAAADomainPadnIpAddress, jnxUserAAADomainPadnIpMask=jnxUserAAADomainPadnIpMask, jnxUserAAADomainPadnDistance=jnxUserAAADomainPadnDistance, jnxUserAAAAccessProfile=jnxUserAAAAccessProfile, jnxUserAAAAccessProfileGeneral=jnxUserAAAAccessProfileGeneral, jnxUserAAAAccessProfileTable=jnxUserAAAAccessProfileTable, jnxUserAAAAccessProfileEntry=jnxUserAAAAccessProfileEntry, jnxUserAAAAccessProfileName=jnxUserAAAAccessProfileName, jnxUserAAAAccessProfileAuthenticationOrder=jnxUserAAAAccessProfileAuthenticationOrder, jnxUserAAAAccessProfileAccountingOrder=jnxUserAAAAccessProfileAccountingOrder, jnxUserAAAAccessProfileAuthorizationOrder=jnxUserAAAAccessProfileAuthorizationOrder, jnxUserAAAAccessProfileProvisioningOrder=jnxUserAAAAccessProfileProvisioningOrder, jnxUserAAAAccessProfileAccStopOnFailure=jnxUserAAAAccessProfileAccStopOnFailure, jnxUserAAAAccessProfileAccStopOnDeny=jnxUserAAAAccessProfileAccStopOnDeny, jnxUserAAAAccessProfileImmediateUpdate=jnxUserAAAAccessProfileImmediateUpdate, jnxUserAAAAccessProfileCoaImmediateUpdate=jnxUserAAAAccessProfileCoaImmediateUpdate, jnxUserAAAAccessProfileInterval=jnxUserAAAAccessProfileInterval, jnxUserAAAAccessProfileStatType=jnxUserAAAAccessProfileStatType)

# Notifications
mibBuilder.exportSymbols("JUNIPER-USER-AAA-MIB", jnxAccessAuthServiceUp=jnxAccessAuthServiceUp, jnxAccessAuthServiceDown=jnxAccessAuthServiceDown, jnxAccessAuthServerDisabled=jnxAccessAuthServerDisabled, jnxAccessAuthServerEnabled=jnxAccessAuthServerEnabled, jnxAccessAuthAddressPoolHighThreshold=jnxAccessAuthAddressPoolHighThreshold, jnxAccessAuthAddressPoolAbateThreshold=jnxAccessAuthAddressPoolAbateThreshold, jnxAccessAuthAddressPoolOutOfAddresses=jnxAccessAuthAddressPoolOutOfAddresses, jnxAccessAuthAddressPoolOutOfMemory=jnxAccessAuthAddressPoolOutOfMemory)
