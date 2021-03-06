# PySNMP SMI module. Autogenerated from smidump -f python POWER-ETHERNET-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:07 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue")

# Objects

powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 105)).setRevisions(("2003-11-24 00:00",))
if mibBuilder.loadTexts: powerEthernetMIB.setOrganization("IETF Ethernet Interfaces and Hub MIB\nWorking Group")
if mibBuilder.loadTexts: powerEthernetMIB.setContactInfo("\nWG Charter:\nhttp://www.ietf.org/html.charters/hubmib-charter.html\n\nMailing lists:\nGeneral Discussion: hubmib@ietf.org\nTo Subscribe: hubmib-requests@ietf.org\nIn Body: subscribe your_email_address\n\nChair: Dan Romascanu\nAvaya\nTel:  +972-3-645-8414\nEmail: dromasca@avaya.com\n\nEditor: Avi Berger\nPowerDsine Inc.\nTel:    972-9-7755100 Ext 307\nFax:    972-9-7755120\nE-mail: avib@PowerDsine.com")
if mibBuilder.loadTexts: powerEthernetMIB.setDescription("The MIB module for managing Power Source Equipment\n(PSE) working according to the IEEE 802.af Powered\nEthernet (DTE Power via MDI) standard.\n\n The following terms are used throughout this\n MIB module.  For complete formal definitions,\n the IEEE 802.3 standards should be consulted\n wherever possible:\n\n Group - A recommended, but optional, entity\n defined by the IEEE 802.3 management standard,\n in order to support a modular numbering scheme.\n The classical example allows an implementor to\n represent field-replaceable units as groups of\n ports, with the port numbering matching the\n modular hardware implementation.\n\nPort - This entity identifies the port within the group\nfor which this entry contains information.  The numbering\nscheme for ports is implementation specific.\n\nCopyright (c) The Internet Society (2003).  This version\nof this MIB module is part of RFC 3621; See the RFC\nitself for full legal notices.")
pethNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 0))
pethObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1))
pethPsePortTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 1))
if mibBuilder.loadTexts: pethPsePortTable.setDescription("A table of objects that display and control the power\ncharacteristics of power Ethernet ports on a Power Source\nEntity (PSE) device.  This group will be implemented in\nmanaged power Ethernet switches and mid-span devices.\nValues of all read-write objects in this table are\npersistent at restart/reboot.")
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 1, 1)).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: pethPsePortEntry.setDescription("A set of objects that display and control the power\ncharacteristics of a power Ethernet PSE port.")
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pethPsePortGroupIndex.setDescription("This variable uniquely identifies the group\ncontaining the port to which a power Ethernet PSE is\nconnected.  Group means box in the stack, module in a\nrack and the value 1 MUST be used for non-modular devices.\nFurthermore, the same value MUST be used in this variable,\npethMainPseGroupIndex, and pethNotificationControlGroupIndex\nto refer to a given box in a stack or module in the rack.")
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pethPsePortIndex.setDescription("This variable uniquely identifies the power Ethernet PSE\nport within group pethPsePortGroupIndex to which the\npower Ethernet PSE entry is connected.")
pethPsePortAdminEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortAdminEnable.setDescription("true (1) An interface which can provide the PSE functions.\nfalse(2) The interface will act as it would if it had no PSE\nfunction.")
pethPsePortPowerPairsControlAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerPairsControlAbility.setDescription("Describes the capability of controlling the power pairs\nfunctionality to switch pins for sourcing power.\nThe value true indicate that the device has the capability\nto control the power pairs.  When false the PSE Pinout\nAlternative used cannot be controlled through the\nPethPsePortAdminEnable attribute.")
pethPsePortPowerPairs = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("signal", 1), ("spare", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPairs.setDescription("Describes or controls the pairs in use.  If the value of\npethPsePortPowerPairsControl is true, this object is\nwritable.\nA value of signal(1) means that the signal pairs\nonly are in use.\nA value of spare(2) means that the spare pairs\nonly are in use.")
pethPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(6,4,2,3,1,5,)).subtype(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDetectionStatus.setDescription("Describes the operational status of the port PD detection.\nA value of disabled(1)- indicates that the PSE State diagram\nis in the state DISABLED.\nA value of deliveringPower(3) - indicates that the PSE State\ndiagram is in the state POWER_ON for a duration greater than\ntlim max (see IEEE Std 802.3af Table 33-5 tlim).\nA value of fault(4) - indicates that the PSE State diagram is\nin the state TEST_ERROR.\nA value of test(5) - indicates that the PSE State diagram is\nin the state TEST_MODE.\nA value of otherFault(6) - indicates that the PSE State\ndiagram is in the state IDLE due to the variable\nerror_conditions.\nA value of searching(2)- indicates the PSE State diagram is\nin a state other than those listed above.")
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPriority.setDescription("This object controls the priority of the port from the point\nof view of a power management algorithm.  The priority that\nis set by this variable could be used by a control mechanism\nthat prevents over current situations by disconnecting first\nports with lower power priority.  Ports that connect devices\ncritical to the operation of the network - like the E911\ntelephones ports - should be set to higher priority.")
pethPsePortMPSAbsentCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortMPSAbsentCounter.setDescription("This counter is incremented when the PSE state diagram\ntransitions directly from the state POWER_ON to the\n\n\n\nstate IDLE due to tmpdo_timer_done being asserted.")
pethPsePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortType.setDescription("A manager will set the value of this variable to indicate\nthe type of powered device that is connected to the port.\nThe default value supplied by the agent if no value has\never been set should be a zero-length octet string.")
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 10), Integer().subtype(subtypeSpec=SingleValueConstraint(5,3,4,1,2,)).subtype(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setDescription("Classification is a way to tag different terminals on the\nPower over LAN network according to their power consumption.\nDevices such as IP telephones, WLAN access points and others,\nwill be classified according to their power requirements.\n\nThe meaning of the classification labels is defined in the\nIEEE specification.\n\nThis variable is valid only while a PD is being powered,\nthat is, while the attribute pethPsePortDetectionStatus\nis reporting the enumeration deliveringPower.")
pethPsePortInvalidSignatureCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortInvalidSignatureCounter.setDescription("This counter is incremented when the PSE state diagram\nenters the state SIGNATURE_INVALID.")
pethPsePortPowerDeniedCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerDeniedCounter.setDescription("This counter is incremented when the PSE state diagram\nenters the state POWER_DENIED.")
pethPsePortOverLoadCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortOverLoadCounter.setDescription("This counter is incremented when the PSE state diagram\nenters the state ERROR_DELAY_OVER.")
pethPsePortShortCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortShortCounter.setDescription("This counter is incremented when the PSE state diagram\nenters the state ERROR_DELAY_SHORT.")
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 3, 1))
if mibBuilder.loadTexts: pethMainPseTable.setDescription("A table of objects that display and control attributes\nof the main power source in a PSE  device.  Ethernet\nswitches are one example of boxes that would support\nthese objects.\nValues of all read-write objects in this table are\npersistent at restart/reboot.")
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1)).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: pethMainPseEntry.setDescription("A set of objects that display and control the Main\npower of a PSE. ")
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pethMainPseGroupIndex.setDescription("This variable uniquely identifies the group to which\npower Ethernet PSE is connected.  Group means (box in\nthe stack, module in a rack) and the value 1 MUST be\nused for non-modular devices.  Furthermore, the same\nvalue MUST be used in this variable, pethPsePortGroupIndex,\nand pethNotificationControlGroupIndex to refer to a\ngiven box in a stack or module in a rack.")
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPsePower.setDescription("The nominal power of the PSE expressed in Watts.")
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseOperStatus.setDescription("The operational status of the main PSE.")
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setDescription("Measured usage power expressed in Watts.")
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setDescription("The usage threshold expressed in percents for\ncomparing the measured power and initiating\nan alarm if the threshold is exceeded.")
pethNotificationControl = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 4))
pethNotificationControlTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 4, 1))
if mibBuilder.loadTexts: pethNotificationControlTable.setDescription("A table of objects that display and control the\nNotification on a PSE  device.\nValues of all read-write objects in this table are\npersistent at restart/reboot.")
pethNotificationControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1)).setIndexNames((0, "POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"))
if mibBuilder.loadTexts: pethNotificationControlEntry.setDescription("A set of objects that control the Notification events.")
pethNotificationControlGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: pethNotificationControlGroupIndex.setDescription("This variable uniquely identifies the group.  Group\nmeans box in the stack, module in a rack and the value\n1 MUST be used for non-modular devices.  Furthermore,\nthe same value MUST be used in this variable,\npethPsePortGroupIndex, and\npethMainPseGroupIndex to refer to a given box in a\nstack or module in a rack. ")
pethNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethNotificationControlEnable.setDescription("This object controls, on a per-group basis, whether\nor not notifications from the agent are enabled.  The\nvalue true(1) means that notifications are enabled; the\nvalue false(2) means that they are not.")
pethConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2))
pethCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 2))

