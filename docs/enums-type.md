```graphql
"""A type of account."""
enum AccountTypeEnum {
  """A commercial account"""
  COMMERCIAL
  """A residential account"""
  RESIDENTIAL
  """A government account"""
  GOVERNMENT
  """An industrial account"""
  INDUSTRIAL
  """A senior citizen account"""
  SENIOR_CITIZEN
}

"""The entity that this `Address` is associated with."""
enum AddressableType {
  """An `Account`."""
  Account
  """An `InventoryLocation`."""
  InventoryLocation
  """A `BankAccount`."""
  BankAccount
  """A `CreditCard`."""
  CreditCard
  """A `NetworkSite`."""
  NetworkSite
  """A `Company`."""
  Company
  """A Towercoverage Submission"""
  TowercoverageSubmission
  """Vendor"""
  Vendor
}

"""The type of address that this is."""
enum AddressType {
  """A physical address where the entity is located"""
  PHYSICAL
  """An address where this entity receives mail"""
  MAILING
}

"""The type of entity that completes a task."""
enum CompletableType {
  """Custom Field"""
  CustomField
  """File"""
  File
}

"""An entity that can have a `Contact` associated with it."""
enum ContactableType {
  """Account"""
  Account
  """Network Site"""
  NetworkSite
  """Vendor"""
  Vendor
}

"""The entity that this `Credit` is associated with."""
enum CreditableType {
  """A `Discount`."""
  Discount
  """A `Payment`."""
  Payment
}

"""An entity that is allowed to have custom fields defined for it."""
enum CustomfielddataableType {
  """A customer account."""
  Account
  """A geographical address."""
  Address
  """A contact person."""
  Contact
  """A generic assignee for inventory items."""
  GenericInventoryAssignee
  """A job, typically in the field."""
  Job
  """A network site."""
  NetworkSite
  """A line item on a purchase order."""
  PurchaseOrderItem
  """types.test_read_only_file_model"""
  TestReadOnlyFileModel
  """A ticket."""
  Ticket
}

"""The entity that this `DisbursementDetail` is associated with."""
enum DisbursableType {
  """A `Payment`."""
  Payment
  """A `Refunded Payment`."""
  RefundedPayment
  """A `Voided Payment`."""
  VoidedPayment
}

"""The entity that this `Email` is associated with."""
enum EmailableType {
  """A `User`."""
  User
  """An `Account`."""
  Account
  """A `Contact`."""
  Contact
  """A `Network Site`."""
  NetworkSite
  """A `Ticket`."""
  Ticket
  """A `TicketReply`."""
  TicketReply
  """A `Vendor`."""
  Vendor
  """A `PurchaseOrder`"""
  PurchaseOrder
}

"""The type of entity that owns this `File`."""
enum FileableType {
  """A customer account."""
  Account
  """An ACH batch file."""
  AchBatch
  """A geographical address."""
  Address
  """An import of call data records (CDRs)."""
  CallDataRecordImport
  """An import of call detail records (CDRs)."""
  CallDetailRecordImport
  """A call log."""
  CallLog
  """A company you do business as."""
  Company
  """A deposit slip."""
  DepositSlip
  """The localized content of an `EmailMessage`."""
  EmailMessageContent
  """A generated FCC Form 477 report."""
  FccForm477Report
  """The signature on a contract."""
  HandwrittenSignature
  """An inventory item."""
  InventoryItem
  """A type of item stored in inventory."""
  InventoryModel
  """A PDF to attach to invoices."""
  InvoiceAttachment
  """A job, typically in the field."""
  Job
  """A mass email communication."""
  MassEmail
  """A network site."""
  NetworkSite
  """A single PDF containing multiple invoices for printing."""
  PrintedInvoiceBatch
  """A purchase order for items from a third party vendor."""
  PurchaseOrder
  """A backup of your Sonar instance's data."""
  SystemBackup
  """types.test_read_only_file_model"""
  TestReadOnlyFileModel
  """A ticket."""
  Ticket
  """A comment on a `Ticket`."""
  TicketComment
  """A reply on a `Ticket`."""
  TicketReply
  """A TowerCoverage submission."""
  TowercoverageSubmission
  """A third party vendor of inventory models."""
  Vendor
  """An import of voice provider rates."""
  VoiceProviderRateImport
}

"""The type of entity to be imported."""
enum ImportableType {
  """A call detail record (CDR)."""
  CallDetailRecord
  """A direct inward dial (DID)."""
  Did
  """A voice provider rate."""
  VoiceProviderRate
}

"""The entity that this `Import` is associated with."""
enum ImportrecipeableType {
  """A recipe for importing call detail records (CDRs)."""
  CallDetailRecordImportRecipe
  """A recipe for importing DIDs."""
  DidImportRecipe
  """A recipe for importing voice provider rates."""
  VoiceProviderRateImportRecipe
}

"""The entity that owns an `InventoryItem`."""
enum InventoryitemableType {
  """A `User`."""
  User
  """An `InventoryLocation`."""
  InventoryLocation
  """A `GenericInventoryAssignee`."""
  GenericInventoryAssignee
  """A `Vehicle`."""
  Vehicle
  """An `InternalLocation`."""
  InternalLocation
  """A serviceable `Address`."""
  Address
  """A `NetworkSite`."""
  NetworkSite
}

"""The owner of an `IpAssignment`."""
enum IpassignmentableType {
  """An `Account`."""
  Account
  """An `InventoryItem`."""
  InventoryItem
  """An `InventoryModelFieldData`."""
  InventoryModelFieldData
  """A `RadiusAccount`."""
  RadiusAccount
  """An `UninventoriedMacAddress`."""
  UninventoriedMacAddress
  """A `NetworkSite`."""
  NetworkSite
}

"""The owner of an `IPAssignmentHistory`."""
enum IpassignmenthistoryableType {
  """An `Account`."""
  Account
  """A `NetworkSite`."""
  NetworkSite
}

"""The ISP type of a `Company`."""
enum IspType {
  """ILEC"""
  ILEC
  """CLEC"""
  CLEC
  """IXC"""
  IXC
  """VOIP"""
  VOIP
  """ISP"""
  ISP
  """Wireless"""
  WIRELESS
  """Retail Sales"""
  RETAIL_SALES
}

"""The type of entity that owns this `Job`."""
enum JobbableType {
  """An `Account`."""
  Account
  """A `NetworkSite`."""
  NetworkSite
}

"""The action taken on a job completion or failure."""
enum JobTypeAction {
  """Create new ticket"""
  CREATE_NEW_TICKET
  """Update linked ticket, create new ticket if no ticket linked"""
  UPDATE_TICKET_OR_ADD
  """None"""
  NONE
}

"""A type of `Log` entry."""
enum LogType {
  """Entity was created"""
  CREATED
  """Entity was updated"""
  UPDATED
  """Entity was deleted"""
  DELETED
  """An entity was attached to another"""
  ATTACHED
  """An entity was detached from another"""
  DETACHED
  """A system log entry."""
  SYSTEM
  """A log entry that doesn't match another log type."""
  OTHER
}

"""An entity that can have a `Note` associated with it."""
enum NoteableType {
  """An access log history on an entity."""
  AccessLog
  """A customer account."""
  Account
  """An account Adtran Mosaic service detail."""
  AccountAdtranMosaicServiceDetail
  """A tracked event that has occurred for an `Account`."""
  AccountEvent
  """An account group."""
  AccountGroup
  """The status of an account."""
  AccountStatus
  """The account type."""
  AccountType
  """
  A voice service configuration that links a service parameter to an account.
  """
  AccountVoiceServiceDetail
  """An ACH batch file."""
  AchBatch
  """
  An address list defines some criteria by which to group accounts for network policy enforcement.
  """
  AddressList
  """An address status."""
  AddressStatus
  """An Adtran Mosaic audit record."""
  AdtranMosaicAudit
  """An Adtran Mosaic Kafka event record."""
  AdtranMosaicKafkaEvent
  """An Adtran Mosaic settings record."""
  AdtranMosaicSetting
  """An Adtran Mosaic workflow event record."""
  AdtranMosaicWorkflowEvent
  """An alerting rotation."""
  AlertingRotation
  """An alerting rotation day."""
  AlertingRotationDay
  """An application firewall IP address or subnet rule."""
  ApplicationFirewallRule
  """A tax category defined by Avalara."""
  AvalaraTaxCategory
  """A bank account."""
  BankAccount
  """A credential used when processing bank account payments."""
  BankAccountProcessorCredential
  """A cable modem provisioner."""
  CableModemProvisioner
  """A cable modem provisioner credential."""
  CableModemProvisionerCredential
  """A Calix Cloud audit record."""
  CalixCloudAudit
  """A Calix Cloud setting."""
  CalixCloudSetting
  """A configuration for a specific Calix SMx endpoint."""
  CalixIntegration
  """An import of call data records (CDRs)."""
  CallDataRecordImport
  """An import of call detail records (CDRs)."""
  CallDetailRecordImport
  """A recipe for importing call detail records (CDRs)."""
  CallDetailRecordImportRecipe
  """A canned reply."""
  CannedReply
  """A canned reply category."""
  CannedReplyCategory
  """A company you do business as."""
  Company
  """A contact person."""
  Contact
  """A contract."""
  Contract
  """A contract template."""
  ContractTemplate
  """A credit card."""
  CreditCard
  """A user defined field."""
  CustomField
  """Details regarding a specific data `Service`."""
  DataServiceDetail
  """A data usage history entry."""
  DataUsageHistory
  """A data usage top off."""
  DataUsageTopOff
  """A period of time when invoices are not evaluated for delinquency."""
  DelinquencyExclusion
  """A department."""
  Department
  """The mode that an inventory item is deployed in."""
  DeploymentType
  """A deposit slip."""
  DepositSlip
  """A DHCP server."""
  DhcpServer
  """A specific identifier for a DHCP server."""
  DhcpServerIdentifier
  """A direct inward dial (DID)."""
  Did
  """A direct inward dial (DID) assignment."""
  DidAssignment
  """A recipe for importing DIDs."""
  DidImportRecipe
  """A disbursement."""
  Disbursement
  """A disbursement detail."""
  DisbursementDetail
  """The `Account` disconnections log."""
  DisconnectionLog
  """A dispute."""
  Dispute
  """A categorization of an `Email` by type."""
  EmailCategory
  """An email domain."""
  EmailDomain
  """An email message."""
  EmailMessage
  """An LTE EPC."""
  Epc
  """The `ExternalMarketingProvider` credentials for integration."""
  ExternalMarketingProviderCredential
  """FiberMap integration."""
  FibermapIntegration
  """FiberMap plan."""
  FibermapPlan
  """FiberMap service location."""
  FibermapServiceLocation
  """
  A fractional debit, stored to accurately calculate multi month billing.
  """
  FractionalDebit
  """
  A fractional tax transaction, stored to accurately calculate multi month billing.
  """
  FractionalTaxTransaction
  """A general ledger code."""
  GeneralLedgerCode
  """A generic assignee for inventory items."""
  GenericInventoryAssignee
  """A generic inventory item."""
  GenericInventoryItem
  """A geographical tax zone."""
  GeoTaxZone
  """A geographical restriction."""
  Geofence
  """
  Defines the minimum and maximum of an inventory level for all locations per inventory model.
  """
  GlobalInventoryModelMinMax
  """Details regarding an ActiveDirectory `IdentityProvider`."""
  IdentityProviderActiveDirectoryDetail
  """Details regarding a Google `IdentityProvider`."""
  IdentityProviderGoogleDetail
  """Details regarding a Microsoft `IdentityProvider`."""
  IdentityProviderMicrosoftDetail
  """Details regarding a SAML `IdentityProvider`."""
  IdentityProviderSamlDetail
  """An import."""
  Import
  """An inbound mailbox."""
  InboundMailbox
  """
  A device that sits inline with customer traffic to impose network policy.
  """
  InlineDevice
  """An inline device credential."""
  InlineDeviceCredential
  """
  An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
  """
  IntegrationFieldMapping
  """An entity which maps a service to a vendor specific service name"""
  IntegrationServiceMapping
  """A location inside an `InventoryLocation` (e.g. a shelf or a room.)"""
  InternalLocation
  """An inventory item."""
  InventoryItem
  """A location that inventory is stored in."""
  InventoryLocation
  """A type of item stored in inventory."""
  InventoryModel
  """A category of item stored in inventory."""
  InventoryModelCategory
  """A field on an inventory model."""
  InventoryModelField
  """
  Defines the minimum and maximum of an inventory level per location per inventory model.
  """
  InventoryModelMinMax
  """A PDF to attach to invoices."""
  InvoiceAttachment
  """A message that is appended to specific invoices."""
  InvoiceMessage
  """A template for generating invoices."""
  InvoiceTemplate
  """
  A version of a template for generating invoices, preserved for historical purposes.
  """
  InvoiceTemplateVersion
  """An IP address assignment."""
  IpAssignment
  """An IP pool, used for single address assignments (e.g. DHCP, PPPoE.)"""
  IpPool
  """A job, typically in the field."""
  Job
  """The type of a `Job`."""
  JobType
  """A local prefix for a voice service."""
  LocalPrefix
  """A report builder license."""
  LookerExploreLicense
  """A report viewer license."""
  LookerViewLicense
  """A provider of LTE provisioning."""
  LteProvider
  """Credentials for an `LteProvider`."""
  LteProviderCredential
  """A manufacturer of an item stored in inventory."""
  Manufacturer
  """Map Overlay."""
  MapOverlay
  """A mass email communication."""
  MassEmail
  """A categorization of a message by type."""
  MessageCategory
  """A record of a monthly billing cycle."""
  MonthlyBillingCompletion
  """A subnet allowed to send data to a Netflow endpoint."""
  NetflowAllowedSubnet
  """A Netflow endpoint."""
  NetflowEndpoint
  """A Netflow on premise record."""
  NetflowOnPremise
  """A whitelisted subnet for a Netflow endpoint."""
  NetflowWhitelist
  """A `NetworkMonitoringGraph`."""
  NetworkMonitoringGraph
  """A `NetworkMonitoringTemplate`."""
  NetworkMonitoringTemplate
  """A network site."""
  NetworkSite
  """Network site serviceable address list."""
  NetworkSiteServiceableAddressList
  """
  An item purchasable from vendors that does not have an `Inventory Model` associated with it
  """
  NonInventoryItem
  """An order group."""
  OrderGroup
  """Details regarding a specific overage `Service`."""
  OverageServiceDetail
  """A collection of `Service`s."""
  Package
  """Paypal credentials for external payments."""
  PayPalCredential
  """An access token for the API."""
  PersonalAccessToken
  """A `Poller`."""
  Poller
  """Poller configuration settings."""
  PollerSetting
  """Preseem integration."""
  Preseem
  """A single PDF containing multiple invoices for printing."""
  PrintedInvoiceBatch
  """A purchase order for items from a third party vendor."""
  PurchaseOrder
  """A line item on a purchase order."""
  PurchaseOrderItem
  """A RADIUS account."""
  RadiusAccount
  """A RADIUS group."""
  RadiusGroup
  """A RADIUS group reply attribute."""
  RadiusGroupReplyAttribute
  """A RADIUS server."""
  RadiusServer
  """The history of a RADIUS session."""
  RadiusSessionHistory
  """A rate center."""
  RateCenter
  """A record of a refund applied to a `Payment`."""
  RefundedPayment
  """A record a `Payment` reversal."""
  ReversedPayment
  """A role defines the permission set that a user has."""
  Role
  """Saved message category."""
  SavedMessageCategory
  """The geographical point that a technician starts or ends their day at."""
  ScheduleAddress
  """Availability for `Job`s to be scheduled."""
  ScheduleAvailability
  """
  An event that blocks off part of a calendar otherwise availability due to `ScheduleAvailability`.
  """
  ScheduleBlocker
  """
  An override to a particular day and time a `ScheduleBlocker` would otherwise cover.
  """
  ScheduleBlockerOverride
  """Time off that removes availability from a `ScheduleAvailability`."""
  ScheduleTimeOff
  """
  The `AccountCalixServiceDetail` records used to configure the Calix integrations when a `ScheduledEvent` is executed.
  """
  ScheduledEventAccountCalixServiceDetail
  """
  The `AccountVoiceServiceDetail` records used to configure a voice service when a `ScheduledEvent` is executed.
  """
  ScheduledEventAccountVoiceServiceDetail
  """A service."""
  Service
  """A signature."""
  Signature
  """An SMS message."""
  SmsMessage
  """An SMS message content."""
  SmsMessageContent
  """SMS configuration settings."""
  SmsSetting
  """An `SnmpOid`."""
  SnmpOid
  """An `SnmpOidThreshold`."""
  SnmpOidThreshold
  """An `SnmpOverride`."""
  SnmpOverride
  """A stored view."""
  StoredView
  """An IPv4/IPv6 subnet."""
  Subnet
  """
  The largest example of a unique subnet on your network. A supernet contains
  many subnets. An example of a supernet is 10.0.0.0/8.
  """
  Supernet
  """A backup of your Sonar instance's data."""
  SystemBackup
  """A configured destination to export system backups to."""
  SystemBackupDestination
  """
  A credential used to authenticate against configured destinations to export system backups to.
  """
  SystemBackupDestinationCredential
  """A log of a system backup export attempt."""
  SystemBackupExport
  """The settings for system backups in your Sonar instance."""
  SystemBackupSetting
  """A tax."""
  Tax
  """A tax exemption."""
  TaxExemption
  """An override to the default taxation rate."""
  TaxOverride
  """A tax provider."""
  TaxProvider
  """Credentials for a `TaxProvider`."""
  TaxProviderCredential
  """types.test_read_only_file_model"""
  TestReadOnlyFileModel
  """A ticket category."""
  TicketCategory
  """A ticket group."""
  TicketGroup
  """A ticket recipient."""
  TicketRecipient
  """TowerCoverage integration."""
  TowercoverageConfiguration
  """A TowerCoverage submission."""
  TowercoverageSubmission
  """An `Email` that is sent when a particular event occurs."""
  TriggeredEmail
  """A message that is sent when a specific event occurs."""
  TriggeredMessage
  """A MAC address that is not recorded in the inventory system."""
  UninventoriedMacAddress
  """A usage based billing policy."""
  UsageBasedBillingPolicy
  """A period of free time in a `UsageBasedBillingPolicy`."""
  UsageBasedBillingPolicyFreePeriod
  """A vehicle."""
  Vehicle
  """A third party vendor of inventory models."""
  Vendor
  """An item that can be purchased from a particular vendor."""
  VendorItem
  """A `VoiceProvider`."""
  VoiceProvider
  """An import of voice provider rates."""
  VoiceProviderRateImport
  """A recipe for importing voice provider rates."""
  VoiceProviderRateImportRecipe
  """Details regarding a specific voice `Service`."""
  VoiceServiceDetail
  """A configurable attribute for a voice service."""
  VoiceServiceGenericParameter
  """A record of a `Payment` that was voided."""
  VoidedPayment
  """A URL to an endpoint that a webhook can be sent to."""
  WebhookEndpoint
  """An event on a model that can fire a webhook"""
  WebhookEndpointEvent
  """A webhook for a model and event that has been queued to be sent."""
  WebhookEndpointEventDispatch
  """A send attempt of a dispatched webhook for a model and event."""
  WebhookEndpointEventDispatchAttempt
}

"""The type of entity that is related to this `Notification`."""
enum NotifiableType {
  """A `Task`."""
  Task
  """A `Ticket`."""
  Ticket
  """A `Job`."""
  Job
  """An `InventoryItem`."""
  InventoryItem
  """A `PurchaseOrder`."""
  PurchaseOrder
  """A `Print to mail batch`."""
  PrintToMailBatch
  """An `InboundMailbox`."""
  InboundMailbox
  """A `Dispute`."""
  Dispute
  """An `Import`."""
  Import
  """A `SystemBackup`."""
  SystemBackup
  """A `SystemBackupExport`."""
  SystemBackupExport
  """A `DHCP Server`."""
  DhcpServer
  """An `Inline Device`."""
  InlineDevice
  """A `CallDetailRecordImport`."""
  CallDetailRecordImport
  """A `VoiceProviderRateImport`."""
  VoiceProviderRateImport
  """A `Fibermap Plan`."""
  FibermapPlan
  """An `Adtran Mosaic Setting`."""
  AdtranMosaicSetting
}

"""The type of notification."""
enum NotificationType {
  """When a job is assigned to me"""
  JOB_ASSIGNED
  """When a job assigned to me is completed successfully"""
  JOB_COMPLETED
  """When a job assigned to me is completed unsuccessfully"""
  JOB_FAILED
  """When a job assigned to me is rescheduled"""
  JOB_RESCHEDULED
  """When a network alert is generated for one of my alerting rotations"""
  NETWORK_ALERT
  """When a dispute is created"""
  DISPUTE_CREATED
  """When a dispute status becomes `won` or `lost`"""
  DISPUTE_WON_OR_LOST
  """When a ticket is assigned to me"""
  TICKET_ASSIGNED
  """When a ticket is assigned to a group I belong to"""
  TICKET_ASSIGNED_GROUP
  """When a ticket assigned to me receives a reply"""
  TICKET_REPLIED
  """When a ticket assigned to a group I belong to receives a reply"""
  TICKET_REPLIED_GROUP
  """When a ticket assigned to me receives a comment"""
  TICKET_COMMENTED
  """When a ticket assigned to a group I belong to receives a comment"""
  TICKET_COMMENTED_GROUP
  """When a task is assigned to me"""
  TASK_ASSIGNED
  """When a task assigned to me is due soon"""
  TASK_DUE_SOON
  """When a task assigned to me is past due"""
  TASK_PAST_DUE
  """When an import completes successfully"""
  IMPORT_COMPLETED
  """When an import fails"""
  IMPORT_FAILED
  """
  When a purchase order I approved or created could not be emailed to its vendor
  """
  PURCHASE_ORDER_FAILED_TO_EMAIL_VENDOR
  """When any purchase order is approved"""
  PURCHASE_ORDER_APPROVED
  """When a purchase order is canceled"""
  PURCHASE_ORDER_CANCELED
  """When a purchase order created by me is approved"""
  OWN_PURCHASE_ORDER_APPROVED
  """When any purchase order is marked as complete"""
  PURCHASE_ORDER_COMPLETE
  """When a product request is created and needs approval"""
  PRODUCT_REQUEST_CREATED
  """When a purchase order created by me is rejected"""
  PRODUCT_REQUEST_REJECTED
  """When a print to mail batch fails"""
  PRINT_TO_MAIL_BATCH_FAILED
  """
  When there are insufficient funds available to send a print to mail batch
  """
  PRINT_TO_MAIL_BATCH_INSUFFICIENT_FUNDS
  """When a print to mail batch has completed"""
  PRINT_TO_MAIL_BATCH_COMPLETED
  """
  When the funds available for print to mail fall below the configured threshold
  """
  PRINT_TO_MAIL_FUNDS_BELOW_THRESHOLD
  """
  When the funds available for SMS messages fall below the configured threshold
  """
  SMS_FUNDS_BELOW_THRESHOLD
  """When there are insufficient funds available to send an SMS message"""
  SMS_INSUFFICIENT_FUNDS
  """When a system backup fails"""
  SYSTEM_BACKUP_FAILED
  """When a Plan is imported from Vetro FiberMap"""
  FIBERMAP_PLANS_CREATED
  """
  When an inbound mailbox slack integration is disabled due to repeated failures
  """
  INBOUND_MAILBOX_SLACK_DISABLED
  """When there are synchronization events for a DHCP Server"""
  SYNCHRONIZATION_EVENTS_DHCP
  """When there are synchronization events for an Inline Device"""
  SYNCHRONIZATION_EVENTS_INLINE
  """When there are updates to the Adtran Mosaic cloud live audit"""
  ADTRAN_MOSAIC_AUDIT_UPDATE
}

"""The type of `Payment` made."""
enum PaymentType {
  """Credit card"""
  CREDITCARD
  """Bank"""
  BANKACCOUNT
  """Cash"""
  CASH
  """Wire"""
  WIRE
  """Check"""
  CHECK
  """Other"""
  OTHER
  """PayPal"""
  PAYPAL
}

"""A type of entity that can have a recent item entry."""
enum RecentitemableType {
  """An `Account`"""
  Account
  """A `Ticket`"""
  Ticket
  """An `InventoryItem`"""
  InventoryItem
  """A `NetworkSite`"""
  NetworkSite
  """A `Job`"""
  Job
}

"""The primary type of a `Service`"""
enum ServiceType {
  """A recurring service"""
  RECURRING
  """An expiring service"""
  EXPIRING
  """A service that applies a one time charge"""
  ONETIME
  """A service that applies a data overage"""
  OVERAGE
  """A service that can be used to apply an adjustment to an account"""
  ADJUSTMENT
  """A data service."""
  DATA
  """A voice service."""
  VOICE
}

"""The entity that this `SMS` is associated with."""
enum SmsableType {
  """A `User`."""
  User
  """A `Contact`."""
  Contact
}

"""
A subnet type defines what kind of entity an IP assignment within an subnet can be assigned to.
"""
enum SubnetType {
  """A subnet that allows assignments to any entity"""
  MIXED
  """A subnet that is only allowed to be used for assignment to an account"""
  ACCOUNT
  """
  A subnet that is only allowed to be used for assignment to a network site
  """
  NETWORK
  """A subnet that cannot be currently used for assignment"""
  EXCLUDED
}

"""The type of entity subscribed to."""
enum SubscribableType {
  """A `Ticket`."""
  Ticket
}

"""A type of entity that can have a task associated with it."""
enum TaskableType {
  """A customer account."""
  Account
  """An inventory item."""
  InventoryItem
  """A job, typically in the field."""
  Job
  """A network site."""
  NetworkSite
  """types.test_read_only_file_model"""
  TestReadOnlyFileModel
  """A ticket."""
  Ticket
}

"""The type of `TaxDefinition` that this entity is associated with."""
enum TaxdefinitionableType {
  """An `AvalaraTaxDefinition`."""
  AvalaraTaxDefinition
}

"""The entity that this `TaxTransaction` is associated with."""
enum TaxtransactionableType {
  """A `Debit`."""
  Debit
  """A `Discount`."""
  Discount
}

"""Whether a `Tax` is applied globally or geographically."""
enum TaxType {
  """A tax that is only applied in a certain geography"""
  GEOGRAPHICAL
  """A tax that is applied to all customers, regardless of geography"""
  GLOBAL
}

"""The type of entity that owns this `Ticket`."""
enum TicketableType {
  """An `Account`."""
  Account
  """A `NetworkSite`."""
  NetworkSite
}

"""A type of transaction."""
enum TransactionType {
  """Debit."""
  DEBIT
  """Discount."""
  DISCOUNT
  """Payment."""
  PAYMENT
}

"""An entity that can have a `Vendor Item` associated with it."""
enum VendoritemableType {
  """Non-Inventory Item"""
  NonInventoryItem
  """Inventory Model"""
  InventoryModel
}
```
