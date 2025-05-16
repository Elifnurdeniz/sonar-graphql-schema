```graphql
"""
The input object that defines the fields for the updateDidAssignment mutation.
"""
input UpdateDidAssignmentMutationInput {
  """The ID of a Service."""
  service_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `service_id` to null."""
  unset_service_id: Boolean
}

"""The input object that defines the fields for the updateDid mutation."""
input UpdateDidMutationInput {
  """The ID of a `VoiceProvider`."""
  voice_provider_id: Int64Bit
  """The ID of a `RateCenter`."""
  rate_center_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
