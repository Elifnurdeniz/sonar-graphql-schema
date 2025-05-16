```graphql
"""
The input object that defines the fields for the updatePhoneNumber mutation.
"""
input UpdatePhoneNumberMutationInput {
  """The number."""
  number: Numeric
  """The extension."""
  extension: Numeric
  """A two character country code for this phone number."""
  country: Country
  """The ID of the PhoneNumberType associated with this phone number."""
  phone_number_type_id: Int64Bit
  """Whether or not SMS messages accepted."""
  sms_opt_in: Boolean
  """Setting this value to `true` will set `extension` to null."""
  unset_extension: Boolean
}

"""
The input object that defines the fields for the updatePhoneNumberType mutation.
"""
input UpdatePhoneNumberTypeMutationInput {
  """A descriptive name."""
  name: String
  """
  Whether or not phone numbers of this type are capable of sending and receiving SMS messages.
  """
  sms_capable: Boolean
}
```
