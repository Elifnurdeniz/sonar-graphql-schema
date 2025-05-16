```graphql
"""
The input object that defines the fields for the updateApplicationFirewallRule mutation.
"""
input UpdateApplicationFirewallRuleMutationInput {
  """An IPv4/IPv6 subnet."""
  subnet: SubnetScalar
  """A human readable description."""
  description: String
  """A note about this entity."""
  note: NoteMutationInput
}
```
