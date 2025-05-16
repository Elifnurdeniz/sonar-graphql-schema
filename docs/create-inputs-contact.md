```graphql
"""
The input object that defines the fields for the createContact mutation.
"""
input CreateContactMutationInput {
  """The type of entity that owns this contact."""
  contactable_type: ContactableType!
  """The ID of the entity that owns this contact."""
  contactable_id: Int64Bit!
  """A descriptive name."""
  name: String!
  """The role of the contact, e.g. "CEO" or "Network Engineer"."""
  role: String
  """An email address."""
  email_address: EmailAddress
  """Phone numbers."""
  phone_numbers: [CreatePhoneNumberMutationInput]
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
  marketing_opt_in: Boolean = false
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
}

"""The input object that defines the fields for the  mutation."""
input CreateContactPhoneNumberMutationInput {
  """The ID of the contact that owns this."""
  contact_id: Int64Bit!
  """The number."""
  number: Numeric!
  """The extension."""
  extension: Numeric
  """A two character country code for this phone number."""
  country: Country!
  """The ID of the PhoneNumberType associated with this phone number."""
  phone_number_type_id: Int64Bit!
  """Whether or not SMS messages accepted."""
  sms_opt_in: Boolean = false
}
```
