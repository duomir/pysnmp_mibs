# PySNMP SMI module. Autogenerated from smidump -f python BFD-STD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:48 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( jnxBfdExperiment, ) = mibBuilder.importSymbols("JUNIPER-EXPERIMENT-MIB", "jnxBfdExperiment")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Counter64, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class BfdDiag(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(7,9,2,5,8,4,3,1,6,)
    namedValues = NamedValues(("noDiagnostic", 1), ("controlDetectionTimeExpired", 2), ("echoFunctionFailed", 3), ("neighborSignaledSessionDown", 4), ("forwardingPlaneReset", 5), ("pathDown", 6), ("concatenatedPathDown", 7), ("administrativelyDown", 8), ("reverseConcatenatedPathDown", 9), )
    
class BfdInterval(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)
    
class BfdSessIndexTC(TextualConvention, Unsigned32):
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(1,4294967295)
    

# Objects

bfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1)).setRevisions(("2005-08-22 12:00","2005-07-22 12:00",))
if mibBuilder.loadTexts: bfdMIB.setOrganization("IETF")
if mibBuilder.loadTexts: bfdMIB.setContactInfo("        Thomas D. Nadeau \nCisco Systems, Inc. \nEmail:  tnadeau@cisco.com \n\nZafar Ali  \nCisco Systems, Inc. \nEmail:  zali@cisco.com ")
if mibBuilder.loadTexts: bfdMIB.setDescription("Bidirectional Forwarding Management Information Base.")
bfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 0))
bfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1))
bfdScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 1))
bfdAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), )).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdAdminStatus.setDescription("The global administrative status of BFD in this router.  \nThe value 'enabled' denotes that the BFD Process is \nactive on at least one interface; 'disabled' disables  \nit on all interfaces.")
bfdVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 1, 3), Unsigned32().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdVersionNumber.setDescription("The current version number of the BFD protocol.")
bfdSessNotificationsEnable = MibScalar((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessNotificationsEnable.setDescription("If this object is set to true(1), then it enables \nthe emission of bfdSessUp and bfdSessDown \nnotifications; otherwise these notifications are not \nemitted.")
bfdSessTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2))
if mibBuilder.loadTexts: bfdSessTable.setDescription("The BFD Session Table describes the BFD sessions.")
bfdSessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1)).setIndexNames((0, "BFD-STD-MIB", "bfdSessIndex"))
if mibBuilder.loadTexts: bfdSessEntry.setDescription("The BFD Session Entry describes BFD session.")
bfdSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 1), BfdSessIndexTC()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: bfdSessIndex.setDescription("This object contains an index used to represent a \nunique BFD session on this device.")
bfdSessApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessApplicationId.setDescription("This object contains an index used to indicate \na local application which owns or maintains this \nBFD session. For instance, the MPLS VPN process may \nmaintain a subset of the total number of BFD \nsessions.  This application ID provides a convenient \nway to segregate sessions by the applications which \nmaintain them.")
bfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDiscriminator.setDescription("This object specifies the local discriminator for this BFD  \nsession, used to uniquely identify it.")
bfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteDiscr.setDescription("This object specifies the session discriminator chosen  \nby the remote system for this BFD session.")
bfdSessUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 5), InetPortNumber().clone('0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessUdpPort.setDescription("The UDP Port for BFD. The default value is the \nwell-known value for this port.")
bfdSessState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,3,4,)).subtype(namedValues=NamedValues(("adminDown", 1), ("down", 2), ("init", 3), ("up", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessState.setDescription("The perceived state of the BFD session.")
bfdSessRemoteHeardFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteHeardFlag.setDescription("This object specifies status of BFD packet reception from  \nthe remote system. Specifically, it is set to true(1) if \nthe local system is actively receiving BFD packets from the  \nremote system, and is set to false(0) if the local system  \nhas not received BFD packets recently (within the detection  \ntime) or if the local system is attempting to tear down \nthe BFD session.")
bfdSessDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: bfdSessDiag.setDescription("A diagnostic code specifying the local system's reason  \nfor the last transition of the session from up(1)  \nto some other state.")
bfdSessOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(4,1,2,3,)).subtype(namedValues=NamedValues(("asyncModeWEchoFun", 1), ("asynchModeWOEchoFun", 2), ("demandModeWEchoFunction", 3), ("demandModeWOEchoFunction", 4), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessOperMode.setDescription("This object specifies current operating mode that BFD  \nsession is operating in. \n\nA value of AsyncModeWEchoFun(1) ... \nA value of AsynchModeWOEchoFun(2) ... \nA value of DemandModeWEchoFunction(3) ... \nA value of DemandModeWOEchoFunction(4) ... ")
bfdSessDemandModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 10), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDemandModeDesiredFlag.setDescription("This object indicates that the local system's  \ndesire to use Demand mode. Specifically, it is set  \nto true(1) if the local system wishes to use  \nDemand mode or false(0) if not")
bfdSessEchoFuncModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 11), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessEchoFuncModeDesiredFlag.setDescription("This object indicates that the local system's  \ndesire to use Echo mode. Specifically, it is set  \nto true(1) if the local system wishes to use  \nEcho mode or false(0) if not")
bfdSessControlPlanIndepFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessControlPlanIndepFlag.setDescription("This object indicates that the local system's  \nability to continue to function through a disruption of  \nthe control plane. Specifically, it is set  \nto true(1) if the local system BFD implementation is \nindependent of the control plane. Otherwise, the  \nvalue is set to false(0)")
bfdSessAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 13), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessAddrType.setDescription("This object specifies IP address of the interface  \nassociated with this BFD session.  \n\nOnly values unknown(0), ipv4(1) or ipv6(2) \nhave to be supported.  \n\nA value of unknown(0) is allowed only when  \nthe outgoing interface is of type point-to-point, or \nwhen the BFD session is not associated with a specific  \ninterface. \n\nIf any other unsupported values are attempted in a set \noperation, the agent MUST return an inconsistentValue  \nerror. ")
bfdSessAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 14), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessAddr.setDescription("This object specifies IP address of the interface  \nassociated with this BFD session.  \nIt can also be used to enabled BFD on a specific  \ninterface. The value is set to zero when BFD session is not  \nassociated with a specific interface. ")
bfdSessDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 15), BfdInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDesiredMinTxInterval.setDescription("This object specifies the minimum interval, in  \nmicroseconds, that the local system would like to use when \n     transmitting BFD Control packets.")
bfdSessDesiredMinRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 16), BfdInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDesiredMinRxInterval.setDescription("This object specifies the minimum interval, in  \nmicroseconds, between received  BFD Control packets the  \nlocal system is capable of supporting.")
bfdSessDesiredMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 17), BfdInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDesiredMinEchoRxInterval.setDescription("This object specifies the minimum interval, in  \nmicroseconds, between received BFD Echo packets that this \nsystem is capable of supporting.")
bfdSessDetectMult = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDetectMult.setDescription("This object specifies the Detect time multiplier.")
bfdSessStorType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 19), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessStorType.setDescription("This variable indicates the storage type for this \nobject. Conceptual rows having the value  \n'permanent' need not allow write-access to any  \ncolumnar objects in the row.")
bfdSessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 20), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRowStatus.setDescription("This variable is used to create, modify, and/or \ndelete a row in this table. When a row in this \ntable has a row in the active(1) state, no  \nobjects in this row can be modified except the \nbfdSessRowStatus and bfdSessStorageType.")
bfdSessAuthPresFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 21), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessAuthPresFlag.setDescription("This object indicates that the local system's  \ndesire to use Authentication. Specifically, it is set  \nto true(1) if the local system wishes the session  \nto be authenticated or false(0) if not")
bfdSessAuthenticationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 2, 1, 22), Integer().subtype(subtypeSpec=SingleValueConstraint(5,2,3,1,4,)).subtype(namedValues=NamedValues(("simplePassword", 1), ("keyedMD5", 2), ("meticulousKeyedMD5", 3), ("keyedSHA1", 4), ("meticulousKeyedSHA1", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessAuthenticationType.setDescription("The Authentication Type used for this BFD session. This \nfield is valid only when the Authentication Present bit is set")
bfdSessPerfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3))
if mibBuilder.loadTexts: bfdSessPerfTable.setDescription("This table specifies BFD Session performance counters.")
bfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1))
if mibBuilder.loadTexts: bfdSessPerfEntry.setDescription("An entry in this table is created by a BFD-enabled node for  \nevery BFD Session. bfdCounterDiscontinuityTime is used to  \nindicate potential discontinuity for all counter objects  \nin this table.")
bfdSessPerfPktIn = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktIn.setDescription("The total number of BFD messages received for this BFD \nsession.")
bfdSessPerfPktOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktOut.setDescription("The total number of BFD messages sent for this BFD session.")
bfdSessUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessUpTime.setDescription("The value of sysUpTime on the most recent occasion at which \nthe session came up. If no such up event exists this object \ncontains a zero value.")
bfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastSessDownTime.setDescription("The value of sysUpTime on the most recent occasion at which \nthe last time communication was lost with the neighbor. If  \nno such down event exist this object contains a zero value.")
bfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 5), BfdDiag()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastCommLostDiag.setDescription("The BFD diag code for the last time communication was lost  \nwith the neighbor. If no such down event exists this object  \ncontains a zero value.")
bfdSessPerfSessUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfSessUpCount.setDescription("The number of times this session has gone into the Up \nstate since the router last rebooted.")
bfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfDiscTime.setDescription("The value of sysUpTime on the most recent occasion at \nwhich any one or more of the session counters suffered \na discontinuity.  \n\nThe relevant counters are the specific instances associated  \nwith this BFD session of any Counter32 object contained in \nthe BfdSessPerfTable. If no such discontinuities have occurred  \nsince the last re-initialization of the local management \nsubsystem, then this object contains a zero value.")
bfdSessPerfPktInHC = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktInHC.setDescription("This value represents the total number of BFD messages \nreceived for this BFD session. It MUST be equal to the \nleast significant 32 bits of bfdSessPerfPktIn \nif bfdSessPerfPktInHC is supported according to \nthe rules spelled out in RFC2863.")
bfdSessPerfPktOutHC = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfPktOutHC.setDescription("This value represents the total number of  \ntotal number of BFD messages transmitted for this  \nBFD session. It MUST be equal to the \nleast significant 32 bits of bfdSessPerfPktIn \nif bfdSessPerfPktOutHC is supported according to \nthe rules spelled out in RFC2863.")
bfdSessMapTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 4))
if mibBuilder.loadTexts: bfdSessMapTable.setDescription("The BFD Session Mapping Table maps the complex \nindexing of the BFD sessions to the flat \nBFDIndex used in the BfdSessionTable. \n\nImplementors need to be aware that if the value of \nthe bfdSessAddr (an OID) has more  \nthat 111 sub-identifiers, then OIDs of column \ninstances in this table will have more than 128 \nsub-identifiers and cannot be accessed using SNMPv1, \nSNMPv2c, or SNMPv3. ")
bfdSessMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 4, 1)).setIndexNames((0, "BFD-STD-MIB", "bfdSessApplicationId"), (0, "BFD-STD-MIB", "bfdSessDiscriminator"), (0, "BFD-STD-MIB", "bfdSessAddrType"), (0, "BFD-STD-MIB", "bfdSessAddr"))
if mibBuilder.loadTexts: bfdSessMapEntry.setDescription("The BFD Session Entry describes BFD session \nthat is mapped to this index.\n\nImplementors need to be aware that if the value of\nthe mplsInSegmentMapLabelPtrIndex (an OID) has more\nthat 111 sub-identifiers, then OIDs of column\ninstances in this table will have more than 128\nsub-identifiers and cannot be accessed using SNMPv1,\nSNMPv2c, or SNMPv3.")
bfdSessMapBfdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 1, 4, 1, 1), BfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessMapBfdIndex.setDescription("This object specifies the BfdIndex referred to by \nthe indexes of this row. In essence, a mapping is \nprovided between these indexes and the BfdSessTable.")
bfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3))
bfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 1))
bfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 2))

