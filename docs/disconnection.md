```graphql
"""The `Account` disconnections log."""
type DisconnectionLog implements NoteableInterface & LoggableInterface & AccessloggableInterface {
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
  """The ID of an Account."""
  account_id: Int64Bit!
  """The date and time that the account was disconnected."""
  disconnected_at: Datetime!
  """The `User` that disconnected the `Account`."""
  disconnected_by_user_id: Int64Bit!
  """The ID of the serviceable address to use for this account."""
  serviceable_address_id: Int64Bit
  """
  The deleted address object, as a formatted single line, that was disconnected.
  Used for historical reporting when address is deleted.
  """
  serviceable_address_reference_record: Text
  """A customer account."""
  account(
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
    """The ID of an AccountStatus."""
    account_status_id: Int64Bit
    """The ID of an AccountType."""
    account_type_id: Int64Bit
    """The date an account was first activated."""
    activation_date: Date
    """The time an account was first activated."""
    activation_time: Time
    """The date and time this entity was archived."""
    archived_at: Datetime
    """The ID of the `User` that archived this entity."""
    archived_by_user_id: Int64Bit
    """The ID of the company that this entity operates under."""
    company_id: Int64Bit
    """
    The percentage of the data usage cap that this account has consumed this
    month, taking into account any data usage top offs.
    """
    data_usage_percentage: Int
    """A geo-point."""
    geopoint: Geopoint
    """Whether or not this account is delinquent."""
    is_delinquent: Boolean
    """
    Whether or not the Account meets the eligibility criteria for archiving.
    """
    is_eligible_for_archive: Boolean
    """A descriptive name."""
    name: String
    """
    The next date this service will bill. If this is null, it will bill on the next account billing date.
    """
    next_bill_date: Date
    """
    The next recurring charge amount for an account. This is the sum of data,
    expiring, recurring, and voice services of an account for this billing
    cycle, including tax.
    """
    next_recurring_charge_amount: Int
    """The ID of the `Account` that is this `Account`s master."""
    parent_account_id: Int64Bit
    """Whether or not to include archived entities in the results."""
    include_archived: Boolean
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
  ): Account
  """The user that disconnected this `Account`."""
  disconnected_by_user(
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
    """Whether or not the user has completed the setup process."""
    completed_setup: Boolean
    """An email address."""
    email_address: EmailAddress
    """Whether or not this is enabled."""
    enabled: Boolean
    """Whether or not this user is a Sonar employee."""
    is_sonar_staff: Boolean
    """A supported language."""
    language: Language
    """A mobile phone number. This will be used to send SMS messages."""
    mobile_number: Numeric
    """A descriptive name."""
    name: String
    """The publicly viewable name of this user."""
    public_name: String
    """The ID of a Role."""
    role_id: Int64Bit
    """
    Super admins receive all system permissions automatically, regardless of their role.
    """
    super_admin: Boolean
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
  ): User
  """The serviceable address."""
  serviceable_address(
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
  ): Address
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

"""The connection wrapper around the `DisconnectionLogConnection` type."""
type DisconnectionLogConnection {
  """A list of the entities provided by this connection."""
  entities: [DisconnectionLog]!
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
