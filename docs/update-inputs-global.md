```graphql
"""
The input object that defines the fields for the updateGlobalInventoryModelMinMax mutation.
"""
input UpdateGlobalInventoryModelMinMaxMutationInput {
  """Minimum value"""
  minimum: Int!
  """Maximum value"""
  maximum: Int
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `maximum` to null."""
  unset_maximum: Boolean
}
```
