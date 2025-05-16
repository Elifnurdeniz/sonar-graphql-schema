```graphql
"""
The input object that defines the fields for the createInternalLocation mutation.
"""
input CreateInternalLocationMutationInput {
  """A descriptive name."""
  name: String!
  """The ID of an `InventoryLocation`."""
  inventory_location_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createInternalTicket mutation.
"""
input CreateInternalTicketMutationInput {
  """The subject."""
  subject: String!
  """A human readable description."""
  description: Text!
  """The status."""
  status: TicketStatus!
  """The priority of a `Ticket`."""
  priority: TicketPriority!
  """The date this invoice is due by."""
  due_date: Date
  """The type of entity that this `Ticket` is associated with."""
  ticketable_type: TicketableType
  """The ID of the entity that this `Ticket` is associated with."""
  ticketable_id: Int64Bit
  """The ID of the `Ticket` that this `Ticket` is a child of."""
  parent_ticket_id: Int64Bit
  """The ID of a `TicketGroup`."""
  ticket_group_id: Int64Bit
  """The ID of a User."""
  user_id: Int64Bit
  """IDs of `TicketCategory`s."""
  ticket_category_ids: [Int64Bit]
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
  """Allows subscribing to notifications for this entity."""
  subscription: SubscriptionMutationInput
}
```
