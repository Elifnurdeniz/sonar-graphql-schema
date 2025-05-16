```graphql
"""Metadata values for the metadata fields on the associated service."""
input OneTimeTransactionAccountVoiceServiceDetailMutationInput {
  """The ID of a voice service configuration parameter."""
  voice_service_generic_parameter_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int!
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  price_override: Int
}
```
