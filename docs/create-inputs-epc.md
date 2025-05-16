```graphql
"""The input object that defines the fields for the createEpc mutation."""
input CreateEpcMutationInput {
  """A descriptive name."""
  name: String!
  """The identifier used by the EPC, this is typically numeric."""
  identifier: String!
  """IDs of `IpPool`s."""
  ip_pool_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
