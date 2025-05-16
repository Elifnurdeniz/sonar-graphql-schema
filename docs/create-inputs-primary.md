```graphql
"""The input object that defines the fields for the Contact mutation."""
input CreatePrimaryContactMutationInput {
  """A descriptive name."""
  name: String!
  """The role of the contact, e.g. "CEO" or "Network Engineer"."""
  role: String
  """An email address."""
  email_address: EmailAddress
  """Phone numbers."""
  phone_numbers: [CreatePhoneNumberMutationInput]
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
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
  """Whether or not marketing messages accepted."""
  marketing_opt_in: Boolean = false
}
```
