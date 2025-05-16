```graphql
"""
The input object that defines the fields for the createDeploymentType mutation.
"""
input CreateDeploymentTypeMutationInput {
  """A descriptive name."""
  name: String!
  """The ID of an `InventoryModel`."""
  inventory_model_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}
```
