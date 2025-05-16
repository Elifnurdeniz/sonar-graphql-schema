```graphql
"""
The input object that defines the fields for the updateIpAssignment mutation.
"""
input UpdateIpAssignmentMutationInput {
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar
  """The owner of this `IpAssignment`."""
  ipassignmentable_type: IpassignmentableType
  """The ID of the owner of this `IpAssignment`."""
  ipassignmentable_id: Int64Bit
  """
  If this IP was assigned automatically (e.g. via DHCP or RADIUS) then it will be marked as a soft assignment.
  """
  soft: Boolean = false
  """Some reference data regarding this IP assignment."""
  reference: Text
  """A human readable description."""
  description: String
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `reference` to null."""
  unset_reference: Boolean
  """Setting this value to `true` will set `description` to null."""
  unset_description: Boolean
}

"""
The input object that defines the fields for the updateIpPool mutation.
"""
input UpdateIpPoolMutationInput {
  """A descriptive name."""
  name: String
  """A range of IPv4 addresses."""
  ip_range: IpRange
  """The ID of a `DhcpServerIdentifier`."""
  dhcp_server_identifier_id: Int64Bit
  """IDs of `EPC`s."""
  epc_ids: [Int64Bit]
  """IDs of `DhcpServer`s."""
  dhcp_server_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `dhcp_server_identifier_id` to null.
  """
  unset_dhcp_server_identifier_id: Boolean
}
```
