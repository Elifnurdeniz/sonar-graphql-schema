```graphql
"""An SMS message."""
type SmsMessage implements NoteableInterface & LoggableInterface & AccessloggableInterface {
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
  """Whether or not SMS message is used for triggers."""
  is_trigger: Boolean!
  """A descriptive name."""
  name: String!
  """An SMS message content."""
  sms_message_contents(
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
    """A supported language."""
    language: Language
    """SMS message body for customers without portal."""
    non_portal_body: String
    """SMS message body for customers with portal."""
    portal_body: String
    """The ID of the SMS message."""
    sms_message_id: Int64Bit
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
  ): SmsMessageContentConnection!
  """A message that is sent when a specific event occurs."""
  triggered_messages(
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
    """Whether or not child accounts are allowed."""
    allow_children: Boolean
    """
    The count associated with this `TriggeredMessage`. This is defined by the
    trigger, and could be something like a number of days, months, gigabytes, etc.
    """
    count: Int
    """The ID of an EmailMessage."""
    email_message_id: Int64Bit
    """Whether or not this is enabled."""
    enabled: Boolean
    """The ID of a `JobType`."""
    job_type_id: Int64Bit
    """A descriptive name."""
    name: String
    """If an item is protected, it cannot be modified or deleted."""
    protected: Boolean
    """The ID of a signature."""
    signature_id: Int64Bit
    """The ID of the SMS message."""
    sms_message_id: Int64Bit
    """The trigger for this message."""
    trigger: MessageTrigger
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
  ): TriggeredMessageConnection!
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

"""The connection wrapper around the `SmsMessageConnection` type."""
type SmsMessageConnection {
  """A list of the entities provided by this connection."""
  entities: [SmsMessage]!
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

"""An SMS message content."""
type SmsMessageContent implements NoteableInterface & LoggableInterface & AccessloggableInterface {
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
  """A supported language."""
  language: Language!
  """SMS message body for customers without portal."""
  non_portal_body: String!
  """SMS message body for customers with portal."""
  portal_body: String!
  """The ID of the SMS message."""
  sms_message_id: Int64Bit!
  """An SMS message."""
  sms_message(
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
    """Whether or not SMS message is used for triggers."""
    is_trigger: Boolean
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
  ): SmsMessage
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

"""The connection wrapper around the `SmsMessageContentConnection` type."""
type SmsMessageContentConnection {
  """A list of the entities provided by this connection."""
  entities: [SmsMessageContent]!
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

"""An SMS outbound message."""
type SmsOutboundMessage implements LoggableInterface & AccessloggableInterface {
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
  """The category of the message."""
  category: SmsOutboundCategory!
  """
  The cost associated with the SMS message. Stored as one hundredth of the
  smallest currency value (e.g. cents, pence, pesos.)
  """
  cost_in_hundredths: Int!
  """The country code of the destination mobile phone number."""
  destination_country: String
  """The error message."""
  error_message: String!
  """The provider message ID."""
  last_status_check: Datetime
  """The message text."""
  message_text: String!
  """The destination mobile phone number."""
  mobile_number: String!
  """The provider message ID."""
  provider_message_id: String
  """The number of segments needed to deliver message text."""
  segments: Int!
  """The ID of the entity that this SMS was sent to."""
  smsable_id: Int64Bit!
  """The type of entity that this SMS was sent to."""
  smsable_type: SmsableType!
  """The current status of the message."""
  status: SmsOutboundStatus!
  """An SMS message."""
  smsable(
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
    """Provides the ability to paginate through results."""
    paginator: Paginator
    """Provides the ability to sort results."""
    sorter: [Sorter]
    """Complex search parameters."""
    search: [Search]
    """Search across all string fields with partial matching."""
    general_search: String
    """Whether or not to include archived entities in the results."""
    include_archived: Boolean
  ): SmsableInterface
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

"""The connection wrapper around the `SmsOutboundMessageConnection` type."""
type SmsOutboundMessageConnection {
  """A list of the entities provided by this connection."""
  entities: [SmsOutboundMessage]!
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

"""SMS configuration settings."""
type SmsSetting implements NoteableInterface & LoggableInterface & AccessloggableInterface {
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
  """Whether the SMS funds are paid for automatically."""
  auto_pay: Boolean!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """A notification is sent if SMS funds fall below this value."""
  low_funds_threshold: Int!
  """End of quiet time for sending SMS triggered messages."""
  triggered_quiet_end_time: Time
  """Start of quiet time for sending SMS triggered messages."""
  triggered_quiet_start_time: Time
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
```
