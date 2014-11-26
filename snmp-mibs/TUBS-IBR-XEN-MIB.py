# PySNMP SMI module. Autogenerated from smidump -f python TUBS-IBR-XEN-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")
( ibr, ) = mibBuilder.importSymbols("TUBS-SMI", "ibr")

# Types

class XenDomainState(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,2,5,6,1,7,3,)
    namedValues = NamedValues(("unknown", 1), ("running", 2), ("blocked", 3), ("paused", 4), ("crashed", 5), ("dying", 6), ("shutdown", 7), )
    

# Objects

xenMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 14)).setRevisions(("2006-02-20 00:00",))
if mibBuilder.loadTexts: xenMIB.setOrganization("TU Braunschweig")
if mibBuilder.loadTexts: xenMIB.setContactInfo("Frank Strauss, Oliver Wellnitz\nTU Braunschweig\nMuehlenpfordtstrasse 23\n38106 Braunschweig\nGermany\n\nTel: +49 531 391 3283\nFax: +49 531 391 5936\nE-mail: {strauss,wellnitz}@ibr.cs.tu-bs.de")
if mibBuilder.loadTexts: xenMIB.setDescription("Experimental MIB module for Xen Virtual Hosting.")
xenObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1))
xenHost = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1))
xenHostXenVersion = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostXenVersion.setDescription("The version string of the Xen version running\non the physical host.")
xenHostTotalMemKBytes = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostTotalMemKBytes.setDescription("The total amount of available memory in Kbytes\non the physical host.")
xenHostCPUs = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostCPUs.setDescription("The total number of CPUs on the physical host.")
xenHostCPUMHz = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenHostCPUMHz.setDescription("The CPU frequency in MHz of the CPUs on the\nphysical host.")
xenDomainTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2))
if mibBuilder.loadTexts: xenDomainTable.setDescription("A list of all Xen domains on the physical host.")
xenDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1)).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"))
if mibBuilder.loadTexts: xenDomainEntry.setDescription("An entry describing a particular Xen domain.")
xenDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: xenDomainName.setDescription("The name of the Xen domain.")
xenDomainState = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 2), XenDomainState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainState.setDescription("The state of the Xen domain.")
xenDomainMemKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainMemKBytes.setDescription("The amount of memory in Kbytes currently occupied\nby the Xen domain.")
xenDomainMaxMemKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenDomainMaxMemKBytes.setDescription("The total amount of memory in Kbytes assigned\nto the Xen domain. A value of zero denotes that\nthere is no limit.")
xenVCPUTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3))
if mibBuilder.loadTexts: xenVCPUTable.setDescription("A list of all VCPUs per Xen domain.")
xenVCPUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1)).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"), (0, "TUBS-IBR-XEN-MIB", "xenVCPUIndex"))
if mibBuilder.loadTexts: xenVCPUEntry.setDescription("An entry describing a VCPU of a Xen domain.")
xenVCPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: xenVCPUIndex.setDescription("The index of the VCPU.")
xenVCPUMilliseconds = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenVCPUMilliseconds.setDescription("The number milliseconds consumed by the VCPU since\nthe Xen domain has been set up.")
xenNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4))
if mibBuilder.loadTexts: xenNetworkTable.setDescription("A list of all networks per Xen domain.")
xenNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1)).setIndexNames((0, "TUBS-IBR-XEN-MIB", "xenDomainName"), (0, "TUBS-IBR-XEN-MIB", "xenNetworkIndex"))
if mibBuilder.loadTexts: xenNetworkEntry.setDescription("An entry describing a network of a Xen domain.")
xenNetworkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: xenNetworkIndex.setDescription("The index of the network.")
xenNetworkInKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInKBytes.setDescription("The number of Kbytes received on the network\ninterface since the Xen domain has been set up.")
xenNetworkInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInPkts.setDescription("The number of packets received on the network\ninterface since the Xen domain has been set up.")
xenNetworkInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInErrors.setDescription("The number of erroneous packets received on the network\ninterface since the Xen domain has been set up.")
xenNetworkInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkInDiscards.setDescription("The number of dropped packets received on the network\ninterface since the Xen domain has been set up.")
xenNetworkOutKBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutKBytes.setDescription("The number of Kbytes sent on the network\ninterface since the Xen domain has been set up.")
xenNetworkOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutPkts.setDescription("The number of packets sent on the network\ninterface since the Xen domain has been set up.")
xenNetworkOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutErrors.setDescription("The number of packets that could not be sent\non the network interface because of any errors\nsince the Xen domain has been set up.")
xenNetworkOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 14, 1, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xenNetworkOutDiscards.setDescription("The number of packets that have not been sent	\non the network interface even though no errors\nhad been detected since the Xen domain has been\nset up.")
xenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 2))
xenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3))
xenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1))
xenGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2))

