```graphql
"""
The input object that defines the fields for the createLocalPrefix mutation.
"""
input CreateLocalPrefixMutationInput {
  """The ID of the `VoiceServiceDetail`."""
  voice_service_detail_id: Int64Bit!
  """A telephone number prefix."""
  prefix: Numeric!
  """A note about this entity."""
  note: NoteMutationInput
}
```
