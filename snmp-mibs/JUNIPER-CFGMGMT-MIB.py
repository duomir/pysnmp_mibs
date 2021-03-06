# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-CFGMGMT-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:48 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxCmNotifications, jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxCmNotifications", "jnxMibs")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks")
( DateAndTime, DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")

# Types

class JnxCmCfChgSource(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(7,2,8,6,5,4,1,3,)
    namedValues = NamedValues(("other", 1), ("cli", 2), ("junoscript", 3), ("synchronize", 4), ("snmp", 5), ("button", 6), ("autoinstall", 7), ("unknown", 8), )
    
class JnxCmRescueCfgState(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,2,)
    namedValues = NamedValues(("nonexistant", 1), ("updated", 2), )
    

# Objects

jnxCfgMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 18)).setRevisions(("2003-11-19 00:00","2003-10-24 00:00","2003-10-24 00:00","2002-05-10 00:00",))
if mibBuilder.loadTexts: jnxCfgMgmt.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxCfgMgmt.setContactInfo("        Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxCfgMgmt.setDescription("This MIB module defines objects used for managing the \nconfiguration of Juniper products.")
jnxCmCfgChg = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1))
jnxCmCfgChgLatestIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgLatestIndex.setDescription("The index in jnxCmCfgChgEventTable for the latest configuration\nchange event.")
jnxCmCfgChgLatestTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgLatestTime.setDescription("The value of sysUpTime when the configuration was last \nchanged.\n\nIf the management subsystem was reset after the last\n	configuration change, this object will return 0.")
jnxCmCfgChgLatestDate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgLatestDate.setDescription("The date and time when the configuration was last changed.")
jnxCmCfgChgLatestSource = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 4), JnxCmCfChgSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgLatestSource.setDescription("The source of the configuration event.")
jnxCmCfgChgLatestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgLatestUser.setDescription("The name of the logged in user.  The length is zero if\nnot available or not applicable.")
jnxCmCfgChgMaxEventEntries = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgMaxEventEntries.setDescription("The maximum number of entries that can be held in\njnxCmCfgChgEventTable.")
jnxCmCfgChgEventTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7))
if mibBuilder.loadTexts: jnxCmCfgChgEventTable.setDescription("A table of configuration events on this router.")
jnxCmCfgChgEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1)).setIndexNames((0, "JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventIndex"))
if mibBuilder.loadTexts: jnxCmCfgChgEventEntry.setDescription("Information about a configuration event on this router.")
jnxCmCfgChgEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxCmCfgChgEventIndex.setDescription("This object identifies a specific configuration change\nevent.  Monotonically increasing values will be assigned\nby the snmp subsystem to each event as it occurs.  If the\nsnmp subsystem is reset, these index values will be reset\nas well.")
jnxCmCfgChgEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgEventTime.setDescription("The value of sysUpTime when the event occurred.")
jnxCmCfgChgEventDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgEventDate.setDescription("The system date and time when the event occurred.")
jnxCmCfgChgEventSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 4), JnxCmCfChgSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgEventSource.setDescription("The source of the configuration event.")
jnxCmCfgChgEventUser = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgEventUser.setDescription("The name of the logged in user.  The length is zero if\nnot available or not applicable.")
jnxCmCfgChgEventLog = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 18, 1, 7, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmCfgChgEventLog.setDescription("The log of the configuration event.  The length is zero\nif not available.")
jnxCmRescueChg = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 18, 2))
jnxCmRescueChgTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmRescueChgTime.setDescription("The value of sysUpTime when the rescue configuration was\nlast changed.\n\nIf the management subsystem was reset after the last\nconfiguration change, this object will return 0.")
jnxCmRescueChgDate = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmRescueChgDate.setDescription("The date and time when the rescue configuration was last\nchanged.")
jnxCmRescueChgSource = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 3), JnxCmCfChgSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmRescueChgSource.setDescription("The source of the rescue configuration event.")
jnxCmRescueChgUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmRescueChgUser.setDescription("The name of the logged in user.  The length is zero if\nnot available or not applicable.")
jnxCmRescueChgState = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 18, 2, 5), JnxCmRescueCfgState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxCmRescueChgState.setDescription("The current state of the rescue configuration.")
jnxCmNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 5, 0))

# Augmentions

# Notifications

jnxCmCfgChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 5, 0, 1)).setObjects(*(("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventTime"), ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventDate"), ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventUser"), ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventLog"), ("JUNIPER-CFGMGMT-MIB", "jnxCmCfgChgEventSource"), ) )
if mibBuilder.loadTexts: jnxCmCfgChange.setDescription("Notification of a configuration management event as\nrecorded in jnxCmCfgChgEventTable.")
jnxCmRescueChange = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 5, 0, 2)).setObjects(*(("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgUser"), ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgState"), ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgTime"), ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgSource"), ("JUNIPER-CFGMGMT-MIB", "jnxCmRescueChgDate"), ) )
if mibBuilder.loadTexts: jnxCmRescueChange.setDescription("Notification of the latest rescue configuration \nchange.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-CFGMGMT-MIB", PYSNMP_MODULE_ID=jnxCfgMgmt)

# Types
mibBuilder.exportSymbols("JUNIPER-CFGMGMT-MIB", JnxCmCfChgSource=JnxCmCfChgSource, JnxCmRescueCfgState=JnxCmRescueCfgState)

# Objects
mibBuilder.exportSymbols("JUNIPER-CFGMGMT-MIB", jnxCfgMgmt=jnxCfgMgmt, jnxCmCfgChg=jnxCmCfgChg, jnxCmCfgChgLatestIndex=jnxCmCfgChgLatestIndex, jnxCmCfgChgLatestTime=jnxCmCfgChgLatestTime, jnxCmCfgChgLatestDate=jnxCmCfgChgLatestDate, jnxCmCfgChgLatestSource=jnxCmCfgChgLatestSource, jnxCmCfgChgLatestUser=jnxCmCfgChgLatestUser, jnxCmCfgChgMaxEventEntries=jnxCmCfgChgMaxEventEntries, jnxCmCfgChgEventTable=jnxCmCfgChgEventTable, jnxCmCfgChgEventEntry=jnxCmCfgChgEventEntry, jnxCmCfgChgEventIndex=jnxCmCfgChgEventIndex, jnxCmCfgChgEventTime=jnxCmCfgChgEventTime, jnxCmCfgChgEventDate=jnxCmCfgChgEventDate, jnxCmCfgChgEventSource=jnxCmCfgChgEventSource, jnxCmCfgChgEventUser=jnxCmCfgChgEventUser, jnxCmCfgChgEventLog=jnxCmCfgChgEventLog, jnxCmRescueChg=jnxCmRescueChg, jnxCmRescueChgTime=jnxCmRescueChgTime, jnxCmRescueChgDate=jnxCmRescueChgDate, jnxCmRescueChgSource=jnxCmRescueChgSource, jnxCmRescueChgUser=jnxCmRescueChgUser, jnxCmRescueChgState=jnxCmRescueChgState, jnxCmNotificationsPrefix=jnxCmNotificationsPrefix)

# Notifications
mibBuilder.exportSymbols("JUNIPER-CFGMGMT-MIB", jnxCmCfgChange=jnxCmCfgChange, jnxCmRescueChange=jnxCmRescueChange)