# Augmentions

# Groups

xenGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 2, 1)).setObjects(*(("TUBS-IBR-XEN-MIB", "xenNetworkOutKBytes"), ("TUBS-IBR-XEN-MIB", "xenDomainMaxMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenHostTotalMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutErrors"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutDiscards"), ("TUBS-IBR-XEN-MIB", "xenNetworkInPkts"), ("TUBS-IBR-XEN-MIB", "xenHostXenVersion"), ("TUBS-IBR-XEN-MIB", "xenDomainState"), ("TUBS-IBR-XEN-MIB", "xenHostCPUs"), ("TUBS-IBR-XEN-MIB", "xenDomainMemKBytes"), ("TUBS-IBR-XEN-MIB", "xenNetworkInErrors"), ("TUBS-IBR-XEN-MIB", "xenNetworkOutPkts"), ("TUBS-IBR-XEN-MIB", "xenNetworkInKBytes"), ("TUBS-IBR-XEN-MIB", "xenHostCPUMHz"), ("TUBS-IBR-XEN-MIB", "xenVCPUMilliseconds"), ("TUBS-IBR-XEN-MIB", "xenNetworkInDiscards"), ) )
if mibBuilder.loadTexts: xenGeneralGroup.setDescription("A collection of all Xen MIB objects.")

# Compliances

xenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1575, 1, 14, 3, 1, 1)).setObjects(*(("TUBS-IBR-XEN-MIB", "xenGeneralGroup"), ) )
if mibBuilder.loadTexts: xenCompliance.setDescription("The compliance statement for an SNMP entity which\nimplements the Xen MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", PYSNMP_MODULE_ID=xenMIB)

# Types
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", XenDomainState=XenDomainState)

# Objects
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", xenMIB=xenMIB, xenObjects=xenObjects, xenHost=xenHost, xenHostXenVersion=xenHostXenVersion, xenHostTotalMemKBytes=xenHostTotalMemKBytes, xenHostCPUs=xenHostCPUs, xenHostCPUMHz=xenHostCPUMHz, xenDomainTable=xenDomainTable, xenDomainEntry=xenDomainEntry, xenDomainName=xenDomainName, xenDomainState=xenDomainState, xenDomainMemKBytes=xenDomainMemKBytes, xenDomainMaxMemKBytes=xenDomainMaxMemKBytes, xenVCPUTable=xenVCPUTable, xenVCPUEntry=xenVCPUEntry, xenVCPUIndex=xenVCPUIndex, xenVCPUMilliseconds=xenVCPUMilliseconds, xenNetworkTable=xenNetworkTable, xenNetworkEntry=xenNetworkEntry, xenNetworkIndex=xenNetworkIndex, xenNetworkInKBytes=xenNetworkInKBytes, xenNetworkInPkts=xenNetworkInPkts, xenNetworkInErrors=xenNetworkInErrors, xenNetworkInDiscards=xenNetworkInDiscards, xenNetworkOutKBytes=xenNetworkOutKBytes, xenNetworkOutPkts=xenNetworkOutPkts, xenNetworkOutErrors=xenNetworkOutErrors, xenNetworkOutDiscards=xenNetworkOutDiscards, xenTraps=xenTraps, xenConformance=xenConformance, xenCompliances=xenCompliances, xenGroups=xenGroups)

# Groups
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", xenGeneralGroup=xenGeneralGroup)

# Compliances
mibBuilder.exportSymbols("TUBS-IBR-XEN-MIB", xenCompliance=xenCompliance)