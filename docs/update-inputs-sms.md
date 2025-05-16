```graphql
"""
The input object that defines the fields for the updateSmsSettings mutation.
"""
input UpdateSmsSettingsMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """A notification is sent if SMS funds fall below this value."""
  low_funds_threshold: Int
  """Start of quiet time for sending SMS triggered messages."""
  triggered_quiet_start_time: Time
  """End of quiet time for sending SMS triggered messages."""
  triggered_quiet_end_time: Time
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `triggered_quiet_start_time` to null.
  """
  unset_triggered_quiet_start_time: Boolean
  """
  Setting this value to `true` will set `triggered_quiet_end_time` to null.
  """
  unset_triggered_quiet_end_time: Boolean
}
```
