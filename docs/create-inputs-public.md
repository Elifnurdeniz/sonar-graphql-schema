```graphql
"""
The input object that defines the fields for the createPublicTicket mutation.
"""
input CreatePublicTicketMutationInput {
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
  """The ID of an `InboundMailbox`."""
  inbound_mailbox_id: Int64Bit!
  """Recipients for ticket replies."""
  ticket_recipients: [CreateTicketRecipientDuringTicketCreationMutationInput]
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
