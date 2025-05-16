```graphql
"""
The input object that defines the fields for the createAchBatch mutation.
"""
input CreateAchBatchMutationInput {
  """The batch ID that gets inserted into the ACH file on generation."""
  ach_sequence: Int64Bit!
  """Whether the receiving bank requires an offset record."""
  offset_record: Boolean!
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
