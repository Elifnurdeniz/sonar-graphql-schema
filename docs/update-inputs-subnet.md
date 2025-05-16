```graphql
"""
The input object that defines the fields for the updateSubnet mutation.
"""
input UpdateSubnetMutationInput {
  """A descriptive name."""
  name: String
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar
  """Subnet type."""
  type: SubnetType
  """The ID of a `Poller`."""
  poller_id: Int64Bit
  """Polling priority."""
  polling_priority: Int
  """A list of `InlineDevice` IDs."""
  inline_device_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `name` to null."""
  unset_name: Boolean
  """Setting this value to `true` will set `poller_id` to null."""
  unset_poller_id: Boolean
}
```
