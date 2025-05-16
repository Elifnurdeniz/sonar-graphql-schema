```graphql
"""
The input object that defines the fields for the updateCallDetailRecord mutation.
"""
input UpdateCallDetailRecordMutationInput {
  """The DID that initiated the call."""
  originating_number: String
  """The DID that received the call."""
  receiving_number: String
  """When the call was started."""
  started_at: Datetime
  """The total length of the call in seconds."""
  length_in_seconds: Int
}

"""
The input object that defines the fields for the updateCallLog mutation.
"""
input UpdateCallLogMutationInput {
  """The subject."""
  subject: String
  """The body."""
  body: Text
  """The time in seconds."""
  time_in_seconds: Int
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
