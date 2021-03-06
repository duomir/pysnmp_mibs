# PySNMP SMI module. Autogenerated from smidump -f python WLSX-IFEXT-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jun  3 12:42:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaDot1dState, ArubaEnableValue, ArubaIfType, ArubaOperStateValue, ArubaPoeState, ArubaPortDuplex, ArubaPortMode, ArubaPortSpeed, ArubaPortType, ArubaVlanValidRange, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaDot1dState", "ArubaEnableValue", "ArubaIfType", "ArubaOperStateValue", "ArubaPoeState", "ArubaPortDuplex", "ArubaPortMode", "ArubaPortSpeed", "ArubaPortType", "ArubaVlanValidRange")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Objects

wlsxIfExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3)).setRevisions(("2012-07-12 00:00","1910-01-26 18:06",))
if mibBuilder.loadTexts: wlsxIfExtMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxIfExtMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxIfExtMIB.setDescription("This MIB module defines MIB objects which provide\nSystem level information about the Aruba controller.")
wlsxIfExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1))
wlsxIfExtPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1))
if mibBuilder.loadTexts: wlsxIfExtPortTable.setDescription("\nThe table of processors contained by the controller. This table is\ndeprecated in favor of wlsxIfExtNPortTable.")
wlsxIfExtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1)).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtSlotNumber"), (0, "WLSX-IFEXT-MIB", "ifExtPortNumber"))
if mibBuilder.loadTexts: wlsxIfExtPortEntry.setDescription("\nAn entry for one processor contained by the controller.")
ifExtSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifExtSlotNumber.setDescription("\nThis object represents the Physical Slot of the Interface.")
ifExtPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 2), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifExtPortNumber.setDescription("\nThis object represents the Physical Port of the Interface. ")
ifExtPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortIfIndex.setDescription("\nThis is the ifIndex in ifTable, representing this slot and port. \nThis object is deprecated in favour of ifExtNPortIfIndex.")
ifExtAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 4), ArubaEnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtAdminState.setDescription("\nThe desired state of the interface. This object is deprecated in\nfavour of ifExtNAdminState.")
ifExtOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtOperState.setDescription("\nThe current operational state of the interface. This object is\ndeprecated in favour of ifExtNOperState.")
ifExtPoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 6), ArubaPoeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtPoeState.setDescription("\nThe current state of the power over ethernet capability of the\nport. This object is deprecated in favour of ifExtNPoeState.")
ifExtIsTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsTrusted.setDescription("\nThe object indicates if the port is used in the trusted side of the\nnetwork or the untrusted side. This object is deprecated in favour\nof ifExtNIsTrusted.")
ifExtDot1DState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 8), ArubaDot1dState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtDot1DState.setDescription("\nCurrent Dot1d state of the Port. \nThis object provides default switch port value if ifExtIsMonitoring\nis true(1).\nThis object is deprecated in favour of ifExtNDot1DState.")
ifExtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 9), ArubaPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtMode.setDescription("\nThis object indicates if the port is in a Trunk mode or access mode.\nThis object provides default switch port value if ifExtIsMonitoring\nis true(1).\nThis object is deprecated in favour of ifExtNMode.")
ifExtAccessVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 10), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtAccessVlanId.setDescription("\nThe VLAN Id when the port is in Access Mode. This object provides\ndefault switch port value if ifExtIsMonitoring is true(1). This object is\ndeprecated in favour of ifExtNAccessVlanId.")
ifExtTrunkNativeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 11), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkNativeVlanId.setDescription("\nThe native VLAN Id of the Port, when the port is in dot1q mode. This\nobject provides default switch port value if ifExtIsMonitoring is\ntrue(1). \nThis object is deprecated in favour of ifExtNTrunkNativeVlanId.")
ifExtTrunkIsAllowedAll = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkIsAllowedAll.setDescription("\nWhen the mode of the port is Trunk, this Object indicates \nif the port is part of all the configured Vlans. This object\nprovides default switch port value if ifExtIsMonitoring is true(1).\nThis object is deprecated in favour of ifExtNTrunkIsAllowedAll.")
ifExtTrunkAllowedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtTrunkAllowedVlanList.setDescription("\nA string of octets containing one bit per VLAN for a\ntotal of 4096 VLANs in the management domain.  \n	The most significant bit of the octet string is the \n	lowest value VLAN of 4096 VLANs.\n	By setting the bit(1) we indicate that the vlan is part of the\n	interface. \n	The most significant bit of the bitmap is transmitted \n	first. Note that if the length of this string is less than\n	512 octets, any 'missing' octets are assumed to contain\n	the value zero. \nThis object provides default switch port value if\nifExtIsMonitoring is true(1).\nThis object is deprecated in favour of\nifExtNTrunkAllowedVlanList.")
ifExtIngressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIngressACLName.setDescription("\nThis object represents the Ingress ACL name applied to the port.\nAn Empty string indicates that there is not ACL applied on this \nport. This object is deprecated in favour of ifExtNIngressACLName.")
ifExtEgressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtEgressACLName.setDescription("\nThis object represents the Egress ACL name applied to the port.\nAn Empty string indicates that there is not ACL applied on this \nport. This object is deprecated in favour of ifExtNEgressACLName.")
ifExtSessionACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtSessionACLName.setDescription("\nThis object represents the Session ACL name applied to the port.\nAn Empty string indicates that there is not ACL applied on this \nport. This object is deprecated in favour of ifExtNEgressACLName.")
ifExtXsecVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 17), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtXsecVlan.setDescription("\nThis object indicates if the port is an Xsec Port. This object is\ndeprecated in favour of ifExtNXsecVlan.")
ifExtIsMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsMonitoring.setDescription("\nThis object indicates if the port is used for Port monitoring.\nWhen the value of this object is true(1), then below objects provide\ndefault switch port values configured on this port.\nifExtMode,\nifExtAccessVlanId,\nifExtTrunkNativeVlanId,\nifExtTrunkIsAllowedAll,\nifExtTrunkAllowedVlanList\nThis object is deprecated in favour of ifExtNIsMonitoring.")
ifExtIsMux = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtIsMux.setDescription("\nThis object indicates if the port is used as a MUX Port. This object\nis deprecated in favour of ifExtNIsMux.")
ifExtUserSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserSlotNumber.setDescription("\nThe user-visible (zero-based) slot number.")
ifExtUserPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserPortNumber.setDescription("\nThe user-visible (zero-based) port number.")
ifExtPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 22), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortSpeed.setDescription("\nSpeed of the Port. This object is deprecated in favour of\nifExtNPortSpeed.")
ifExtPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 23), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortDuplex.setDescription("\nDuplexity of the Port. This object is deprecated in favour of\nifExtNPortDuplex.")
ifExtPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 24), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtPortType.setDescription("\nType of the Port. This object is deprecated in favour of\nifExtNPortType.")
ifExtDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtDescr.setDescription("\nPort Description. This object is deprecated in favour of\nifExtNDescr.")
ifExtUserModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtUserModuleNumber.setDescription("\nThe user-visible (zero-based) module number.")
wlsxIfExtVlanTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2))
if mibBuilder.loadTexts: wlsxIfExtVlanTable.setDescription("")
wlsxIfExtVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1)).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"))
if mibBuilder.loadTexts: wlsxIfExtVlanEntry.setDescription("\nAn entry for one processor contained by the controller.")
ifExtVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 1), ArubaVlanValidRange()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifExtVlanId.setDescription("\nThis object represents the VLAN Id of the Interface.")
ifExtVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanName.setDescription("\nName of the VLAN. ")
ifExtVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanStatus.setDescription("\nA Row status Object used to create/modify the row.")
wlsxIfExtVlanMemberTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3))
if mibBuilder.loadTexts: wlsxIfExtVlanMemberTable.setDescription("")
wlsxIfExtVlanMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1)).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: wlsxIfExtVlanMemberEntry.setDescription("\nAn entry for one processor contained by the controller.")
ifExtVlanMemberStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanMemberStatus.setDescription("\nA Row status Object used to create/modify and indicate the \nstatus row.")
ifExtVlanMemberSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberSlot.setDescription("\nThe slot index of the slot referred to by this row (1-based).")
ifExtVlanMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberPort.setDescription("\nThe slot index of the slot referred to by this row (1-based).")
ifExtVlanMemberType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 3, 1, 4), ArubaIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtVlanMemberType.setDescription("\nThe VLAN member type.")
wlsxIfExtVlanInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4))
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceTable.setDescription("")
wlsxIfExtVlanInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1)).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtVlanId"))
if mibBuilder.loadTexts: wlsxIfExtVlanInterfaceEntry.setDescription("\nAn entry for one processor contained by the controller.")
ifExtVlanInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIfIndex.setDescription("\nThis is the ifIndex in ifTable, representing VLAN Interface. ")
ifExtVlanInterfaceDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceDescription.setDescription("\nThis Object indicates the description of the Interface.")
ifExtVlanInterfaceBWContract = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceBWContract.setDescription("\nThis Object indicates the Bandwidth contract on the interface.")
ifExtVlanInterfaceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 4), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceAdminState.setDescription("\nThis Object indicates the administrative state of the Interface.")
ifExtVlanInterfaceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 5), ArubaOperStateValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceOperState.setDescription("\nThis Object indicates the operational state of the Interface.")
ifExtVlanInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpAddress.setDescription("\nThis Object indicates the IP Address of the Interface.")
ifExtVlanInterfaceIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 7), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpMask.setDescription("\nThis Object indicates the subnet mask of the Interface.")
ifExtVlanInterfaceIsLocalArp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 8), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIsLocalArp.setDescription("\nThis Object indicates if the Local Arp is set on the Interface. ")
ifExtVlanInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceStatus.setDescription("\nA Row status Object used to create/modify and indicate the \nstatus row.")
ifExtVlanInterfaceIpRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 10), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpRouting.setDescription("\nThis Object indicates if the IP routing is set on the Interface. ")
ifExtVlanInterfaceIpNatInside = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 11), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpNatInside.setDescription("\nThis Object indicates if the IP nat inside is set on the Interface. ")
ifExtVlanInterfaceIpIgmpSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 4, 1, 12), ArubaEnableValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ifExtVlanInterfaceIpIgmpSnooping.setDescription("\nThis Object indicates if the IP IGMP snooping is set on the Interface. ")
wlsxIfExtNPortTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5))
if mibBuilder.loadTexts: wlsxIfExtNPortTable.setDescription("\nThe table of interface details.")
wlsxIfExtNPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1)).setIndexNames((0, "WLSX-IFEXT-MIB", "ifExtNSlotNumber"), (0, "WLSX-IFEXT-MIB", "ifExtNModuleNumber"), (0, "WLSX-IFEXT-MIB", "ifExtNPortNumber"))
if mibBuilder.loadTexts: wlsxIfExtNPortEntry.setDescription("\nAn entry in wlsxIfExtNPortTable.")
ifExtNSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifExtNSlotNumber.setDescription("\nThis object represents the user-visible (zero-based) Physical Slot of the Interface.")
ifExtNModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 2), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifExtNModuleNumber.setDescription("\nThis object represents the user-visible (zero-based) Physical Module of the Interface.")
ifExtNPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 3), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ifExtNPortNumber.setDescription("\nThis object represents the user-visible (zero-based) Physical Port of the Interface.")
ifExtNPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortIfIndex.setDescription("\nThis is the ifIndex in ifTable, representing this slot, module and port.")
ifExtNAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 5), ArubaEnableValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNAdminState.setDescription("\nThe desired state of the interface.")
ifExtNOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNOperState.setDescription("\nThe current operational state of the interface.")
ifExtNPoeState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 7), ArubaPoeState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNPoeState.setDescription("\nThe current state of the power over ethernet capability of the\nport.")
ifExtNIsTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsTrusted.setDescription("\nThe object indicates if the port is used in the trusted side of the\nnetwork or the untrusted side.")
ifExtNDot1DState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 9), ArubaDot1dState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNDot1DState.setDescription("\nCurrent Dot1d state of the Port.")
ifExtNMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 10), ArubaPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNMode.setDescription("\nThis object indicates if the port is in a Trunk mode or access mode.\nThis object provides default switch port value if ifExtIsMonitoring\nis true(1).")
ifExtNAccessVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 11), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNAccessVlanId.setDescription("\nThe VLAN Id when the port is in Access Mode. This object provides \ndefault switch port value if ifExtIsMonitoring is true(1).")
ifExtNTrunkNativeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 12), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkNativeVlanId.setDescription("\nThe native VLAN Id of the Port, when the port is in dot1q mode.\nThis object provides default switch port value if ifExtIsMonitoring\nis true(1).")
ifExtNTrunkIsAllowedAll = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkIsAllowedAll.setDescription("\nWhen the mode of the port is Trunk, this Object indicates\nif the port is part of all the configured Vlans.\nThis object provides default switch port value if ifExtIsMonitoring\nis true(1).")
ifExtNTrunkAllowedVlanList = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNTrunkAllowedVlanList.setDescription("\nA string of octets containing one bit per VLAN for a\ntotal of 4096 VLANs in the management domain.\nThe most significant bit of the octet string is the\nlowest value VLAN of 4096 VLANs.\nBy setting the bit(1) we indicate that the vlan is part of the\ninterface.\nThe most significant bit of the bitmap is transmitted\nfirst. Note that if the length of this string is less than\n512 octets, any 'missing' octets are assumed to contain\nthe value zero.\nThis object provides default switch port value if\nifExtIsMonitoring is true(1).")
ifExtNIngressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIngressACLName.setDescription("\nThis object represents the Ingress ACL name applied to the port.\nAn Empty string indicates that there is not ACL applied on this\nport.")
ifExtNEgressACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNEgressACLName.setDescription("\nThis object represents the Egress ACL name applied to the port.\nAn Empty string indicates that there is not ACL applied on this\nport.")
ifExtNSessionACLName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNSessionACLName.setDescription("\nThis object represents the Session ACL name applied to the port.\nAn Empty string indicates that there is not ACL applied on this\nport.")
ifExtNXsecVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 18), ArubaVlanValidRange()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNXsecVlan.setDescription("\nThis object indicates if the port is an Xsec Port.")
ifExtNIsMonitoring = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsMonitoring.setDescription("\nThis object indicates if the port is used for Port monitoring.\nWhen the value of this object is true(1), then below objects provide\ndefault switch port values configured on this port.\nifExtNMode,\nifExtNAccessVlanId,\nifExtNTrunkNativeVlanId,\nifExtNTrunkIsAllowedAll,\nifExtNTrunkAllowedVlanList")
ifExtNIsMux = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifExtNIsMux.setDescription("\nThis object indicates if the port is used as a MUX Port.")
ifExtNPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 21), ArubaPortSpeed()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortSpeed.setDescription("\nSpeed of the Port.")
ifExtNPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 22), ArubaPortDuplex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortDuplex.setDescription("\nDuplexity of the Port.")
ifExtNPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 23), ArubaPortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNPortType.setDescription("\nType of the Port.")
ifExtNDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 3, 1, 5, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifExtNDescr.setDescription("\nPort Description.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-IFEXT-MIB", PYSNMP_MODULE_ID=wlsxIfExtMIB)

