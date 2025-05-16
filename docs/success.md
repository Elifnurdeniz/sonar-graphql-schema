```graphql
"""
Returned when the result of a mutation is only true or false, and there is no
other data to return. The `message` property can sometimes contain a description
of the failure, if `success` is false.
"""
type SuccessResponse {
  """Will be true if the operation succeeded."""
  success: Boolean!
  """The message."""
  message: Text
}

"""
Returned when the result of a mutation is not consistent. The `message` property
can sometimes contain a description of the failure, if `success` is false. The
id may contain the model created if `success` is true.
"""
type SuccessResponseWithId {
  """Will be true if the operation succeeded."""
  success: Boolean!
  """The message."""
  message: Text
  """The ID of the entity."""
  id: Int64Bit
}
```
