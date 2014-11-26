# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-REDUNDANCY-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:33 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( aristaMibs, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( TextualConvention, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp")

# Types

class AristaRedundancyProtocol(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,0,3,1,)
    namedValues = NamedValues(("unknown", 0), ("simplex", 1), ("rpr", 2), ("sso", 3), )
    
class AristaRedundancyState(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,0,3,2,)
    namedValues = NamedValues(("unknown", 0), ("standby", 1), ("active", 2), ("disabled", 3), )
    

# Objects

aristaRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 8)).setRevisions(("2012-11-10 22:37",))
if mibBuilder.loadTexts: aristaRedundancyMIB.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaRedundancyMIB.setContactInfo("Arista Networks, Inc.\n\nPostal: 5470 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@aristanetworks.com")
if mibBuilder.loadTexts: aristaRedundancyMIB.setDescription("This MIB module provides configuration and status\ninformation pertaining to high availability or redundancy \ninfrastructure on Arista devices.\n\nAs such, this MIB module is aimed at providing relevant\ninformation on 'Modular Systems' which support dual\nsupervisors for control plane redundancy.\n\nEach of the dual supervisors are referred to as 'unit'\nin the module.")
aristaRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0))
aristaRedundancyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0))
aristaRedundancyProtocolConfig = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 1), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolConfig.setDescription("Indicates the configured redundancy protocol in\nthe system.")
aristaRedundancyProtocolOper = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 2), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolOper.setDescription("Indicates the operational redundancy protocol\nin the system.")
aristaRedundancyUnitStateTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3))
if mibBuilder.loadTexts: aristaRedundancyUnitStateTable.setDescription("This table contains the current redundancy\nstate information for the units in the system.")
aristaRedundancyUnitStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1)).setIndexNames((0, "ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitId"))
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntry.setDescription("An entry containing redundancy state\ninformation for a unit.")
aristaRedundancyUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: aristaRedundancyUnitId.setDescription("A unique identifier representing a unit. \nUsually it is the slot number of the inserted unit on \nthe given modular system.")
aristaRedundancyUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 2), AristaRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitState.setDescription("The current state of the given unit.")
aristaRedundancyUnitStateEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntryTime.setDescription("The value of sysUpTime when the unit entered\nthe given state.")
aristaRedundancyLastSwOverReason = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyLastSwOverReason.setDescription("The reason for the last switchover in the system.")
aristaRedundancyHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 1))
aristaRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1))
aristaRedundancyNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0))
aristaRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2))
aristaRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1))
aristaRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2))

# Augmentions

# Notifications

aristaRedundancySwitchOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0, 1)).setObjects(*(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ) )
if mibBuilder.loadTexts: aristaRedundancySwitchOverNotif.setDescription("A switchover notification is generated whenever a unit\nbecomes active and it has taken over the control\nplane duties.")

# Groups

aristaRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 1)).setObjects(*(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolConfig"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitState"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolOper"), ) )
if mibBuilder.loadTexts: aristaRedundancyStatusGroup.setDescription("The collection of objects that represent the redundancy\nstatus of the system.")
aristaRedundancyNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 2)).setObjects(*(("ARISTA-REDUNDANCY-MIB", "aristaRedundancySwitchOverNotif"), ) )
if mibBuilder.loadTexts: aristaRedundancyNotificationsGroup.setDescription("The collection of notifications generated by the system on\nredundancy change events.")

# Compliances

aristaRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1, 1)).setObjects(*(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyNotificationsGroup"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyStatusGroup"), ) )
if mibBuilder.loadTexts: aristaRedundancyCompliance.setDescription("The compliance statement for Arista switches that\nsupport Redundancy MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", PYSNMP_MODULE_ID=aristaRedundancyMIB)

# Types
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", AristaRedundancyProtocol=AristaRedundancyProtocol, AristaRedundancyState=AristaRedundancyState)

# Objects
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancyMIB=aristaRedundancyMIB, aristaRedundancyObjects=aristaRedundancyObjects, aristaRedundancyStatus=aristaRedundancyStatus, aristaRedundancyProtocolConfig=aristaRedundancyProtocolConfig, aristaRedundancyProtocolOper=aristaRedundancyProtocolOper, aristaRedundancyUnitStateTable=aristaRedundancyUnitStateTable, aristaRedundancyUnitStateEntry=aristaRedundancyUnitStateEntry, aristaRedundancyUnitId=aristaRedundancyUnitId, aristaRedundancyUnitState=aristaRedundancyUnitState, aristaRedundancyUnitStateEntryTime=aristaRedundancyUnitStateEntryTime, aristaRedundancyLastSwOverReason=aristaRedundancyLastSwOverReason, aristaRedundancyHistory=aristaRedundancyHistory, aristaRedundancyNotifications=aristaRedundancyNotifications, aristaRedundancyNotificationPrefix=aristaRedundancyNotificationPrefix, aristaRedundancyConformance=aristaRedundancyConformance, aristaRedundancyCompliances=aristaRedundancyCompliances, aristaRedundancyGroups=aristaRedundancyGroups)

# Notifications
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancySwitchOverNotif=aristaRedundancySwitchOverNotif)

# Groups
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancyStatusGroup=aristaRedundancyStatusGroup, aristaRedundancyNotificationsGroup=aristaRedundancyNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancyCompliance=aristaRedundancyCompliance)