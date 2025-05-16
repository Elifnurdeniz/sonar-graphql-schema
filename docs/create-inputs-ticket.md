```graphql
"""
The input object that defines the fields for the createTicketCategory mutation.
"""
input CreateTicketCategoryMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTicketComment mutation.
"""
input CreateTicketCommentMutationInput {
  """The body of the comment."""
  body: Text!
  """The ID of a `Ticket`."""
  ticket_id: Int64Bit!
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}

"""
The input object that defines the fields for the createTicketGroup mutation.
"""
input CreateTicketGroupMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """Whether or not the group is private."""
  private: Boolean!
  """The IDs of `Users` in this `TicketGroup`."""
  user_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTicketRecipient mutation.
"""
input CreateTicketRecipientDuringTicketCreationMutationInput {
  """A descriptive name."""
  name: String!
  """An email address."""
  email_address: EmailAddress!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTicketRecipient mutation.
"""
input CreateTicketRecipientMutationInput {
  """A descriptive name."""
  name: String!
  """An email address."""
  email_address: EmailAddress!
  """The ID of a `Ticket`."""
  ticket_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTicketReply mutation.
"""
input CreateTicketReplyMutationInput {
  """The ID of a `Ticket`."""
  ticket_id: Int64Bit!
  """The body."""
  body: Text!
  """
  Whether or not the reply was incoming (from an external party) or outgoing (from a Sonar `User`.)
  """
  incoming: Boolean = false
  """The author."""
  author: Text
  """The email address of the author."""
  author_email: EmailAddress
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
