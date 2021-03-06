# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-QOS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:32 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( aristaMibs, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")

# Types

class AristaQosMapType(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,1,)
    namedValues = NamedValues(("controlPlane", 1), ("dataPlane", 2), )
    
class AristaQosShortId(TextualConvention, OctetString):
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,40)
    

# Objects

aristaQosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 13)).setRevisions(("2013-06-01 00:00",))
if mibBuilder.loadTexts: aristaQosMib.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaQosMib.setContactInfo("Arista Networks, Inc.\n\nPostal: 5470 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@aristanetworks.com")
if mibBuilder.loadTexts: aristaQosMib.setDescription("**********************************\nOverview\n**********************************\nThis MIB provides read access to Quality of Service (QoS) \nconfiguration and statistics information for Arista \nplatforms.\n\nConfiguration information available through this MIB includes\nall class-map, policy-map, and service-policy parameters.  The\ndefinitions of these object types are given below.\n\nStatistics available through this MIB include dropped, sent and\nmatched packet counters per traffic class after any configured\nQoS policies are applied.  \n\n**********************************\nDefinitions\n**********************************\nClass map - A data structure that uses access-control lists\nto define a data stream.\n\nPolicy map - A data structure that associates class maps identifying \nspecific data streams with actions that control its transmission.\n\nAction - A traffic-management action that is applied to traffic\nclassified as belonging to a particular class. Actions may include\nmodifying CoS or DSCP fields, assigning to traffic-class queues,\nshaping, or filtering.")
aristaQosMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1))
aristaClassMapTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1))
if mibBuilder.loadTexts: aristaClassMapTable.setDescription("Lists the class maps configured on the system.")
aristaClassMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaClassMapType"))
if mibBuilder.loadTexts: aristaClassMapEntry.setDescription("A conceptual row in aristaClassMapTable.")
aristaClassMapId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 1), AristaQosShortId()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaClassMapId.setDescription("Bounded-length identifier for a given class map, derived from\nthe class map's name.")
aristaClassMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 2), AristaQosMapType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaClassMapType.setDescription("Type of a given class map.")
aristaClassMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapName.setDescription("Name of a given class map.")
aristaClassMapMatchCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("matchConditionAny", 1), ("matchConditionAll", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapMatchCondition.setDescription("Indicates how many match criteria traffic must match in order to\nbelong to a class with multiple match critera.")
aristaClassMapMatchTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2))
if mibBuilder.loadTexts: aristaClassMapMatchTable.setDescription("Describes the match criteria used to classify traffic as belonging\nto a class map.")
aristaClassMapMatchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaClassMapType"), (0, "ARISTA-QOS-MIB", "aristaClassMapMatchIndex"))
if mibBuilder.loadTexts: aristaClassMapMatchEntry.setDescription("A conceptual row in the aristaClassMapMatchTable.")
aristaClassMapMatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaClassMapMatchIndex.setDescription("This index identifies the position of a match criterion among all the\ncriteria for a class map.")
aristaClassMapMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("ipv4AccessGroup", 1), ("ipv6AccessGroup", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapMatchType.setDescription("Indicates whether a match criterion of a class map is an IPv4 or an\nIPv6 access-control list.")
aristaClassMapMatchName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaClassMapMatchName.setDescription("The name of the access-control list for a match criterion.")
aristaPolicyMapTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3))
if mibBuilder.loadTexts: aristaPolicyMapTable.setDescription("Lists the policy maps configured on the system.")
aristaPolicyMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"))
if mibBuilder.loadTexts: aristaPolicyMapEntry.setDescription("A conceptual row in aristaPolicyMapTable.")
aristaPolicyMapId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 1), AristaQosShortId()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaPolicyMapId.setDescription("Bounded-length identifier for a given policy map, derived from\nthe policy map's name.")
aristaPolicyMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 2), AristaQosMapType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaPolicyMapType.setDescription("Type of a given policy map.")
aristaPolicyMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapName.setDescription("Name of a given policy map.")
aristaPolicyMapClassTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4))
if mibBuilder.loadTexts: aristaPolicyMapClassTable.setDescription("Lists the classes associated with a given policy map.")
aristaPolicyMapClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapClassIndex"))
if mibBuilder.loadTexts: aristaPolicyMapClassEntry.setDescription("A conceptual row in aristaPolicyMapClassTable.")
aristaPolicyMapClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaPolicyMapClassIndex.setDescription("Determines the sequence in which traffic is matched\nto classes within a policy map. The class with the smallest\naristaPolicyMapClassIndex is given the first preference.\nClass Index values may not be consecutive.")
aristaPolicyMapClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 4, 1, 2), AristaQosShortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapClassId.setDescription("Identifier of the class map for a given class in a policy map.")
aristaPolicyMapActionTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5))
if mibBuilder.loadTexts: aristaPolicyMapActionTable.setDescription("Lists the actions that are applied to traffic classified\nas belonging to a particular class in a policy map.")
aristaPolicyMapActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"), (0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapActionType"))
if mibBuilder.loadTexts: aristaPolicyMapActionEntry.setDescription("A conceptual row in the aristaPolicyMapActionTable.")
aristaPolicyMapActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(3,4,2,5,1,)).subtype(namedValues=NamedValues(("actionSetShape", 1), ("actionSetBandwidth", 2), ("actionSetCos", 3), ("actionSetDscp", 4), ("actionSetTc", 5), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaPolicyMapActionType.setDescription("Type of a traffic-management action.\nFor example: If the action is 'set cos 5', then\nthe action type is 'actionSetCos'.")
aristaPolicyMapActionRateUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,0,)).subtype(namedValues=NamedValues(("rateUnitNone", 0), ("rateUnitPps", 1), ("rateUnitKbps", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapActionRateUnit.setDescription("Indicates the rate unit of shaping/bandwidth actions.\n\nrateUnitNone\n  - This action is not a shaping or bandwidth action.\nrateUnitPps\n  - Packets per second\nrateUnitKbps\n  - Kilobits per second")
aristaPolicyMapActionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaPolicyMapActionValue.setDescription("Value applied in a traffic-management action.\nFor example: If the action is 'set cos 5', then\naristaPolicyMapActionValue is 5.")
aristaServicePolicyTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6))
if mibBuilder.loadTexts: aristaServicePolicyTable.setDescription("Lists the policy maps currently applied to interfaces.")
aristaServicePolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaServicePolicyIfIndex"), (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"))
if mibBuilder.loadTexts: aristaServicePolicyEntry.setDescription("A conceptual row in the aristaServicePolicyTable.")
aristaServicePolicyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaServicePolicyIfIndex.setDescription("The index of interface to which a policy map is applied.")
aristaServicePolicyDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("input", 1), ("output", 2), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaServicePolicyDirection.setDescription("The direction of traffic for which the service policy applies.\n\ninput\n - The service policy applies to inbound traffic.\noutput\n  - The service policy applies to outbound traffic.")
aristaServicePolicyMapId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 3), AristaQosShortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaServicePolicyMapId.setDescription("Identifier of the policy map applied to the interface.")
aristaServicePolicyMapType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 6, 1, 4), AristaQosMapType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaServicePolicyMapType.setDescription("Type of the policy map applied to the interface.")
aristaQosStatsTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7))
if mibBuilder.loadTexts: aristaQosStatsTable.setDescription("An entry in this table contains dropped, sent and matched packet\ncounters for a given class of a policy map applied in a given direction.\n Counts are aggregated for all interfaces.")
aristaQosStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1)).setIndexNames((0, "ARISTA-QOS-MIB", "aristaPolicyMapId"), (0, "ARISTA-QOS-MIB", "aristaPolicyMapType"), (0, "ARISTA-QOS-MIB", "aristaClassMapId"), (0, "ARISTA-QOS-MIB", "aristaServicePolicyDirection"))
if mibBuilder.loadTexts: aristaQosStatsEntry.setDescription("A conceptual row in the aristaQosStatsTable.")
aristaQosPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaQosPktsDropped.setDescription("The number of packets dropped by a service policy.\nThis number is zero for classes of type dataPlane.")
aristaQosPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaQosPktsSent.setDescription("The number of packets classified by a service policy and allowed\nthrough.")
aristaQosPktsMatched = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 13, 1, 7, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaQosPktsMatched.setDescription("The number of packets classified by a service policy.\nEqual to the sum of aristaQosPktsDropped and aristaQosPktsSent.")
aristaQosMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2))
aristaQosMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 1))
aristaQosMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2))

