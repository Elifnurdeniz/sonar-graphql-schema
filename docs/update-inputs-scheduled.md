```graphql
"""
The fields necessary to update an account voice service detail on a scheduled event.
"""
input UpdateScheduledEventAccountVoiceServiceDetailMutationInput {
  """The ID of a voice service configuration parameter."""
  voice_service_generic_parameter_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  price_override: Int
  """The reason that the price of a service has been overridden."""
  price_override_reason: String
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  unset_price_override: Boolean
  """The reason that the price of a service has been overridden."""
  unset_price_override_reason: Boolean
}

"""
The input object that defines the fields for the updateScheduledEvent mutation.
"""
input UpdateScheduledEventMutationInput {
  """A human readable description."""
  description: String
  """A date and time"""
  datetime: Datetime
  """The ID of an object described by the `event` field."""
  primary_event_object_id: String
  """
  The amount to be used for this scheduled event. Only applicable for events
  that relate to money (e.g. price override, payment.)
  """
  amount: Int
  """Whether or not to prorate the transaction."""
  prorate: Boolean
  """
  Items specific to a voice service. Includes the quantity, price override, and related configuration parameter of each.
  """
  account_voice_service_details: [UpdateScheduledEventAccountVoiceServiceDetailMutationInput]
  """Items specific to Calix provisioning on associated service."""
  account_calix_service_details: [AccountCalixServiceDetailMutationInput]
  """Setting this value to `true` will set `prorate` to null."""
  unset_prorate: Boolean
}
```