# Objects
mibBuilder.exportSymbols("WLSX-IFEXT-MIB", wlsxIfExtMIB=wlsxIfExtMIB, wlsxIfExtGroup=wlsxIfExtGroup, wlsxIfExtPortTable=wlsxIfExtPortTable, wlsxIfExtPortEntry=wlsxIfExtPortEntry, ifExtSlotNumber=ifExtSlotNumber, ifExtPortNumber=ifExtPortNumber, ifExtPortIfIndex=ifExtPortIfIndex, ifExtAdminState=ifExtAdminState, ifExtOperState=ifExtOperState, ifExtPoeState=ifExtPoeState, ifExtIsTrusted=ifExtIsTrusted, ifExtDot1DState=ifExtDot1DState, ifExtMode=ifExtMode, ifExtAccessVlanId=ifExtAccessVlanId, ifExtTrunkNativeVlanId=ifExtTrunkNativeVlanId, ifExtTrunkIsAllowedAll=ifExtTrunkIsAllowedAll, ifExtTrunkAllowedVlanList=ifExtTrunkAllowedVlanList, ifExtIngressACLName=ifExtIngressACLName, ifExtEgressACLName=ifExtEgressACLName, ifExtSessionACLName=ifExtSessionACLName, ifExtXsecVlan=ifExtXsecVlan, ifExtIsMonitoring=ifExtIsMonitoring, ifExtIsMux=ifExtIsMux, ifExtUserSlotNumber=ifExtUserSlotNumber, ifExtUserPortNumber=ifExtUserPortNumber, ifExtPortSpeed=ifExtPortSpeed, ifExtPortDuplex=ifExtPortDuplex, ifExtPortType=ifExtPortType, ifExtDescr=ifExtDescr, ifExtUserModuleNumber=ifExtUserModuleNumber, wlsxIfExtVlanTable=wlsxIfExtVlanTable, wlsxIfExtVlanEntry=wlsxIfExtVlanEntry, ifExtVlanId=ifExtVlanId, ifExtVlanName=ifExtVlanName, ifExtVlanStatus=ifExtVlanStatus, wlsxIfExtVlanMemberTable=wlsxIfExtVlanMemberTable, wlsxIfExtVlanMemberEntry=wlsxIfExtVlanMemberEntry, ifExtVlanMemberStatus=ifExtVlanMemberStatus, ifExtVlanMemberSlot=ifExtVlanMemberSlot, ifExtVlanMemberPort=ifExtVlanMemberPort, ifExtVlanMemberType=ifExtVlanMemberType, wlsxIfExtVlanInterfaceTable=wlsxIfExtVlanInterfaceTable, wlsxIfExtVlanInterfaceEntry=wlsxIfExtVlanInterfaceEntry, ifExtVlanInterfaceIfIndex=ifExtVlanInterfaceIfIndex, ifExtVlanInterfaceDescription=ifExtVlanInterfaceDescription, ifExtVlanInterfaceBWContract=ifExtVlanInterfaceBWContract, ifExtVlanInterfaceAdminState=ifExtVlanInterfaceAdminState, ifExtVlanInterfaceOperState=ifExtVlanInterfaceOperState, ifExtVlanInterfaceIpAddress=ifExtVlanInterfaceIpAddress, ifExtVlanInterfaceIpMask=ifExtVlanInterfaceIpMask, ifExtVlanInterfaceIsLocalArp=ifExtVlanInterfaceIsLocalArp, ifExtVlanInterfaceStatus=ifExtVlanInterfaceStatus, ifExtVlanInterfaceIpRouting=ifExtVlanInterfaceIpRouting, ifExtVlanInterfaceIpNatInside=ifExtVlanInterfaceIpNatInside, ifExtVlanInterfaceIpIgmpSnooping=ifExtVlanInterfaceIpIgmpSnooping, wlsxIfExtNPortTable=wlsxIfExtNPortTable, wlsxIfExtNPortEntry=wlsxIfExtNPortEntry, ifExtNSlotNumber=ifExtNSlotNumber, ifExtNModuleNumber=ifExtNModuleNumber, ifExtNPortNumber=ifExtNPortNumber, ifExtNPortIfIndex=ifExtNPortIfIndex, ifExtNAdminState=ifExtNAdminState, ifExtNOperState=ifExtNOperState, ifExtNPoeState=ifExtNPoeState, ifExtNIsTrusted=ifExtNIsTrusted, ifExtNDot1DState=ifExtNDot1DState, ifExtNMode=ifExtNMode, ifExtNAccessVlanId=ifExtNAccessVlanId, ifExtNTrunkNativeVlanId=ifExtNTrunkNativeVlanId, ifExtNTrunkIsAllowedAll=ifExtNTrunkIsAllowedAll, ifExtNTrunkAllowedVlanList=ifExtNTrunkAllowedVlanList, ifExtNIngressACLName=ifExtNIngressACLName, ifExtNEgressACLName=ifExtNEgressACLName, ifExtNSessionACLName=ifExtNSessionACLName, ifExtNXsecVlan=ifExtNXsecVlan, ifExtNIsMonitoring=ifExtNIsMonitoring, ifExtNIsMux=ifExtNIsMux, ifExtNPortSpeed=ifExtNPortSpeed, ifExtNPortDuplex=ifExtNPortDuplex, ifExtNPortType=ifExtNPortType, ifExtNDescr=ifExtNDescr)

