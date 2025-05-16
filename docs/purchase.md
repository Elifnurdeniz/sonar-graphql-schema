```graphql
"""A purchase order for items from a third party vendor."""
type PurchaseOrder implements EmailableInterface & NoteableInterface & NotifiableInterface & FileableInterface & LoggableInterface & AccessloggableInterface {
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
  """The ID of the user that approved this purchase order."""
  approved_by_user_id: Int64Bit
  """The date/time that this purchase order was cancelled."""
  canceled_at: Datetime
  """The ID of the user that cancelled this purchase order."""
  canceled_by_user_id: Int64Bit
  """
  The ID of the company that will be used in the header of this purchase order.
  """
  company_id: Int64Bit!
  """The ID of the user that created this purchase order."""
  created_by_user_id: Int64Bit!
  """The currency the system displays money in."""
  currency: Currency
  """A message to be included on purchase orders when sent to vendors."""
  external_message: String
  """The source of the shipping address for a purchase order."""
  inventory_location_id: Int64Bit!
  """Whether or not the purchase order has been marked as being paid."""
  is_paid: Boolean
  """The date and time that the inventory item status last changed."""
  last_status_change: Datetime!
  """The ID of an order group related to this purchase order."""
  order_group_id: Int64Bit
  """A unique number identifying an approved purchase order."""
  order_number: Int
  """The terms of payment for deliveries from this vendor."""
  payment_terms: PaymentTerm
  """The current status of this purchase order."""
  status: PurchaseOrderStatus!
  """The ID of a vendor."""
  vendor_id: Int64Bit!
  """The name of a vendor."""
  vendor_name: String
  """The ID of the user that canceled this purchase order."""
  canceled_by_user(
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
  """The ID of the user that created this entity."""
  created_by_user(
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
  """The ID of the user that approved this purchase order."""
  approved_by_user(
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
  """A third party vendor of inventory models."""
  vendor(
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
    Archived vendors may not be used for creating new Purchase Orders or Product Requests.
    """
    archived: Boolean
    """
    Determines if approved purchase orders for this vendor should automatically dispatch an email to the vendor.
    """
    automate_approved_purchase_orders: Boolean
    """The currency used for all transactions with this vendor."""
    currency: Currency
    """A descriptive name."""
    name: String
    """The terms of payment for deliveries from this vendor."""
    payment_terms: PaymentTerm
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
  ): Vendor
  """A location that inventory is stored in."""
  inventory_location(
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
    Marks this inventory location as the default shipping location for purchase orders.
    """
    default_shipping_location: Boolean
    """A geo-point."""
    geopoint: Geopoint
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
  ): InventoryLocation
  """A company you do business as."""
  company(
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
    The daily end time of the period during which billing communication e.g. new
    invoices, delinquency, etc. will not be sent.
    """
    billing_communication_delay_end_local_time: Time
    """
    The daily start time of the period during which billing communication e.g.
    new invoices, delinquency, etc. will not be sent.
    """
    billing_communication_delay_start_local_time: Time
    """On an enabled remittance slip, who should checks be made payable to?"""
    checks_payable_to: String
    """A two character country code."""
    country: Country
    """The URL to your customer portal."""
    customer_portal_url: URL
    """Whether or not this entity is a default entry."""
    default: Boolean
    """Whether or not this is enabled."""
    enabled: Boolean
    """The ISP type of this `Company`."""
    isp_type: IspType
    """A descriptive name."""
    name: String
    """A telephone number."""
    phone_number: Numeric
    """The primary color to use in Sonar."""
    primary_color: HtmlHexColor
    """The secondary color to use in Sonar."""
    secondary_color: HtmlHexColor
    """Whether or not to include a detachable remittance slip on the invoice."""
    show_remittance_slip: Boolean
    """
    A tax identification number. Should only be entered if you are required to
    share some type of tax identification information with your customers.
    """
    tax_identification: String
    """The address of the company website."""
    website_address: URL
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
  ): Company
  """An order group."""
  order_group(
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
    The threshold at which requesters require approval of their purchase orders.
    """
    automatic_approval_threshold: Int
    """
    Disabled order groups cannot be assigned users or used to create purchase orders.
    """
    enabled: Boolean
    """The name of an order group."""
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
  ): OrderGroup
  """A line item on a purchase order."""
  purchase_order_items(
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
    The tax transaction that was created for this purchase order item the last time it was modified.
    """
    calculated_tax: Int
    """
    The quantity of a generic purchase order item that has already been received.
    """
    generic_quantity_received: Int
    """The order this item is shown in a list."""
    list_order: Int
    """A descriptive name."""
    name: String
    """Part number used by the vendor to identify this vendor item."""
    part_number: String
    """
    The price of the vendor item at the time the purchase order was created.
    """
    price: Int64Bit
    """The ID of a purchase order."""
    purchase_order_id: Int64Bit
    """
    Number of inventory models that are included in a single unit of this vendors product.
    """
    quantity_per_unit: Int
    """The current status of a purchase order item."""
    status: PurchaseOrderItemStatus
    """The quantity of a vendor item on a purchase order."""
    units: Int
    """The ID of a vendor item."""
    vendor_item_id: Int64Bit
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
  ): PurchaseOrderItemConnection!
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
  """A `Notification`."""
  notifications(
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
    """Whether this notification is read or unread."""
    is_read: Boolean
    """The ID of the entity that the notification is related to."""
    notifiable_id: Int64Bit
    """The type of entity that the notification is related to."""
    notifiable_type: NotifiableType
    """The type."""
    type: NotificationType
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
  ): NotificationConnection!
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

"""The connection wrapper around the `PurchaseOrderConnection` type."""
type PurchaseOrderConnection {
  """A list of the entities provided by this connection."""
  entities: [PurchaseOrder]!
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

"""A line item on a purchase order."""
type PurchaseOrderItem implements NoteableInterface & CustomfielddataableInterface & LoggableInterface & AccessloggableInterface {
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
  """
  The tax transaction that was created for this purchase order item the last time it was modified.
  """
  calculated_tax: Int
  """
  The quantity of a generic purchase order item that has already been received.
  """
  generic_quantity_received: Int!
  """The order this item is shown in a list."""
  list_order: Int
  """A descriptive name."""
  name: String
  """Part number used by the vendor to identify this vendor item."""
  part_number: String
  """
  The price of the vendor item at the time the purchase order was created.
  """
  price: Int64Bit!
  """The ID of a purchase order."""
  purchase_order_id: Int64Bit!
  """
  Number of inventory models that are included in a single unit of this vendors product.
  """
  quantity_per_unit: Int
  """The current status of a purchase order item."""
  status: PurchaseOrderItemStatus!
  """The quantity of a vendor item on a purchase order."""
  units: Int!
  """The ID of a vendor item."""
  vendor_item_id: Int64Bit!
  """A purchase order for items from a third party vendor."""
  purchase_order(
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
    """The ID of the user that approved this purchase order."""
    approved_by_user_id: Int64Bit
    """The date/time that this purchase order was cancelled."""
    canceled_at: Datetime
    """The ID of the user that cancelled this purchase order."""
    canceled_by_user_id: Int64Bit
    """
    The ID of the company that will be used in the header of this purchase order.
    """
    company_id: Int64Bit
    """The ID of the user that created this purchase order."""
    created_by_user_id: Int64Bit
    """The currency the system displays money in."""
    currency: Currency
    """A message to be included on purchase orders when sent to vendors."""
    external_message: String
    """The source of the shipping address for a purchase order."""
    inventory_location_id: Int64Bit
    """Whether or not the purchase order has been marked as being paid."""
    is_paid: Boolean
    """The date and time that the inventory item status last changed."""
    last_status_change: Datetime
    """The ID of an order group related to this purchase order."""
    order_group_id: Int64Bit
    """A unique number identifying an approved purchase order."""
    order_number: Int
    """The terms of payment for deliveries from this vendor."""
    payment_terms: PaymentTerm
    """The current status of this purchase order."""
    status: PurchaseOrderStatus
    """The ID of a vendor."""
    vendor_id: Int64Bit
    """The name of a vendor."""
    vendor_name: String
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
  ): PurchaseOrder
  """An item that can be purchased from a particular vendor."""
  vendor_item(
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
    Archived vendor items may not be used for creating new purchase orders or product requests.
    """
    archived: Boolean
    """A descriptive name."""
    name: String
    """Part number used by the vendor to identify this vendor item."""
    part_number: String
    """The purchase price of this item from the vendor."""
    price: Int
    """
    Number of inventory models that are included in a single unit of this vendors product.
    """
    quantity_per_unit: Int
    """
    Flag for vendor items that should create a one-time service for retail sale to customers.
    """
    retail_item: Boolean
    """The price of the one-time service created for this vendor item"""
    retail_item_price: Int
    """
    The ID of the one-time service created when this vendor item was created.
    """
    retail_item_service_id: Int64Bit
    """The ID of the vendor that sells this item"""
    vendor_id: Int64Bit
    """The ID of the entity that is referred to by this vendor item."""
    vendoritemable_id: Int64Bit
    """The type of entity that is referred to by this vendor item."""
    vendoritemable_type: VendoritemableType
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
  ): VendorItem
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
  """A tax."""
  taxes(
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
    Whether this `Tax` is applied as a percentage of the `Service` charge, or as a flat rate.
    """
    application: TaxApplication
    """A descriptive name."""
    name: String
    """
    The rate for a tax. For a percentage based tax, this is a percentage. For a
    flat tax, it is a currency value in the smallest currency unit (e.g. cents, pence, pesos.)
    """
    rate: Float
    """
    Whether this tax is applied based on the account being in a specific
    geography, or whether it is applied to all accounts.
    """
    type: TaxType
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
  ): TaxConnection!
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

"""The connection wrapper around the `PurchaseOrderItemConnection` type."""
type PurchaseOrderItemConnection {
  """A list of the entities provided by this connection."""
  entities: [PurchaseOrderItem]!
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
