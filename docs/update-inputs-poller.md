```graphql
"""
The input object that defines the fields for the updatePoller mutation.
"""
input UpdatePollerMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """Poller subnet configuration."""
  poller_subnets: [PollerSubnetMutationInput]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updatePollerSettings mutation.
"""
input UpdatePollerSettingsMutationInput {
  """How often to poll account equipment (minutes)."""
  account_polling_frequency_in_minutes: Int
  """How often to poll infrastructure equipment (minutes)."""
  infrastructure_polling_frequency_in_minutes: Int
  """A note about this entity."""
  note: NoteMutationInput
}
```