# Augmentions

# Groups

aristaClassMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 1)).setObjects(*(("ARISTA-QOS-MIB", "aristaQosPktsMatched"), ("ARISTA-QOS-MIB", "aristaClassMapMatchName"), ("ARISTA-QOS-MIB", "aristaClassMapMatchCondition"), ("ARISTA-QOS-MIB", "aristaClassMapName"), ("ARISTA-QOS-MIB", "aristaQosPktsSent"), ("ARISTA-QOS-MIB", "aristaClassMapMatchType"), ("ARISTA-QOS-MIB", "aristaQosPktsDropped"), ("ARISTA-QOS-MIB", "aristaPolicyMapClassId"), ) )
if mibBuilder.loadTexts: aristaClassMapGroup.setDescription("The collection of objects that represent QoS configuration and\nstatistics information for class maps.")
aristaPolicyMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 2)).setObjects(*(("ARISTA-QOS-MIB", "aristaPolicyMapName"), ) )
if mibBuilder.loadTexts: aristaPolicyMapGroup.setDescription("The collection of objects that represent QoS configuration\ninformation for policy maps.")
aristaPolicyMapActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 3)).setObjects(*(("ARISTA-QOS-MIB", "aristaPolicyMapActionRateUnit"), ("ARISTA-QOS-MIB", "aristaPolicyMapActionValue"), ) )
if mibBuilder.loadTexts: aristaPolicyMapActionGroup.setDescription("The collection of objects that represent configuration\ninformation for QoS actions.")
aristaServicePolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 2, 4)).setObjects(*(("ARISTA-QOS-MIB", "aristaServicePolicyMapType"), ("ARISTA-QOS-MIB", "aristaServicePolicyMapId"), ) )
if mibBuilder.loadTexts: aristaServicePolicyGroup.setDescription("The collection of objects that represent QoS configuration\ninformation for service policies.")

