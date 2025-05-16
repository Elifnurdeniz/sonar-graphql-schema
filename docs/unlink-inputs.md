```graphql
"""
The input object that defines the fields for the unlinkEntityFromTicket mutation.
"""
input UnlinkEntityFromTicketMutationInput {
  """The entity type to unlink."""
  linked_entityable_type: TicketLinkableEntityType!
  """The entity ID to unlink."""
  linked_entityable_id: Int64Bit!
}
```
