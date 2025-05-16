```graphql
"""
The input object that defines the fields for the updateTowercoverageConfiguration mutation.
"""
input UpdateTowercoverageConfigurationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """The alphanumeric 64-character API key for TowerCoverage."""
  api_key: Text
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """The ID of an AccountStatus."""
  account_status_id: Int64Bit
  """The ID of the PhoneNumberType associated with this phone number."""
  phone_number_type_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `api_key` to null."""
  unset_api_key: Boolean
  """Setting this value to `true` will set `account_type_id` to null."""
  unset_account_type_id: Boolean
  """Setting this value to `true` will set `account_status_id` to null."""
  unset_account_status_id: Boolean
  """Setting this value to `true` will set `phone_number_type_id` to null."""
  unset_phone_number_type_id: Boolean
}

"""
The input object that defines the fields for the updateTowercoverageSubmission mutation.
"""
input UpdateTowercoverageSubmissionMutationInput {
  """is_visible of the information"""
  is_visible: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
