```graphql
"""
The input object that defines the fields for the createNetflowAllowedSubnet mutation.
"""
input CreateNetflowAllowedSubnetMutationInput {
  """The ID of a `NetflowEndpoint`."""
  netflow_endpoint_id: Int64Bit!
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createNetflowEndpoint mutation.
"""
input CreateNetflowEndpointMutationInput {
  """A descriptive name."""
  name: String!
  """Whitelist mode."""
  whitelist_mode: Boolean!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createNetflowOnPremise mutation.
"""
input CreateNetflowOnPremiseMutationInput {
  """A descriptive name."""
  name: String!
  """An IPv4/IPv6 address."""
  ip: IP!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createNetflowWhitelist mutation.
"""
input CreateNetflowWhitelistMutationInput {
  """The ID of a `NetflowEndpoint`."""
  netflow_endpoint_id: Int64Bit!
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar!
  """A note about this entity."""
  note: NoteMutationInput
}
```
