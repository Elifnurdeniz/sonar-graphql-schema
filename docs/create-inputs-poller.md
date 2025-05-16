```graphql
"""
The input object that defines the fields for the createPoller mutation.
"""
input CreatePollerMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean
  """Poller subnet configuration."""
  poller_subnets: [PollerSubnetMutationInput]
  """A note about this entity."""
  note: NoteMutationInput
}
```