# Augmentions

# Notifications

pethPsePortOnOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 1)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ) )
if mibBuilder.loadTexts: pethPsePortOnOffNotification.setDescription(" This Notification indicates if Pse Port is delivering or\nnot power to the PD.  This Notification SHOULD be sent on\nevery status change except in the searching mode.\nAt least 500 msec must elapse between notifications\nbeing emitted by the same object instance.")
pethMainPowerUsageOnNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 2)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ) )
if mibBuilder.loadTexts: pethMainPowerUsageOnNotification.setDescription(" This Notification indicate PSE Threshold usage\nindication is on, the usage power is above the\nthreshold.  At least 500 msec must elapse between\nnotifications being emitted by the same object\ninstance.")
pethMainPowerUsageOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 3)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ) )
if mibBuilder.loadTexts: pethMainPowerUsageOffNotification.setDescription(" This Notification indicates PSE Threshold usage indication\noff, the usage power is below the threshold.\nAt least 500 msec must elapse between notifications being\nemitted by the same object instance.")

# Groups

pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 1)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortShortCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerDeniedCounter"), ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ("POWER-ETHERNET-MIB", "pethPsePortType"), ("POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"), ("POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"), ("POWER-ETHERNET-MIB", "pethPsePortInvalidSignatureCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPriority"), ("POWER-ETHERNET-MIB", "pethPsePortAdminEnable"), ("POWER-ETHERNET-MIB", "pethPsePortOverLoadCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairs"), ) )
if mibBuilder.loadTexts: pethPsePortGroup.setDescription("PSE Port objects.")
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 2)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"), ("POWER-ETHERNET-MIB", "pethMainPseOperStatus"), ("POWER-ETHERNET-MIB", "pethMainPsePower"), ("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ) )
if mibBuilder.loadTexts: pethMainPseGroup.setDescription("Main PSE Objects. ")
pethNotificationControlGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 3)).setObjects(*(("POWER-ETHERNET-MIB", "pethNotificationControlEnable"), ) )
if mibBuilder.loadTexts: pethNotificationControlGroup.setDescription("Notification Control  Objects. ")
pethPsePortNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 4)).setObjects(*(("POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"), ) )
if mibBuilder.loadTexts: pethPsePortNotificationGroup.setDescription("Pse Port Notifications.")
pethMainPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 5)).setObjects(*(("POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"), ("POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"), ) )
if mibBuilder.loadTexts: pethMainPowerNotificationGroup.setDescription("Main PSE Notifications.")

