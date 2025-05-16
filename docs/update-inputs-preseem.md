```graphql
"""
The input object that defines the fields for the updatePreseem mutation.
"""
input UpdatePreseemMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """An API key."""
  api_key: Text
  """A note about this entity."""
  note: NoteMutationInput
}
```
