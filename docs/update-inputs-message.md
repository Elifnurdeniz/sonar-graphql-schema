```graphql
"""
The input object that defines the fields for the updateMessageCategory mutation.
"""
input UpdateMessageCategoryMutationInput {
  """A descriptive name."""
  name: String
  """
  If this is `true`, then any contacts created will have this category associated with them by default.
  """
  default: Boolean
  """If `true`, this category will be added to all existing contacts."""
  apply_to_existing_contacts: Boolean
  """
  If `true`, this category will be removed from all existing contacts. Ignored if apply_to_existing_contacts is `true`
  """
  remove_from_existing_contacts: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}
```
