```graphql
"""
The input object that defines the fields for the createSupernet mutation.
"""
input CreateSupernetMutationInput {
  """A descriptive name."""
  name: String
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar!
  """A note about this entity."""
  note: NoteMutationInput
}
```