# Augmentions
bfdSessEntry.registerAugmentions(("BFD-STD-MIB", "bfdSessPerfEntry"))
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())

# Notifications

bfdSessUp = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 0, 1)).setObjects(*(("BFD-STD-MIB", "bfdSessDiag"), ) )
if mibBuilder.loadTexts: bfdSessUp.setDescription("This notification is generated when the \nbfdSessState object for one or more contiguous \nentries in bfdSessTable are about to enter the up(2) \nstate from some other state. The included values of \nbfdSessDiag MUST both be set equal to this \nnew state (i.e: up(1)).  The two instances of  \nbfdSessDiag in this notification indicate the range  \nof indexes that are affected.  Note that all the indexes  \nof the two ends of the range can be derived from the \ninstance identifiers of these two objects.  For the \ncases where a contiguous range of sessions \nhave transitioned into the up(1) state at roughly \nthe same time, the device SHOULD issue a single \nnotification for each range of contiguous indexes in \nan effort to minimize the emission of a large number \nof notifications.  If a notification has to be \nissued for just a single bfdSessEntry, then \nthe instance identifier (and values) of the two \nbfdSessDiag objects MUST be the identical.")
bfdSessDown = NotificationType((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 0, 2)).setObjects(*(("BFD-STD-MIB", "bfdSessDiag"), ) )
if mibBuilder.loadTexts: bfdSessDown.setDescription("This notification is generated when the \nbfdSessState object for one or more contiguous \nentries in bfdSessTable are about to enter the down(4) \nor adminDown(5) states from some other state. The included  \nvalues of bfdSessDiag MUST both be set equal to this \nnew state (i.e: down(4) or adminDown(5)).  The two instances  \nof bfdSessDiag in this notification indicate the range  \nof indexes that are affected.  Note that all the indexes  \nof the two ends of the range can be derived from the \ninstance identifiers of these two objects.  For \ncases where a contiguous range of sessions \nhave transitioned into the down(4) or adminDown(5) states  \nat roughly the same time, the device SHOULD issue a single \nnotification for each range of contiguous indexes in \nan effort to minimize the emission of a large number \nof notifications.  If a notification has to be \nissued for just a single bfdSessEntry, then \nthe instance identifier (and values) of the two \nbfdSessDiag objects MUST be the identical.")

