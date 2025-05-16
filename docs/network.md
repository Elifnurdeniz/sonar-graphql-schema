```graphql
"""A `NetworkMonitoringGraph`."""
type NetworkMonitoringGraph implements NoteableInterface & LoggableInterface & AccessloggableInterface {
  """The ID of the entity."""
  id: Int64Bit!
  """
  An ID that uniquely identifies this entity across the whole Sonar system.
  """
  sonar_unique_id: ID!
  """The date and time this entity was created."""
  created_at: Datetime!
  """The last date and time this entity was modified."""
  updated_at: Datetime!
  """
  A string that shows the version of this entity. It will be incremented whenever the entity is modified.
  """
  _version: String!
  """A descriptive name."""
  name: String!
  """The ID of a `NetworkMonitoringTemplate`."""
  network_monitoring_template_id: Int64Bit!
  """Stacked"""
  stacked: Boolean!
  """The type."""
  type: NetworkMonitoringGraphType!
  """A `NetworkMonitoringTemplate`."""
  network_monitoring_template(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Whether or not to collect interface statistics."""
    collect_interface_statistics: Boolean
    """ICMP latency threshold (ms)."""
    icmp_latency_threshold: Int
    """ICMP loss threshold (%)."""
    icmp_loss_threshold: Int
    """Whether or not ICMP monitoring is enabled."""
    icmp_monitoring: Boolean
    """A descriptive name."""
    name: String
    """SNMPv3 auth passphrase"""
    snmp3_auth_passphrase: Text
    """SNMPv3 auth protocol"""
    snmp3_auth_protocol: Snmp3AuthProtocol
    """SNMPv3 context engine ID"""
    snmp3_context_engineid: Text
    """SNMPv3 context name"""
    snmp3_context_name: Text
    """SNMPv3 privacy passphrase"""
    snmp3_priv_passphrase: Text
    """SNMPv3 privacy protocol"""
    snmp3_priv_protocol: Snmp3PrivProtocol
    """SNMPv3 security level"""
    snmp3_sec_level: Snmp3SecurityLevel
    """SNMP community/securityName"""
    snmp_community: Text
    """SNMP version"""
    snmp_version: SnmpVersion
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NetworkMonitoringTemplate
  """An `SnmpOid`."""
  snmp_oids(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Whether or not to auto scale."""
    auto_scale: Boolean
    """Color."""
    color: HtmlHexColor
    """Display as table"""
    display_as_table: Boolean
    """Divide by"""
    divide_by: Int
    """A descriptive name."""
    name: String
    """The ID of a `NetworkMonitoringGraph`."""
    network_monitoring_graph_id: Int64Bit
    """An OID"""
    oid: String
    """Unit of measurement"""
    unit_of_measurement: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): SnmpOidConnection!
  """A note."""
  notes(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The message."""
    message: Text
    """The ID of the entity that owns this note."""
    noteable_id: Int64Bit
    """The type of entity that owns this note."""
    noteable_type: NoteableType
    """The priority of this item."""
    priority: NotePriority
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NoteConnection!
  """A log entry."""
  logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Current data."""
    current: Text
    """
    Whether or not this log was transferred from a Sonar v1 instance. If so, the
    formatting will not match current version logs.
    """
    legacy: Boolean
    """
    A title which is only populated on logs that were imported from Sonar v1.
    """
    legacy_title: String
    """The severity level."""
    level: LogLevel
    """The ID of the entity that this log is attached to."""
    loggable_id: Int64Bit
    """The type of entity that this log is attached to."""
    loggable_type: String
    """The entity ID that triggered the log."""
    logged_entity_id: Int64Bit
    """The entity that triggered the log."""
    logged_entity_type: String
    """The message."""
    message: Text
    """Previous data."""
    previous: Text
    """Data from objects related to this change."""
    relation_data: Text
    """The type."""
    type: LogType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): LogConnection!
  """An access log history on an entity."""
  access_logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The date and time that this entity was accessed."""
    access_datetime: Datetime
    """The ID of the entity that this access log belongs to."""
    accessloggable_id: Int64Bit
    """The entity that this access log belongs to."""
    accessloggable_type: String
    """The ID of the entity that this access log belongs to."""
    entity_id: Int64Bit
    """The entity that this access log belongs to."""
    entity_name: String
    """The ID of the user that accessed this entity."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AccessLogConnection!
}

"""
The connection wrapper around the `NetworkMonitoringGraphConnection` type.
"""
type NetworkMonitoringGraphConnection {
  """A list of the entities provided by this connection."""
  entities: [NetworkMonitoringGraph]!
  """
  An object providing information about the page of results being displayed, as
  well as the total amount of pages/records available.
  """
  page_info: PageInfo!
  """
  Provides the ability to return aggregated mathematical data about your results.
  """
  aggregations: [Aggregation]!
}

"""A `NetworkMonitoringTemplate`."""
type NetworkMonitoringTemplate implements NoteableInterface & LoggableInterface & AccessloggableInterface {
  """The ID of the entity."""
  id: Int64Bit!
  """
  An ID that uniquely identifies this entity across the whole Sonar system.
  """
  sonar_unique_id: ID!
  """The date and time this entity was created."""
  created_at: Datetime!
  """The last date and time this entity was modified."""
  updated_at: Datetime!
  """
  A string that shows the version of this entity. It will be incremented whenever the entity is modified.
  """
  _version: String!
  """Whether or not to collect interface statistics."""
  collect_interface_statistics: Boolean!
  """ICMP latency threshold (ms)."""
  icmp_latency_threshold: Int
  """ICMP loss threshold (%)."""
  icmp_loss_threshold: Int
  """Whether or not ICMP monitoring is enabled."""
  icmp_monitoring: Boolean!
  """A descriptive name."""
  name: String!
  """SNMPv3 auth passphrase"""
  snmp3_auth_passphrase: Text
  """SNMPv3 auth protocol"""
  snmp3_auth_protocol: Snmp3AuthProtocol
  """SNMPv3 context engine ID"""
  snmp3_context_engineid: Text
  """SNMPv3 context name"""
  snmp3_context_name: Text
  """SNMPv3 privacy passphrase"""
  snmp3_priv_passphrase: Text
  """SNMPv3 privacy protocol"""
  snmp3_priv_protocol: Snmp3PrivProtocol
  """SNMPv3 security level"""
  snmp3_sec_level: Snmp3SecurityLevel
  """SNMP community/securityName"""
  snmp_community: Text
  """SNMP version"""
  snmp_version: SnmpVersion
  """A type of item stored in inventory."""
  inventory_models(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """
    Sets the default vendor to be used for purchasing this inventory model.
    """
    default_vendor_id: Int64Bit
    """The type of inventory model."""
    device_type: InventoryModelDeviceType
    """Whether or not this is enabled."""
    enabled: Boolean
    """Whether or not this is generic."""
    generic: Boolean
    """An icon."""
    icon: Icon
    """The ID of an InventoryModelCategory."""
    inventory_model_category_id: Int64Bit
    """Whether or not inventory item can be broken down into segments."""
    is_segmentable: Boolean
    """
    If this is a SIM card for LTE provisioning, which provider this SIM is for.
    """
    lte_sim_type: LteProviderType
    """The ID of a Manufacturer."""
    manufacturer_id: Int64Bit
    """The actual model name/part number."""
    model_name: String
    """A descriptive name."""
    name: String
    """The ID of a `NetworkMonitoringTemplate`."""
    network_monitoring_template_id: Int64Bit
    """
    The TCP port that the web interface of this type of device is available on.
    """
    port: Int
    """The protocol used to access the web interface."""
    protocol: Protocol
    """The quantity of this inventory model."""
    quantity: Int
    """The unit of measurement for this inventory model."""
    unit_of_measurement: UnitOfMeasurementType
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): InventoryModelConnection!
  """The mode that an inventory item is deployed in."""
  deployment_types(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The ID of an `InventoryModel`."""
    inventory_model_id: Int64Bit
    """A descriptive name."""
    name: String
    """The ID of a `NetworkMonitoringTemplate`."""
    network_monitoring_template_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): DeploymentTypeConnection!
  """A `NetworkMonitoringGraph`."""
  network_monitoring_graphs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """A descriptive name."""
    name: String
    """The ID of a `NetworkMonitoringTemplate`."""
    network_monitoring_template_id: Int64Bit
    """Stacked"""
    stacked: Boolean
    """The type."""
    type: NetworkMonitoringGraphType
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NetworkMonitoringGraphConnection!
  """A note."""
  notes(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The message."""
    message: Text
    """The ID of the entity that owns this note."""
    noteable_id: Int64Bit
    """The type of entity that owns this note."""
    noteable_type: NoteableType
    """The priority of this item."""
    priority: NotePriority
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NoteConnection!
  """A log entry."""
  logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Current data."""
    current: Text
    """
    Whether or not this log was transferred from a Sonar v1 instance. If so, the
    formatting will not match current version logs.
    """
    legacy: Boolean
    """
    A title which is only populated on logs that were imported from Sonar v1.
    """
    legacy_title: String
    """The severity level."""
    level: LogLevel
    """The ID of the entity that this log is attached to."""
    loggable_id: Int64Bit
    """The type of entity that this log is attached to."""
    loggable_type: String
    """The entity ID that triggered the log."""
    logged_entity_id: Int64Bit
    """The entity that triggered the log."""
    logged_entity_type: String
    """The message."""
    message: Text
    """Previous data."""
    previous: Text
    """Data from objects related to this change."""
    relation_data: Text
    """The type."""
    type: LogType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): LogConnection!
  """An access log history on an entity."""
  access_logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The date and time that this entity was accessed."""
    access_datetime: Datetime
    """The ID of the entity that this access log belongs to."""
    accessloggable_id: Int64Bit
    """The entity that this access log belongs to."""
    accessloggable_type: String
    """The ID of the entity that this access log belongs to."""
    entity_id: Int64Bit
    """The entity that this access log belongs to."""
    entity_name: String
    """The ID of the user that accessed this entity."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AccessLogConnection!
}

"""
The connection wrapper around the `NetworkMonitoringTemplateConnection` type.
"""
type NetworkMonitoringTemplateConnection {
  """A list of the entities provided by this connection."""
  entities: [NetworkMonitoringTemplate]!
  """
  An object providing information about the page of results being displayed, as
  well as the total amount of pages/records available.
  """
  page_info: PageInfo!
  """
  Provides the ability to return aggregated mathematical data about your results.
  """
  aggregations: [Aggregation]!
}

"""A network site."""
type NetworkSite implements SearchableInterface & ContactableInterface & TicketableInterface & JobbableInterface & InventoryitemableInterface & AddressableInterface & IpassignmentableInterface & IpassignmenthistoryableInterface & GenericinventoryitemableInterface & GenericinventoryitemactionloggableInterface & EmailableInterface & NoteableInterface & CustomfielddataableInterface & FileableInterface & RecentitemableInterface & TaskableInterface & LoggableInterface & AccessloggableInterface {
  """The ID of the entity."""
  id: Int64Bit!
  """
  An ID that uniquely identifies this entity across the whole Sonar system.
  """
  sonar_unique_id: ID!
  """The date and time this entity was created."""
  created_at: Datetime!
  """The last date and time this entity was modified."""
  updated_at: Datetime!
  """
  A string that shows the version of this entity. It will be incremented whenever the entity is modified.
  """
  _version: String!
  """A geo-point."""
  geopoint: Geopoint
  """Height in meters."""
  height_in_meters: Float!
  """A descriptive name."""
  name: String!
  """Network site serviceable address list."""
  network_site_serviceable_address_list(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Network site id."""
    network_site_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NetworkSiteServiceableAddressList
  """A contact person."""
  contacts(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The ID of the entity that owns this contact."""
    contactable_id: Int64Bit
    """The type of entity that owns this contact."""
    contactable_type: ContactableType
    """An email address."""
    email_address: EmailAddress
    """A supported language."""
    language: Language
    """Whether or not marketing messages accepted."""
    marketing_opt_in: Boolean
    """A descriptive name."""
    name: String
    """Whether or not this is the primary type of entity."""
    primary: Boolean
    """The role of the contact, e.g. "CEO" or "Network Engineer"."""
    role: String
    """A username, used for authentication."""
    username: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): ContactConnection!
  """A ticket."""
  tickets(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """
    The last date and time this entity was updated, or was the subject of a log.
    """
    global_updated_at: Datetime
    """The time this was closed at."""
    closed_at: Datetime
    """The ID of the `User` that closed this."""
    closed_by_user_id: Int64Bit
    """The ID of the company that this entity operates under."""
    company_id: Int64Bit
    """A human readable description."""
    description: Text
    """The date this invoice is due by."""
    due_date: Date
    """The ID of an `InboundMailbox`."""
    inbound_mailbox_id: Int64Bit
    """Indicates if this ticket is marked as spam."""
    is_spam: Boolean
    """The ID of the `Ticket` that this `Ticket` is a child of."""
    parent_ticket_id: Int64Bit
    """The priority of this item."""
    priority: TicketPriority
    """Mail processor's spam rating for whether or not this is spam."""
    spam_score: Float
    """The status."""
    status: TicketStatus
    """The subject."""
    subject: String
    """The ID of a `TicketGroup`."""
    ticket_group_id: Int64Bit
    """The ID of the entity that this `Ticket` is associated with."""
    ticketable_id: Int64Bit
    """The type of entity that this `Ticket` is associated with."""
    ticketable_type: TicketableType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): TicketConnection!
  """A job, typically in the field."""
  jobs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The serviceable address where this job was completed."""
    address_on_completion: String
    """Whether or not this is complete."""
    complete: Boolean
    """The `User` that completed this."""
    completed_by_user_id: Int64Bit
    """Whether this `Job` was completed successfully or not."""
    completed_successfully: Boolean
    """The date and time this `Job` was completed."""
    completion_datetime: Datetime
    """Any notes entered when this `Job` was completed."""
    completion_notes: Text
    """The ID of a `JobType`."""
    job_type_id: Int64Bit
    """The ID of the entity that this `Job` is associated with."""
    jobbable_id: Int64Bit
    """The type of entity that this `Job` is associated with."""
    jobbable_type: JobbableType
    """The length in minutes for this `Job`."""
    length_in_minutes: Int
    """The date and time this `Job` is scheduled for."""
    scheduled_datetime: Datetime
    """The ID of the serviceable address account assignment future."""
    serviceable_address_account_assignment_future_id: Int64Bit
    """
    Indicates this entity has skipped the validations which would normally apply.
    """
    skips_validation: Boolean
    """The ID of a `Ticket`."""
    ticket_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): JobConnection!
  """An inventory item."""
  inventory_items(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The ID of an AccountService."""
    account_service_id: Int64Bit
    """The ID of the `User` that claimed this."""
    claimed_user_id: Int64Bit
    """The ID of a `DeploymentType`."""
    deployment_type_id: Int64Bit
    """Whether this inventory item is flapping or not."""
    flapping: Boolean
    """The current ICMP monitoring status of an `InventoryItem`."""
    icmp_device_status: InventoryItemDeviceStatus
    """The number of times the ICMP status has flapped."""
    icmp_status_flap_count: Int
    """The timestamp of when the ICMP status last changed."""
    icmp_status_last_change: Datetime
    """The ICMP monitoring threshold violation type."""
    icmp_threshold_violation: InventoryItemIcmpThresholdViolation
    """The ID of an `InventoryModel`."""
    inventory_model_id: Int64Bit
    """The ID of the entity that this inventory item is assigned to."""
    inventoryitemable_id: Int64Bit
    """The type of entity that this inventory item is assigned to."""
    inventoryitemable_type: InventoryitemableType
    """A decimal latitude."""
    latitude: Latitude
    """A decimal longitude."""
    longitude: Longitude
    """The metadata."""
    metadata: String
    """
    The overall status of an `InventoryItem` (the worse of ICMP/SNMP status).
    """
    overall_status: InventoryItemDeviceStatus
    """The overridden status of an `InventoryItem`."""
    override_status: InventoryItemDeviceStatus
    """The timestamp of when the override status last changed."""
    override_status_last_change: Datetime
    """The ID of the parent `InventoryItem`."""
    parent_inventory_item_id: Int64Bit
    """The status of the device, as read from Preseem."""
    preseem_status: PreseemStatus
    """The ID of a purchase order item"""
    purchase_order_item_id: Int64Bit
    """The purchase price of this item."""
    purchase_price: Int
    """The quantity of this inventory model."""
    quantity: Int
    """The ID of the `InventoryItem` that this segment is a child of."""
    segment_parent_id: Int64Bit
    """The current SNMP monitoring status of an `InventoryItem`."""
    snmp_device_status: InventoryItemDeviceStatus
    """The number of times the SNMP status has flapped."""
    snmp_status_flap_count: Int
    """The timestamp of when the SNMP status last changed."""
    snmp_status_last_change: Datetime
    """The SNMP monitoring status message."""
    snmp_status_message: String
    """The physical status of this item."""
    status: InventoryItemStatus
    """The unit of measurement price for this inventory item."""
    um_price: Int
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): InventoryItemConnection!
  """A geographical address."""
  addresses(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Address status ID."""
    address_status_id: Int64Bit
    """The ID of the entity that owns this address."""
    addressable_id: Int64Bit
    """The type of entity that owns this address."""
    addressable_type: AddressableType
    """The address ID for the Anchor address"""
    anchor_address_id: Int64Bit
    """The attainable download speed in kilobits per second."""
    attainable_download_speed: Int
    """The attainable upload speed in kilobits per second."""
    attainable_upload_speed: Int
    """Avalara PCode."""
    avalara_pcode: String
    """The ID of a BillingDefault."""
    billing_default_id: Int64Bit
    """The year used for calculating fips and census tract information."""
    census_year: Int
    """A city."""
    city: String
    """A two character country code."""
    country: Country
    """A US county. Only used for US addresses."""
    county: UsCounty
    """
    Only used in the USA, this is the census tract information used for calculating things like FCC Form 477.
    """
    fips: String
    """Identifies the source used to obtain the FIPS code"""
    fips_source: FipsSource
    """Whether or not this address is an anchor"""
    is_anchor: Boolean
    """A decimal latitude."""
    latitude: Latitude
    """Address line 1."""
    line1: String
    """Address line 2."""
    line2: String
    """A decimal longitude."""
    longitude: Longitude
    """
    Whether or not the address is serviceable, and can be used for new accounts.
    """
    serviceable: Boolean
    """A state, province, or other country subdivision."""
    subdivision: Subdivision
    """The timezone you want times in the system displayed in."""
    timezone: Timezone
    """The type."""
    type: AddressType
    """A ZIP or postal code."""
    zip: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AddressConnection!
  """An IP address assignment."""
  ip_assignments(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """A human readable description."""
    description: String
    """The ID of an `IpPool`."""
    ip_pool_id: Int64Bit
    """The ID of the owner of this `IpAssignment`."""
    ipassignmentable_id: Int64Bit
    """The owner of this `IpAssignment`."""
    ipassignmentable_type: IpassignmentableType
    """Some reference data regarding this IP assignment."""
    reference: Text
    """
    If this IP was assigned automatically (e.g. via DHCP or RADIUS) then it will be marked as a soft assignment.
    """
    soft: Boolean
    """An IPv4/IPv6 subnet."""
    subnet: SubnetScalar
    """The ID of a `Subnet`."""
    subnet_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): IpAssignmentConnection!
  """A historical record of an IP assignment."""
  ip_assignment_histories(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The date and time of assignment."""
    assigned_datetime: Datetime
    """A human readable description."""
    description: String
    """The ID of an `IpAssignment`."""
    ip_assignment_id: Int64Bit
    """The ID of the owner of this `IpAssignment`."""
    ipassignmentable_id: Int64Bit
    """The owner of this `IpAssignment`."""
    ipassignmentable_type: IpassignmentableType
    """The ID of the entity that the IP address was assigned to."""
    ipassignmenthistoryable_id: Int64Bit
    """
    The parent entity that the IP address was assigned to (e.g. `Account`, `NetworkSite`.)
    """
    ipassignmenthistoryable_type: IpassignmenthistoryableType
    """Some reference data regarding this IP assignment."""
    reference: Text
    """The date and time of removal."""
    removed_datetime: Datetime
    """
    If this IP was assigned automatically (e.g. via DHCP or RADIUS) then it will be marked as a soft assignment.
    """
    soft: Boolean
    """An IPv4/IPv6 subnet."""
    subnet: SubnetScalar
    """
    Some unique identifier that was related to the IP (e.g. a MAC address, IMSI, RADIUS username.)
    """
    unique_identifier: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): IpAssignmentHistoryConnection!
  """A generic inventory item."""
  generic_inventory_items(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The type of entity that owns this generic `InventoryItem`."""
    genericinventoryitemable_id: Int64Bit
    """The ID of the entity that owns this generic `InventoryItem`."""
    genericinventoryitemable_type: InventoryitemableType
    """The ID of an `InventoryModel`."""
    inventory_model_id: Int64Bit
    """The quantity for this service."""
    quantity: Int
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): GenericInventoryItemConnection!
  """A log of an action taken against a set of generic inventory items."""
  generic_inventory_item_action_logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The action that was performed."""
    action: GenericInventoryItemActionLogAction
    """The ID of the entity that this `GenericInventoryItemActionLog` is for."""
    genericinventoryitemactionloggable_id: Int64Bit
    """The type of entity that this `GenericInventoryItemActionLog` is for."""
    genericinventoryitemactionloggable_type: InventoryitemableType
    """The ID of an `InventoryModel`."""
    inventory_model_id: Int64Bit
    """The purchase price of this item."""
    purchase_price: Float
    """The quantity for this service."""
    quantity: Int
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): GenericInventoryItemActionLogConnection!
  """An email."""
  emails(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The body."""
    body: Text
    """An email address."""
    email_address: EmailAddress
    """The ID of the entity that this email was sent to."""
    emailable_id: Int64Bit
    """The type of entity that this email was sent to."""
    emailable_type: EmailableType
    """If rejected, the reason for rejection."""
    reject_reason: String
    """The status."""
    status: EmailStatus
    """The subject."""
    subject: String
    """The name of the recipient."""
    to_name: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): EmailConnection!
  """A note."""
  notes(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The message."""
    message: Text
    """The ID of the entity that owns this note."""
    noteable_id: Int64Bit
    """The type of entity that owns this note."""
    noteable_type: NoteableType
    """The priority of this item."""
    priority: NotePriority
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NoteConnection!
  """Data entered into a `CustomField`."""
  custom_field_data(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The ID of a CustomField that is associated with this type of entity."""
    custom_field_id: Int64Bit
    """The ID of the entity that owns this custom field data."""
    customfielddataable_id: Int64Bit
    """The type of entity that owns this custom field data."""
    customfielddataable_type: CustomfielddataableType
    """The value."""
    value: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): CustomFieldDataConnection!
  """A file."""
  files(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """A human readable description."""
    description: String
    """The file size, in bytes."""
    file_size_in_bytes: Int64Bit
    """The ID of the entity that owns this file."""
    fileable_id: Int64Bit
    """The type of entity that owns this file."""
    fileable_type: FileableType
    """The file name."""
    filename: String
    """The MIME type of the file."""
    mime_type: String
    """
    An image file may be set to the primary image. This will be used as the
    displayed image for the object that this file is associated to throughout Sonar.
    """
    primary_image: Boolean
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): FileConnection!
  """A task."""
  tasks(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The ID of the entity that completes or completed this task."""
    completable_id: Int64Bit
    """The type of entity that completes this task."""
    completable_type: CompletableType
    """Whether or not this is complete."""
    complete: Boolean
    """The date and time this was completed."""
    completed_at: Datetime
    """The `User` that completed this."""
    completed_by_user_id: Int64Bit
    """How this task gets marked as completed."""
    completion_type: TaskCompletionType
    """The date on which the task is due."""
    due: Date
    """The order this item is shown in a list."""
    list_order: Int
    """The task to be performed."""
    task: Text
    """The ID of the entity that the task is associated with."""
    taskable_id: Int64Bit
    """The entity that the task is associated with."""
    taskable_type: TaskableType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): TaskConnection!
  """A log entry."""
  logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Current data."""
    current: Text
    """
    Whether or not this log was transferred from a Sonar v1 instance. If so, the
    formatting will not match current version logs.
    """
    legacy: Boolean
    """
    A title which is only populated on logs that were imported from Sonar v1.
    """
    legacy_title: String
    """The severity level."""
    level: LogLevel
    """The ID of the entity that this log is attached to."""
    loggable_id: Int64Bit
    """The type of entity that this log is attached to."""
    loggable_type: String
    """The entity ID that triggered the log."""
    logged_entity_id: Int64Bit
    """The entity that triggered the log."""
    logged_entity_type: String
    """The message."""
    message: Text
    """Previous data."""
    previous: Text
    """Data from objects related to this change."""
    relation_data: Text
    """The type."""
    type: LogType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): LogConnection!
  """An access log history on an entity."""
  access_logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The date and time that this entity was accessed."""
    access_datetime: Datetime
    """The ID of the entity that this access log belongs to."""
    accessloggable_id: Int64Bit
    """The entity that this access log belongs to."""
    accessloggable_type: String
    """The ID of the entity that this access log belongs to."""
    entity_id: Int64Bit
    """The entity that this access log belongs to."""
    entity_name: String
    """The ID of the user that accessed this entity."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AccessLogConnection!
  """An alerting rotation."""
  alerting_rotations(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Whether to include all account equipment in this rotation."""
    all_accounts: Boolean
    """Whether to include all inventory models in this rotation."""
    all_inventory_models: Boolean
    """Whether to include all network site equipment in this rotation."""
    all_network_sites: Boolean
    """
    The number of minutes a device can be in a down state before generating alert.
    """
    down_time_in_minutes_before_alerting: Int
    """
    The number of minutes a device can remain in a down state before sending a repeat alert.
    """
    down_time_in_minutes_before_repeat: Int
    """Whether or not this is enabled."""
    enabled: Boolean
    """Whether this repeats forever or not."""
    infinite_repetitions: Boolean
    """A descriptive name."""
    name: String
    """The number of times this repeats."""
    repetitions: Int
    """The start."""
    start: Date
    """
    The number of minutes a device can be in a warning state before generating alert.
    """
    warning_time_in_minutes_before_alerting: Int
    """
    The number of minutes a device can remain in a warning state before sending a repeat alert.
    """
    warning_time_in_minutes_before_repeat: Int
    """The number of weeks between repetitions."""
    weeks_between_repetitions: Int
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AlertingRotationConnection!
  """Tickets that are linked to this item."""
  linked_tickets(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """
    The last date and time this entity was updated, or was the subject of a log.
    """
    global_updated_at: Datetime
    """The time this was closed at."""
    closed_at: Datetime
    """The ID of the `User` that closed this."""
    closed_by_user_id: Int64Bit
    """The ID of the company that this entity operates under."""
    company_id: Int64Bit
    """A human readable description."""
    description: Text
    """The date this invoice is due by."""
    due_date: Date
    """The ID of an `InboundMailbox`."""
    inbound_mailbox_id: Int64Bit
    """Indicates if this ticket is marked as spam."""
    is_spam: Boolean
    """The ID of the `Ticket` that this `Ticket` is a child of."""
    parent_ticket_id: Int64Bit
    """The priority of this item."""
    priority: TicketPriority
    """Mail processor's spam rating for whether or not this is spam."""
    spam_score: Float
    """The status."""
    status: TicketStatus
    """The subject."""
    subject: String
    """The ID of a `TicketGroup`."""
    ticket_group_id: Int64Bit
    """The ID of the entity that this `Ticket` is associated with."""
    ticketable_id: Int64Bit
    """The type of entity that this `Ticket` is associated with."""
    ticketable_type: TicketableType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): TicketConnection!
  """Map Overlay."""
  map_overlays(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Map Overlay Language (KML) file contents."""
    contents: String
    """file type"""
    file_type: MapOverlayFileType
    """A decimal latitude."""
    latitude: Latitude
    """A decimal longitude."""
    longitude: Longitude
    """A descriptive name."""
    name: String
    """Network site id."""
    network_site_id: Int64Bit
    """Radius in KM."""
    radius: Float
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): MapOverlayConnection!
  """FiberMap plan."""
  fibermap_plans(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Build"""
    build: String
    """A two character country code."""
    country: String
    """Drop"""
    drop: String
    """FiberMap integration ID"""
    fibermap_integration_id: Int64Bit
    """FiberMap plan ID"""
    fibermap_plan_id: Int64Bit
    """Fibermap project ID."""
    fibermap_project_id: Int64Bit
    """Fibermap project name."""
    fibermap_project_name: String
    """FiberMap updated at"""
    fibermap_updated_at: Datetime
    """Height in meters."""
    height_in_meters: Int
    """is_visible of the information"""
    is_visible: Boolean
    """A decimal latitude."""
    latitude: Latitude
    """A decimal longitude."""
    longitude: Longitude
    """The ID of a map overlay."""
    map_overlay_id: Int64Bit
    """Mapped at"""
    mapped_at: Datetime
    """Mapping user"""
    mapping_user: String
    """A descriptive name."""
    name: String
    """Network site id."""
    network_site_id: Int64Bit
    """A state, province, or other country subdivision."""
    subdivision: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): FibermapPlanConnection!
}

"""The connection wrapper around the `NetworkSiteConnection` type."""
type NetworkSiteConnection {
  """A list of the entities provided by this connection."""
  entities: [NetworkSite]!
  """
  An object providing information about the page of results being displayed, as
  well as the total amount of pages/records available.
  """
  page_info: PageInfo!
  """
  Provides the ability to return aggregated mathematical data about your results.
  """
  aggregations: [Aggregation]!
}

"""Network site serviceable address list."""
type NetworkSiteServiceableAddressList implements NoteableInterface & LoggableInterface & AccessloggableInterface {
  """The ID of the entity."""
  id: Int64Bit!
  """
  An ID that uniquely identifies this entity across the whole Sonar system.
  """
  sonar_unique_id: ID!
  """The date and time this entity was created."""
  created_at: Datetime!
  """The last date and time this entity was modified."""
  updated_at: Datetime!
  """
  A string that shows the version of this entity. It will be incremented whenever the entity is modified.
  """
  _version: String!
  """Network site id."""
  network_site_id: Int64Bit!
  """A network site."""
  network_site(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """A geo-point."""
    geopoint: Geopoint
    """Height in meters."""
    height_in_meters: Float
    """A descriptive name."""
    name: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NetworkSite
  """A geographical address."""
  addresses(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Address status ID."""
    address_status_id: Int64Bit
    """The ID of the entity that owns this address."""
    addressable_id: Int64Bit
    """The type of entity that owns this address."""
    addressable_type: AddressableType
    """The address ID for the Anchor address"""
    anchor_address_id: Int64Bit
    """The attainable download speed in kilobits per second."""
    attainable_download_speed: Int
    """The attainable upload speed in kilobits per second."""
    attainable_upload_speed: Int
    """Avalara PCode."""
    avalara_pcode: String
    """The ID of a BillingDefault."""
    billing_default_id: Int64Bit
    """The year used for calculating fips and census tract information."""
    census_year: Int
    """A city."""
    city: String
    """A two character country code."""
    country: Country
    """A US county. Only used for US addresses."""
    county: UsCounty
    """
    Only used in the USA, this is the census tract information used for calculating things like FCC Form 477.
    """
    fips: String
    """Identifies the source used to obtain the FIPS code"""
    fips_source: FipsSource
    """Whether or not this address is an anchor"""
    is_anchor: Boolean
    """A decimal latitude."""
    latitude: Latitude
    """Address line 1."""
    line1: String
    """Address line 2."""
    line2: String
    """A decimal longitude."""
    longitude: Longitude
    """
    Whether or not the address is serviceable, and can be used for new accounts.
    """
    serviceable: Boolean
    """A state, province, or other country subdivision."""
    subdivision: Subdivision
    """The timezone you want times in the system displayed in."""
    timezone: Timezone
    """The type."""
    type: AddressType
    """A ZIP or postal code."""
    zip: String
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AddressConnection!
  """A note."""
  notes(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The message."""
    message: Text
    """The ID of the entity that owns this note."""
    noteable_id: Int64Bit
    """The type of entity that owns this note."""
    noteable_type: NoteableType
    """The priority of this item."""
    priority: NotePriority
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): NoteConnection!
  """A log entry."""
  logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """Current data."""
    current: Text
    """
    Whether or not this log was transferred from a Sonar v1 instance. If so, the
    formatting will not match current version logs.
    """
    legacy: Boolean
    """
    A title which is only populated on logs that were imported from Sonar v1.
    """
    legacy_title: String
    """The severity level."""
    level: LogLevel
    """The ID of the entity that this log is attached to."""
    loggable_id: Int64Bit
    """The type of entity that this log is attached to."""
    loggable_type: String
    """The entity ID that triggered the log."""
    logged_entity_id: Int64Bit
    """The entity that triggered the log."""
    logged_entity_type: String
    """The message."""
    message: Text
    """Previous data."""
    previous: Text
    """Data from objects related to this change."""
    relation_data: Text
    """The type."""
    type: LogType
    """The ID of a User."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): LogConnection!
  """An access log history on an entity."""
  access_logs(
    """The ID of the entity."""
    id: Int64Bit
    """
    An ID that uniquely identifies this entity across the whole Sonar system.
    """
    sonar_unique_id: ID
    """The date and time this entity was created."""
    created_at: Datetime
    """The last date and time this entity was modified."""
    updated_at: Datetime
    """
    A string that shows the version of this entity. It will be incremented whenever the entity is modified.
    """
    _version: String
    """The date and time that this entity was accessed."""
    access_datetime: Datetime
    """The ID of the entity that this access log belongs to."""
    accessloggable_id: Int64Bit
    """The entity that this access log belongs to."""
    accessloggable_type: String
    """The ID of the entity that this access log belongs to."""
    entity_id: Int64Bit
    """The entity that this access log belongs to."""
    entity_name: String
    """The ID of the user that accessed this entity."""
    user_id: Int64Bit
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """
    Provides the ability to return aggregated mathematical data about your results.
    """
    aggregation: [Aggregator]
    """
    Reverse relation filters allow you to filter the result of a relation, and
    use that filter to affect the returned root elements.
    """
    reverse_relation_filters: [ReverseRelationFilter]
  ): AccessLogConnection!
}

"""
The connection wrapper around the `NetworkSiteServiceableAddressListConnection` type.
"""
type NetworkSiteServiceableAddressListConnection {
  """A list of the entities provided by this connection."""
  entities: [NetworkSiteServiceableAddressList]!
  """
  An object providing information about the page of results being displayed, as
  well as the total amount of pages/records available.
  """
  page_info: PageInfo!
  """
  Provides the ability to return aggregated mathematical data about your results.
  """
  aggregations: [Aggregation]!
}
```
