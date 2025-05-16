```graphql
"""The input object that defines the fields for the  mutation."""
input CreatePhoneNumberMutationInput {
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

"""
The input object that defines the fields for the createPhoneNumberType mutation.
"""
input CreatePhoneNumberTypeMutationInput {
  """A descriptive name."""
  name: String!
  """
  Whether or not phone numbers of this type are capable of sending and receiving SMS messages.
  """
  sms_capable: Boolean!
}
```
