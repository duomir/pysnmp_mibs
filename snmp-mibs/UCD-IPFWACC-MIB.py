# PySNMP SMI module. Autogenerated from smidump -f python UCD-IPFWACC-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")
( ucdExperimental, ) = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")

# Objects

ucdIpFwAccMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 1)).setRevisions(("1999-12-16 00:00",))
if mibBuilder.loadTexts: ucdIpFwAccMIB.setOrganization("University of California, Davis")
if mibBuilder.loadTexts: ucdIpFwAccMIB.setContactInfo("This mib is no longer being maintained by the University of\nCalifornia and is now in life-support-mode and being\nmaintained by the net-snmp project.  The best place to write\nfor public questions about the net-snmp-coders mailing list\nat net-snmp-coders@lists.sourceforge.net.\n\npostal:   Wes Hardaker\n         P.O. Box 382\n         Davis CA  95617\n\nemail:    net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts: ucdIpFwAccMIB.setDescription("This module defines MIB components for reading information\nfrom the accounting rules IP Firewall. This would typically\nlet you read the rules and the counters. I did not include\nsome flags and fields that I considered irrelevant for the\naccounting rules. Resetting the counters of the rules by SNMP\nwould be simple, but I don't consider it so useful. I gave no\nconsideration to implementing write access for allowing\nmodification of the accounting rules.\n\nCristian.Estan@net.utcluj.ro ")
ipFwAccTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1))
if mibBuilder.loadTexts: ipFwAccTable.setDescription("A table with the accounting rules of the IP firewall")
ipFwAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1)).setIndexNames((0, "UCD-IPFWACC-MIB", "ipFwAccIndex"))
if mibBuilder.loadTexts: ipFwAccEntry.setDescription("An accounting rule of the IP firewall")
ipFwAccIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccIndex.setDescription("Reference index for each firewall rule.")
ipFwAccSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcAddr.setDescription("The source address in the firewall rule.")
ipFwAccSrcNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcNetMask.setDescription("The netmask of the source address in the firewall rule.")
ipFwAccDstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstAddr.setDescription("The destination address in the firewall rule.")
ipFwAccDstNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstNetMask.setDescription("The netmask of the destination address in the firewall rule.")
ipFwAccViaName = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccViaName.setDescription("The name of the interface to which the rule applies. If no\ninterface is associated with the present rule, this should\ncontain a dash (-).")
ipFwAccViaAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccViaAddr.setDescription("The address of the interface to which the rule applies.\nUsing this parameter makes sense when multiple addresses are\nassociated to the same physical interface. If not defined\nfor the current rule this should be set to 0.")
ipFwAccProto = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(2,4,3,1,5,)).subtype(namedValues=NamedValues(("other", 1), ("all", 2), ("tcp", 3), ("udp", 4), ("icmp", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccProto.setDescription("The protocol(s) to which the rule applies.")
ipFwAccBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccBidir.setDescription("Whether the rule works in both directions (i.e. with the\nsource and destination parts swapped) or not.")
ipFwAccDir = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 10), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,3,)).subtype(namedValues=NamedValues(("both", 1), ("in", 2), ("out", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDir.setDescription("Whether the rule applies to packets entering or exiting the\nkernel.")
ipFwAccBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccBytes.setDescription("The number of bytes that matched this rule since the last\nreset of the counters.")
ipFwAccPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPackets.setDescription("The number of packets that matched this rule since the last\nreset of the counters.")
ipFwAccNrSrcPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccNrSrcPorts.setDescription("The number of ports that refer to the source address.")
ipFwAccNrDstPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccNrDstPorts.setDescription("The number of ports that refer to the destination address.")
ipFwAccSrcIsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 15), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("srchasrange", 1), ("srchasnorange", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccSrcIsRange.setDescription("Interpret the first two ports of the source part as\nthe upper and lower limit of an interval or not.")
ipFwAccDstIsRange = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 16), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("dsthasrange", 1), ("dsthasnorange", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccDstIsRange.setDescription("Interpret the first two ports of the destination part as\nthe upper and lower limit of an interval or not.")
ipFwAccPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort1.setDescription("Port number 1.")
ipFwAccPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort2.setDescription("Port number 2.")
ipFwAccPort3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort3.setDescription("Port number 3.")
ipFwAccPort4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort4.setDescription("Port number 4.")
ipFwAccPort5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort5.setDescription("Port number 5.")
ipFwAccPort6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort6.setDescription("Port number 6.")
ipFwAccPort7 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort7.setDescription("Port number 7.")
ipFwAccPort8 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort8.setDescription("Port number 8.")
ipFwAccPort9 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort9.setDescription("Port number 9.")
ipFwAccPort10 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFwAccPort10.setDescription("Port number 10.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("UCD-IPFWACC-MIB", PYSNMP_MODULE_ID=ucdIpFwAccMIB)

# Objects
mibBuilder.exportSymbols("UCD-IPFWACC-MIB", ucdIpFwAccMIB=ucdIpFwAccMIB, ipFwAccTable=ipFwAccTable, ipFwAccEntry=ipFwAccEntry, ipFwAccIndex=ipFwAccIndex, ipFwAccSrcAddr=ipFwAccSrcAddr, ipFwAccSrcNetMask=ipFwAccSrcNetMask, ipFwAccDstAddr=ipFwAccDstAddr, ipFwAccDstNetMask=ipFwAccDstNetMask, ipFwAccViaName=ipFwAccViaName, ipFwAccViaAddr=ipFwAccViaAddr, ipFwAccProto=ipFwAccProto, ipFwAccBidir=ipFwAccBidir, ipFwAccDir=ipFwAccDir, ipFwAccBytes=ipFwAccBytes, ipFwAccPackets=ipFwAccPackets, ipFwAccNrSrcPorts=ipFwAccNrSrcPorts, ipFwAccNrDstPorts=ipFwAccNrDstPorts, ipFwAccSrcIsRange=ipFwAccSrcIsRange, ipFwAccDstIsRange=ipFwAccDstIsRange, ipFwAccPort1=ipFwAccPort1, ipFwAccPort2=ipFwAccPort2, ipFwAccPort3=ipFwAccPort3, ipFwAccPort4=ipFwAccPort4, ipFwAccPort5=ipFwAccPort5, ipFwAccPort6=ipFwAccPort6, ipFwAccPort7=ipFwAccPort7, ipFwAccPort8=ipFwAccPort8, ipFwAccPort9=ipFwAccPort9, ipFwAccPort10=ipFwAccPort10)

