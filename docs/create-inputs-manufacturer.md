```graphql
"""
The input object that defines the fields for the createManufacturer mutation.
"""
input CreateManufacturerMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
}
```
