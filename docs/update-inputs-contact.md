```graphql
"""
The input object that defines the fields for the updateContact mutation.
"""
input UpdateContactMutationInput {
  """A descriptive name."""
  name: String
  """The role of the contact, e.g. "CEO" or "Network Engineer"."""
  role: String
  """An email address."""
  email_address: EmailAddress
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  message_category_ids: [Int64Bit]
  """
  A list of MessageCategory IDs to apply to this contact. If this property is
  excluded, then the contact will inherit the default message categories, which
  is the typical behavior. You should only include this property if you want to
  override the default behavior.
  """
  email_category_ids: [Int64Bit]
  """Make this the new primary contact."""
  become_primary: Boolean
  """A supported language."""
  language: Language
  """A username, used for authentication."""
  username: String
  """A password."""
  password: String
  """Whether or not marketing messages accepted."""
  marketing_opt_in: Boolean
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `email_address` to null."""
  unset_email_address: Boolean
  """Setting this value to `true` will set `role` to null."""
  unset_role: Boolean
  """Setting this value to `true` will set `username` to null."""
  unset_username: Boolean
}
```
