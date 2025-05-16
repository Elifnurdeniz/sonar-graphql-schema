```graphql
"""
The input object that defines the fields for the updateCalendarIcal mutation.
"""
input UpdateCalendarIcalMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """Setting this value to `true` will set `name` to null."""
  unset_name: Boolean
}

"""
The input object that defines the fields for the updateCalendarSystemSettings mutation.
"""
input UpdateCalendarSystemSettingsMutationInput {
  """If enabled allow external calendar integrations to sync."""
  calendar_allow_external_sync: Boolean
  """
  Number of months to sync calendar history, 0-3 allowed.  Future will always sync.
  """
  calendar_history_sync_maximum: Int
}
```
