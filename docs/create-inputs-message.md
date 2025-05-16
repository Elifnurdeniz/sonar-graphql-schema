```graphql
"""
The input object that defines the fields for the createMessageCategory mutation.
"""
input CreateMessageCategoryMutationInput {
  """A descriptive name."""
  name: String!
  """
  If this is `true`, then any contacts created will have this category associated with them by default.
  """
  default: Boolean!
  """If `true`, this category will be added to all existing contacts."""
  apply_to_existing_contacts: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}
```
