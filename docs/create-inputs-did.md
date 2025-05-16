```graphql
"""
The input object that defines the fields for the createDidAssignment mutation.
"""
input CreateDidAssignmentMutationInput {
  """The ID of a `Did`."""
  did_id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of a Service."""
  service_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createDidImportFlatfile mutation.
"""
input CreateDidImportFlatfileMutationInput {
  """The ID of a `VoiceProvider`."""
  voice_provider_id: Int64Bit!
  """The ID of a `RateCenter`."""
  rate_center_id: Int64Bit!
  """The identifier of a unique batch at Flatfile."""
  flatfile_batch_identifier: String!
  """A note about this entity."""
  note: NoteMutationInput
}

"""The input object that defines the fields for the createDid mutation."""
input CreateDidMutationInput {
  """The ID of a `VoiceProvider`."""
  voice_provider_id: Int64Bit!
  """The ID of a `RateCenter`."""
  rate_center_id: Int64Bit!
  """The number."""
  number: String!
  """A note about this entity."""
  note: NoteMutationInput
}
```
