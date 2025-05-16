```graphql
"""
The input object that defines the fields for the createPersonalAccessToken mutation.
"""
input CreatePersonalAccessTokenMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
}
```