# Compliances

pethCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 105, 2, 1, 1)).setObjects(*(("POWER-ETHERNET-MIB", "pethNotificationControlGroup"), ("POWER-ETHERNET-MIB", "pethMainPowerNotificationGroup"), ("POWER-ETHERNET-MIB", "pethMainPseGroup"), ("POWER-ETHERNET-MIB", "pethPsePortNotificationGroup"), ("POWER-ETHERNET-MIB", "pethPsePortGroup"), ) )
if mibBuilder.loadTexts: pethCompliance.setDescription("Describes the requirements for conformance to the\nPower Ethernet MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", PYSNMP_MODULE_ID=powerEthernetMIB)

# Objects
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", powerEthernetMIB=powerEthernetMIB, pethNotifications=pethNotifications, pethObjects=pethObjects, pethPsePortTable=pethPsePortTable, pethPsePortEntry=pethPsePortEntry, pethPsePortGroupIndex=pethPsePortGroupIndex, pethPsePortIndex=pethPsePortIndex, pethPsePortAdminEnable=pethPsePortAdminEnable, pethPsePortPowerPairsControlAbility=pethPsePortPowerPairsControlAbility, pethPsePortPowerPairs=pethPsePortPowerPairs, pethPsePortDetectionStatus=pethPsePortDetectionStatus, pethPsePortPowerPriority=pethPsePortPowerPriority, pethPsePortMPSAbsentCounter=pethPsePortMPSAbsentCounter, pethPsePortType=pethPsePortType, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethPsePortInvalidSignatureCounter=pethPsePortInvalidSignatureCounter, pethPsePortPowerDeniedCounter=pethPsePortPowerDeniedCounter, pethPsePortOverLoadCounter=pethPsePortOverLoadCounter, pethPsePortShortCounter=pethPsePortShortCounter, pethMainPseObjects=pethMainPseObjects, pethMainPseTable=pethMainPseTable, pethMainPseEntry=pethMainPseEntry, pethMainPseGroupIndex=pethMainPseGroupIndex, pethMainPsePower=pethMainPsePower, pethMainPseOperStatus=pethMainPseOperStatus, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethNotificationControl=pethNotificationControl, pethNotificationControlTable=pethNotificationControlTable, pethNotificationControlEntry=pethNotificationControlEntry, pethNotificationControlGroupIndex=pethNotificationControlGroupIndex, pethNotificationControlEnable=pethNotificationControlEnable, pethConformance=pethConformance, pethCompliances=pethCompliances, pethGroups=pethGroups)

# Notifications
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethPsePortOnOffNotification=pethPsePortOnOffNotification, pethMainPowerUsageOnNotification=pethMainPowerUsageOnNotification, pethMainPowerUsageOffNotification=pethMainPowerUsageOffNotification)

# Groups
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethPsePortGroup=pethPsePortGroup, pethMainPseGroup=pethMainPseGroup, pethNotificationControlGroup=pethNotificationControlGroup, pethPsePortNotificationGroup=pethPsePortNotificationGroup, pethMainPowerNotificationGroup=pethMainPowerNotificationGroup)

# Compliances
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethCompliance=pethCompliance)
