# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-RPS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxRPS, ) = mibBuilder.importSymbols("JUNIPER-EX-SMI", "jnxRPS")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")

# Types

class JnxRPSStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(2,3,0,4,6,1,5,)
    namedValues = NamedValues(("green", 0), ("red", 1), ("amber", 2), ("green-blink", 3), ("red-blink", 4), ("amber-blink", 5), ("off", 6), )
    

# Objects

jnxRPSMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1)).setRevisions(("2009-08-07 00:00","2007-08-29 00:00",))
if mibBuilder.loadTexts: jnxRPSMIBObjects.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxRPSMIBObjects.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxRPSMIBObjects.setDescription("This module contains definitions of management information for\nRedundant power supply.")
jnxRPSVersionTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1))
if mibBuilder.loadTexts: jnxRPSVersionTable.setDescription("A Table containing RPS Version details.")
jnxRPSVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1)).setIndexNames((0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"))
if mibBuilder.loadTexts: jnxRPSVersionEntry.setDescription("RPS Version details on a specific serial number.")
jnxRPSSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRPSSerialNumber.setDescription("The RPS Serial Number of the Chassis.")
jnxRPSModel = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSModel.setDescription("The RPS Model name of the Chassis.")
jnxRPSFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSFirmwareVersion.setDescription("The RPS Firmware version of the Chassis.")
jnxRPSUBootVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSUBootVersion.setDescription("The RPS UBoot verison of the Chassis.")
jnxRPSStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2))
if mibBuilder.loadTexts: jnxRPSStatusTable.setDescription("A table containing RPS Fan and System Status for each slot.")
jnxRPSStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2, 1)).setIndexNames((0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"))
if mibBuilder.loadTexts: jnxRPSStatusEntry.setDescription("Status information for each FAN and SYSTEM slot.")
jnxRPSFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2, 1, 1), JnxRPSStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSFanStatus.setDescription("The RPS Fan Status on the chassis .")
jnxRPSSystemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 2, 1, 2), JnxRPSStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSSystemStatus.setDescription("The RPS System Status on the Chassis.")
jnxRPSPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3))
if mibBuilder.loadTexts: jnxRPSPowerSupplyTable.setDescription("A table containing RPS Power Supply details.")
jnxRPSPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1)).setIndexNames((0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"), (0, "JUNIPER-RPS-MIB", "jnxRPSPowerSupplyIndex"))
if mibBuilder.loadTexts: jnxRPSPowerSupplyEntry.setDescription("Information about Power Supply Status and Description.")
jnxRPSPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRPSPowerSupplyIndex.setDescription("The RPS Power Supply Index of the Chassis corresponding to RPS node.")
jnxRPSPowerSupplySlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPowerSupplySlotId.setDescription("The RPS Power Supply Slot ID f the Chassis corresponding to RPS node.")
jnxRPSPowerSupplyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPowerSupplyStatus.setDescription("The RPS Power Supply Status of the Chassis corresponding to RPS node.")
jnxRPSPowerSupplyDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPowerSupplyDescription.setDescription("The RPS Power Supply Description of the Chassis corresponding to RPS node.")
jnxRPSLedPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4))
if mibBuilder.loadTexts: jnxRPSLedPortStatusTable.setDescription("A table containing RPS LED Status details.")
jnxRPSLedPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4, 1)).setIndexNames((0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"), (0, "JUNIPER-RPS-MIB", "jnxRPSLedPortIndex"))
if mibBuilder.loadTexts: jnxRPSLedPortStatusEntry.setDescription("LED Port status of each port.")
jnxRPSLedPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRPSLedPortIndex.setDescription("The RPS Led Port Index of the Chassis corresponding to RPS node.")
jnxRPSLedPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSLedPortStatus.setDescription("The RPS Led Port Status of the Chassis corresponding to RPS node.")
jnxRPSPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5))
if mibBuilder.loadTexts: jnxRPSPortStatusTable.setDescription("A table containing RPS Port Status details.")
jnxRPSPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1)).setIndexNames((0, "JUNIPER-RPS-MIB", "jnxRPSSerialNumber"), (0, "JUNIPER-RPS-MIB", "jnxRPSPortIndex"))
if mibBuilder.loadTexts: jnxRPSPortStatusEntry.setDescription("Port Priority and Status for each port .")
jnxRPSPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxRPSPortIndex.setDescription("The RPS Port Index of the Chassis corresponding to RPS node.")
jnxRPSPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPortId.setDescription("The RPS Port ID of the Chassis corresponding to RPS node.")
jnxRPSPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPortStatus.setDescription("The RPS Port Status of the Chassis corresponding to RPS node.")
jnxRPSPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPortPriority.setDescription("The RPS Port Priority of the Chassis corresponding to RPS node.")
jnxRPSPortPowerRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 6, 1, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxRPSPortPowerRequested.setDescription("The RPS Led Port Power Requested of the Chassis corresponding to RPS node.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-RPS-MIB", PYSNMP_MODULE_ID=jnxRPSMIBObjects)

# Types
mibBuilder.exportSymbols("JUNIPER-RPS-MIB", JnxRPSStatus=JnxRPSStatus)

# Objects
mibBuilder.exportSymbols("JUNIPER-RPS-MIB", jnxRPSMIBObjects=jnxRPSMIBObjects, jnxRPSVersionTable=jnxRPSVersionTable, jnxRPSVersionEntry=jnxRPSVersionEntry, jnxRPSSerialNumber=jnxRPSSerialNumber, jnxRPSModel=jnxRPSModel, jnxRPSFirmwareVersion=jnxRPSFirmwareVersion, jnxRPSUBootVersion=jnxRPSUBootVersion, jnxRPSStatusTable=jnxRPSStatusTable, jnxRPSStatusEntry=jnxRPSStatusEntry, jnxRPSFanStatus=jnxRPSFanStatus, jnxRPSSystemStatus=jnxRPSSystemStatus, jnxRPSPowerSupplyTable=jnxRPSPowerSupplyTable, jnxRPSPowerSupplyEntry=jnxRPSPowerSupplyEntry, jnxRPSPowerSupplyIndex=jnxRPSPowerSupplyIndex, jnxRPSPowerSupplySlotId=jnxRPSPowerSupplySlotId, jnxRPSPowerSupplyStatus=jnxRPSPowerSupplyStatus, jnxRPSPowerSupplyDescription=jnxRPSPowerSupplyDescription, jnxRPSLedPortStatusTable=jnxRPSLedPortStatusTable, jnxRPSLedPortStatusEntry=jnxRPSLedPortStatusEntry, jnxRPSLedPortIndex=jnxRPSLedPortIndex, jnxRPSLedPortStatus=jnxRPSLedPortStatus, jnxRPSPortStatusTable=jnxRPSPortStatusTable, jnxRPSPortStatusEntry=jnxRPSPortStatusEntry, jnxRPSPortIndex=jnxRPSPortIndex, jnxRPSPortId=jnxRPSPortId, jnxRPSPortStatus=jnxRPSPortStatus, jnxRPSPortPriority=jnxRPSPortPriority, jnxRPSPortPowerRequested=jnxRPSPortPowerRequested)

