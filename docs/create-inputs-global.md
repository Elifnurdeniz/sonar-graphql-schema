```graphql
"""
The input object that defines the fields for the createGlobalInventoryModelMinMax mutation.
"""
input CreateGlobalInventoryModelMinMaxMutationInput {
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """Minimum value"""
  minimum: Int!
  """Minimum value"""
  maximum: Int
  """A note about this entity."""
  note: NoteMutationInput
}
```