# Groups

bfdSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 1, 1)).setObjects(*(("BFD-STD-MIB", "bfdSessRemoteHeardFlag"), ("BFD-STD-MIB", "bfdVersionNumber"), ("BFD-STD-MIB", "bfdSessDiscriminator"), ("BFD-STD-MIB", "bfdSessStorType"), ("BFD-STD-MIB", "bfdSessDemandModeDesiredFlag"), ("BFD-STD-MIB", "bfdSessControlPlanIndepFlag"), ("BFD-STD-MIB", "bfdSessAddrType"), ("BFD-STD-MIB", "bfdSessOperMode"), ("BFD-STD-MIB", "bfdSessUdpPort"), ("BFD-STD-MIB", "bfdSessApplicationId"), ("BFD-STD-MIB", "bfdSessDesiredMinTxInterval"), ("BFD-STD-MIB", "bfdAdminStatus"), ("BFD-STD-MIB", "bfdSessRowStatus"), ("BFD-STD-MIB", "bfdSessDesiredMinEchoRxInterval"), ("BFD-STD-MIB", "bfdSessAuthenticationType"), ("BFD-STD-MIB", "bfdSessNotificationsEnable"), ("BFD-STD-MIB", "bfdSessEchoFuncModeDesiredFlag"), ("BFD-STD-MIB", "bfdSessAddr"), ("BFD-STD-MIB", "bfdSessAuthPresFlag"), ("BFD-STD-MIB", "bfdSessDiag"), ("BFD-STD-MIB", "bfdSessMapBfdIndex"), ("BFD-STD-MIB", "bfdSessRemoteDiscr"), ("BFD-STD-MIB", "bfdSessState"), ("BFD-STD-MIB", "bfdSessDetectMult"), ("BFD-STD-MIB", "bfdSessDesiredMinRxInterval"), ) )
if mibBuilder.loadTexts: bfdSessionGroup.setDescription("Collection of objects needed for BFD sessions.")
bfdSessionPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 1, 2)).setObjects(*(("BFD-STD-MIB", "bfdSessPerfLastCommLostDiag"), ("BFD-STD-MIB", "bfdSessUpTime"), ("BFD-STD-MIB", "bfdSessPerfPktIn"), ("BFD-STD-MIB", "bfdSessPerfDiscTime"), ("BFD-STD-MIB", "bfdSessPerfLastSessDownTime"), ("BFD-STD-MIB", "bfdSessPerfSessUpCount"), ("BFD-STD-MIB", "bfdSessPerfPktOut"), ) )
if mibBuilder.loadTexts: bfdSessionPerfGroup.setDescription("Collection of objects needed to monitor the \nperformance of BFD sessions.")
bfdSessionPerfHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 1, 3)).setObjects(*(("BFD-STD-MIB", "bfdSessPerfPktInHC"), ("BFD-STD-MIB", "bfdSessPerfPktOutHC"), ) )
if mibBuilder.loadTexts: bfdSessionPerfHCGroup.setDescription("Collection of objects needed to monitor the \nperformance of BFD sessions for which the \nvalues of bfdSessPerfPktIn, bfdSessPerfPktOut  \nwrap around too quickly.")
bfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 1, 4)).setObjects(*(("BFD-STD-MIB", "bfdSessUp"), ("BFD-STD-MIB", "bfdSessDown"), ) )
if mibBuilder.loadTexts: bfdNotificationGroup.setDescription("Set of notifications implemented in this  \nmodule.")

