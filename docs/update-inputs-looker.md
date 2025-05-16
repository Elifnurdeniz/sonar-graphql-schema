```graphql
"""
The input object that defines the fields for the updateLookerExploreLicense mutation.
"""
input UpdateLookerExploreLicenseMutationInput {
  """The ID of a User."""
  user_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `user_id` to null."""
  unset_user_id: Boolean
}

"""
The input object that defines the fields for the updateLookerViewLicense mutation.
"""
input UpdateLookerViewLicenseMutationInput {
  """The ID of a User."""
  user_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `user_id` to null."""
  unset_user_id: Boolean
}
```
