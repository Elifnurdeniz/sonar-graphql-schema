```graphql
"""
The input object that defines the fields for the createInlineDevice mutation.
"""
input CreateInlineDeviceMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean! = true
  """An IPv4/IPv6 address."""
  ip_address: IP!
  """A TCP port."""
  port: Port
  """The type of inline device."""
  type: InlineDeviceType!
  """Whether this device should write entries for all subnets or not."""
  all_subnets: Boolean!
  """Credentials for an inline device."""
  inline_device_credentials: [InlineDeviceAuthenticationCredentialMutationInput]!
  """IDs of `Subnet`s."""
  subnet_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
