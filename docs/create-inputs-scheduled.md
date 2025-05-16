```graphql
"""
The input object that defines the fields for the createScheduledEvent mutation.
"""
input CreateScheduledEventMutationInput {
  """A human readable description."""
  description: String
  """A date and time"""
  datetime: Datetime!
  """The event for this scheduled event."""
  event: ScheduledEventEvent!
  """The ID of an object described by the `event` field."""
  primary_event_object_id: String
  """
  The amount to be used for this scheduled event. Only applicable for events
  that relate to money (e.g. price override, payment.)
  """
  amount: Int
  """Whether or not to prorate the transaction."""
  prorate: Boolean
  """The ID of an Account."""
  account_id: Int64Bit!
  """
  Items specific to a voice service. Includes the quantity, price override, and related configuration parameter of each.
  """
  account_voice_service_details: [AccountVoiceServiceDetailMutationInput]
  """Items specific to Calix provisioning on associated service."""
  account_calix_service_details: [AccountCalixServiceDetailMutationInput]
}
```
