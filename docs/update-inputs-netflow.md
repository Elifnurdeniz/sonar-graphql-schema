```graphql
"""
The input object that defines the fields for the updateNetflowAllowedSubnet mutation.
"""
input UpdateNetflowAllowedSubnetMutationInput {
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateNetflowEndpoint mutation.
"""
input UpdateNetflowEndpointMutationInput {
  """A descriptive name."""
  name: String
  """Whitelist mode."""
  whitelist_mode: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateNetflowOnPremise mutation.
"""
input UpdateNetflowOnPremiseMutationInput {
  """A descriptive name."""
  name: String
  """An IPv4/IPv6 address."""
  ip: IP
  """The date and time of the last processed records."""
  last_processed_timestamp: Datetime
  """The file name of the last processed records."""
  last_processed_filename: String
  """The size of the last processed records file."""
  last_processed_size: Int
  """A JSON object of tracked statistics."""
  statistics: Text
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `last_processed_timestamp` to null.
  """
  unset_last_processed_timestamp: Boolean
  """
  Setting this value to `true` will set `last_processed_filename` to null.
  """
  unset_last_processed_filename: Boolean
  """Setting this value to `true` will set `last_processed_size` to null."""
  unset_last_processed_size: Boolean
}

"""
The input object that defines the fields for the updateNetflowWhitelist mutation.
"""
input UpdateNetflowWhitelistMutationInput {
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar
  """A note about this entity."""
  note: NoteMutationInput
}
```
