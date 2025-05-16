```graphql
"""
The input object that defines the fields for the updateLocalPrefix mutation.
"""
input UpdateLocalPrefixMutationInput {
  """A telephone number prefix."""
  prefix: Numeric!
  """A note about this entity."""
  note: NoteMutationInput
}
```
