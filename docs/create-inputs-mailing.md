```graphql
"""
The input object that defines the fields for the createMailingAddress mutation.
"""
input CreateMailingAddressMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """Address line 1."""
  line1: String!
  """Address line 2."""
  line2: String
  """A city."""
  city: String!
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String!
  """A two character country code."""
  country: Country!
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
