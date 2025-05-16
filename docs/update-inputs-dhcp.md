```graphql
"""
The input object that defines the fields for the updateDhcpServerIdentifier mutation.
"""
input UpdateDhcpServerIdentifierMutationInput {
  """A descriptive name."""
  name: String
  """IDs of `IpPool`s."""
  ip_pool_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateDhcpServer mutation.
"""
input UpdateDhcpServerMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean = true
  """An IPv4/IPv6 address."""
  ip_address: IP
  """A TCP port."""
  port: Port
  """Does this `DhcpServer` provide DHCP for all IP pools?"""
  serves_all_pools: Boolean
  """
  If this is `true`, then Sonar will use the MAC address of the DHCP relay
  rather than the MAC address of the requesting device when writing a lease.
  This should generally be disabled unless you have a specific reason to enable it.
  """
  use_source_mac_address: Boolean = false
  """Credentials for the `DhcpServer.`"""
  dhcp_server_credentials: [DhcpServerAuthenticationCredentialMutationInput]
  """IDs of `IpPool`s."""
  ip_pool_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
