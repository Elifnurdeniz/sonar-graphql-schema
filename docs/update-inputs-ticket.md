```graphql
"""
The input object that defines the fields for the updateTicketCategory mutation.
"""
input UpdateTicketCategoryMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateTicketComment mutation.
"""
input UpdateTicketCommentMutationInput {
  """The body."""
  body: Text
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}

"""
The input object that defines the fields for the updateTicketGroup mutation.
"""
input UpdateTicketGroupMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """Whether or not the group is private."""
  private: Boolean
  """The IDs of `Users` in this `TicketGroup`."""
  user_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateTicket mutation.
"""
input UpdateTicketMutationInput {
  """The subject."""
  subject: String
  """A human readable description."""
  description: Text
  """The status."""
  status: TicketStatus
  """The priority of a `Ticket`."""
  priority: TicketPriority
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
  inbound_mailbox_id: Int64Bit
  """Recipients for ticket replies."""
  ticket_recipients: [CreateTicketRecipientDuringTicketCreationMutationInput]
  """Indicates if this ticket is marked as spam."""
  is_spam: Boolean
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
  """Setting this value to `true` will set `due_date` to null."""
  unset_due_date: Boolean
  """Setting this value to `true` will set `ticketable_type` to null."""
  unset_ticketable_type: Boolean
  """Setting this value to `true` will set `ticketable_id` to null."""
  unset_ticketable_id: Boolean
  """Setting this value to `true` will set `parent_ticket_id` to null."""
  unset_parent_ticket_id: Boolean
  """Setting this value to `true` will set `ticket_group_id` to null."""
  unset_ticket_group_id: Boolean
  """Setting this value to `true` will set `user_id` to null."""
  unset_user_id: Boolean
  """Setting this value to `true` will set `inbound_mailbox_id` to null."""
  unset_inbound_mailbox_id: Boolean
}

"""
The input object that defines the fields for the updateTicketRecipient mutation.
"""
input UpdateTicketRecipientMutationInput {
  """A descriptive name."""
  name: String
  """An email address."""
  email_address: EmailAddress
  """A note about this entity."""
  note: NoteMutationInput
}
```
