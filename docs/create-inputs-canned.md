```graphql
"""
The input object that defines the fields for the createCannedReplyCategory mutation.
"""
input CreateCannedReplyCategoryMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createCannedReply mutation.
"""
input CreateCannedReplyMutationInput {
  """A descriptive name."""
  name: String!
  """The body."""
  body: Text!
  """The ID of a `CannedReplyCategory`."""
  canned_reply_category_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}
```
