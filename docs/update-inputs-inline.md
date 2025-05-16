```graphql
"""
The input object that defines the fields for the updateInlineDevice mutation.
"""
input UpdateInlineDeviceMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """An IPv4/IPv6 address."""
  ip_address: IP
  """A TCP port."""
  port: Port
  """Whether this device should write entries for all subnets or not."""
  all_subnets: Boolean
  """Credentials for an inline device."""
  inline_device_credentials: [InlineDeviceAuthenticationCredentialMutationInput]
  """IDs of `Subnet`s."""
  subnet_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
