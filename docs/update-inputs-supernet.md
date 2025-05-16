```graphql
"""
The input object that defines the fields for the updateSupernet mutation.
"""
input UpdateSupernetMutationInput {
  """A descriptive name."""
  name: String
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `name` to null."""
  unset_name: Boolean
}
```