# Compliances

aristaQosMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 13, 2, 1, 1)).setObjects(*(("ARISTA-QOS-MIB", "aristaClassMapGroup"), ("ARISTA-QOS-MIB", "aristaPolicyMapGroup"), ("ARISTA-QOS-MIB", "aristaServicePolicyGroup"), ("ARISTA-QOS-MIB", "aristaPolicyMapActionGroup"), ) )
if mibBuilder.loadTexts: aristaQosMibCompliance.setDescription("The compliance statement for Arista switches that\nsupport ARISTA-QOS-MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-QOS-MIB", PYSNMP_MODULE_ID=aristaQosMib)

# Types
mibBuilder.exportSymbols("ARISTA-QOS-MIB", AristaQosMapType=AristaQosMapType, AristaQosShortId=AristaQosShortId)

# Objects
mibBuilder.exportSymbols("ARISTA-QOS-MIB", aristaQosMib=aristaQosMib, aristaQosMibObjects=aristaQosMibObjects, aristaClassMapTable=aristaClassMapTable, aristaClassMapEntry=aristaClassMapEntry, aristaClassMapId=aristaClassMapId, aristaClassMapType=aristaClassMapType, aristaClassMapName=aristaClassMapName, aristaClassMapMatchCondition=aristaClassMapMatchCondition, aristaClassMapMatchTable=aristaClassMapMatchTable, aristaClassMapMatchEntry=aristaClassMapMatchEntry, aristaClassMapMatchIndex=aristaClassMapMatchIndex, aristaClassMapMatchType=aristaClassMapMatchType, aristaClassMapMatchName=aristaClassMapMatchName, aristaPolicyMapTable=aristaPolicyMapTable, aristaPolicyMapEntry=aristaPolicyMapEntry, aristaPolicyMapId=aristaPolicyMapId, aristaPolicyMapType=aristaPolicyMapType, aristaPolicyMapName=aristaPolicyMapName, aristaPolicyMapClassTable=aristaPolicyMapClassTable, aristaPolicyMapClassEntry=aristaPolicyMapClassEntry, aristaPolicyMapClassIndex=aristaPolicyMapClassIndex, aristaPolicyMapClassId=aristaPolicyMapClassId, aristaPolicyMapActionTable=aristaPolicyMapActionTable, aristaPolicyMapActionEntry=aristaPolicyMapActionEntry, aristaPolicyMapActionType=aristaPolicyMapActionType, aristaPolicyMapActionRateUnit=aristaPolicyMapActionRateUnit, aristaPolicyMapActionValue=aristaPolicyMapActionValue, aristaServicePolicyTable=aristaServicePolicyTable, aristaServicePolicyEntry=aristaServicePolicyEntry, aristaServicePolicyIfIndex=aristaServicePolicyIfIndex, aristaServicePolicyDirection=aristaServicePolicyDirection, aristaServicePolicyMapId=aristaServicePolicyMapId, aristaServicePolicyMapType=aristaServicePolicyMapType, aristaQosStatsTable=aristaQosStatsTable, aristaQosStatsEntry=aristaQosStatsEntry, aristaQosPktsDropped=aristaQosPktsDropped, aristaQosPktsSent=aristaQosPktsSent, aristaQosPktsMatched=aristaQosPktsMatched, aristaQosMibConformance=aristaQosMibConformance, aristaQosMibCompliances=aristaQosMibCompliances, aristaQosMibGroups=aristaQosMibGroups)

# Groups
mibBuilder.exportSymbols("ARISTA-QOS-MIB", aristaClassMapGroup=aristaClassMapGroup, aristaPolicyMapGroup=aristaPolicyMapGroup, aristaPolicyMapActionGroup=aristaPolicyMapActionGroup, aristaServicePolicyGroup=aristaServicePolicyGroup)

# Compliances
mibBuilder.exportSymbols("ARISTA-QOS-MIB", aristaQosMibCompliance=aristaQosMibCompliance)
