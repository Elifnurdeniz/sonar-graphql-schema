```graphql
"""
The input object that defines the fields for the createCallDetailRecordImportFlatfile mutation.
"""
input CreateCallDetailRecordImportFlatfileMutationInput {
  """The ID of a `VoiceProvider`."""
  voice_provider_id: Int64Bit!
  """The identifier of a unique batch at Flatfile."""
  flatfile_batch_identifier: String!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createCallDetailRecord mutation.
"""
input CreateCallDetailRecordMutationInput {
  """The ID of a `VoiceProvider`."""
  voice_provider_id: Int64Bit!
  """The DID that initiated the call."""
  originating_number: String!
  """The DID that received the call."""
  receiving_number: String!
  """When the call was started."""
  started_at: Datetime!
  """The total length of the call in seconds."""
  length_in_seconds: Int!
}

"""
The input object that defines the fields for the createCallLog mutation.
"""
input CreateCallLogMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The subject."""
  subject: String!
  """The body."""
  body: Text!
  """The time in seconds."""
  time_in_seconds: Int!
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
