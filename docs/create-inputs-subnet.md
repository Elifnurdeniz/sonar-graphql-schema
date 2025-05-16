```graphql
"""
The input object that defines the fields for the createSubnet mutation.
"""
input CreateSubnetMutationInput {
  """A descriptive name."""
  name: String
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar!
  """Subnet type."""
  type: SubnetType!
  """The ID of a `Poller`."""
  poller_id: Int64Bit
  """Polling priority."""
  polling_priority: Int = 5
  """A list of `InlineDevice` IDs."""
  inline_device_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
