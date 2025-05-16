```graphql
"""The fields necessary to configure a subnet for a poller."""
input PollerSubnetMutationInput {
  """The ID of a `Subnet`."""
  subnet_id: Int64Bit!
  """Polling priority."""
  polling_priority: Int = 5
}
```