# Compliances

bfdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2636, 5, 3, 1, 3, 2, 1)).setObjects(*(("BFD-STD-MIB", "bfdNotificationGroup"), ("BFD-STD-MIB", "bfdSessionPerfGroup"), ("BFD-STD-MIB", "bfdSessionGroup"), ("BFD-STD-MIB", "bfdSessionPerfHCGroup"), ) )
if mibBuilder.loadTexts: bfdModuleFullCompliance.setDescription("Compliance statement for agents that provide full \nsupport for BFD-MIB. Such devices can \nthen be monitored and also be configured using \nthis MIB module.")

# Exports

# Module identity
mibBuilder.exportSymbols("BFD-STD-MIB", PYSNMP_MODULE_ID=bfdMIB)

# Types
mibBuilder.exportSymbols("BFD-STD-MIB", BfdDiag=BfdDiag, BfdInterval=BfdInterval, BfdSessIndexTC=BfdSessIndexTC)

# Objects
mibBuilder.exportSymbols("BFD-STD-MIB", bfdMIB=bfdMIB, bfdNotifications=bfdNotifications, bfdObjects=bfdObjects, bfdScalarObjects=bfdScalarObjects, bfdAdminStatus=bfdAdminStatus, bfdVersionNumber=bfdVersionNumber, bfdSessNotificationsEnable=bfdSessNotificationsEnable, bfdSessTable=bfdSessTable, bfdSessEntry=bfdSessEntry, bfdSessIndex=bfdSessIndex, bfdSessApplicationId=bfdSessApplicationId, bfdSessDiscriminator=bfdSessDiscriminator, bfdSessRemoteDiscr=bfdSessRemoteDiscr, bfdSessUdpPort=bfdSessUdpPort, bfdSessState=bfdSessState, bfdSessRemoteHeardFlag=bfdSessRemoteHeardFlag, bfdSessDiag=bfdSessDiag, bfdSessOperMode=bfdSessOperMode, bfdSessDemandModeDesiredFlag=bfdSessDemandModeDesiredFlag, bfdSessEchoFuncModeDesiredFlag=bfdSessEchoFuncModeDesiredFlag, bfdSessControlPlanIndepFlag=bfdSessControlPlanIndepFlag, bfdSessAddrType=bfdSessAddrType, bfdSessAddr=bfdSessAddr, bfdSessDesiredMinTxInterval=bfdSessDesiredMinTxInterval, bfdSessDesiredMinRxInterval=bfdSessDesiredMinRxInterval, bfdSessDesiredMinEchoRxInterval=bfdSessDesiredMinEchoRxInterval, bfdSessDetectMult=bfdSessDetectMult, bfdSessStorType=bfdSessStorType, bfdSessRowStatus=bfdSessRowStatus, bfdSessAuthPresFlag=bfdSessAuthPresFlag, bfdSessAuthenticationType=bfdSessAuthenticationType, bfdSessPerfTable=bfdSessPerfTable, bfdSessPerfEntry=bfdSessPerfEntry, bfdSessPerfPktIn=bfdSessPerfPktIn, bfdSessPerfPktOut=bfdSessPerfPktOut, bfdSessUpTime=bfdSessUpTime, bfdSessPerfLastSessDownTime=bfdSessPerfLastSessDownTime, bfdSessPerfLastCommLostDiag=bfdSessPerfLastCommLostDiag, bfdSessPerfSessUpCount=bfdSessPerfSessUpCount, bfdSessPerfDiscTime=bfdSessPerfDiscTime, bfdSessPerfPktInHC=bfdSessPerfPktInHC, bfdSessPerfPktOutHC=bfdSessPerfPktOutHC, bfdSessMapTable=bfdSessMapTable, bfdSessMapEntry=bfdSessMapEntry, bfdSessMapBfdIndex=bfdSessMapBfdIndex, bfdConformance=bfdConformance, bfdGroups=bfdGroups, bfdCompliances=bfdCompliances)

# Notifications
mibBuilder.exportSymbols("BFD-STD-MIB", bfdSessUp=bfdSessUp, bfdSessDown=bfdSessDown)

# Groups
mibBuilder.exportSymbols("BFD-STD-MIB", bfdSessionGroup=bfdSessionGroup, bfdSessionPerfGroup=bfdSessionPerfGroup, bfdSessionPerfHCGroup=bfdSessionPerfHCGroup, bfdNotificationGroup=bfdNotificationGroup)

# Compliances
mibBuilder.exportSymbols("BFD-STD-MIB", bfdModuleFullCompliance=bfdModuleFullCompliance)