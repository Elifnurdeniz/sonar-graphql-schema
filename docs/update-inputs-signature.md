```graphql
"""
The input object that defines the fields for the updateSignature mutation.
"""
input UpdateSignatureMutationInput {
  """A descriptive name."""
  name: String
  """The ID of a department."""
  department_id: Int64Bit
  """Whether or not signature is default for mass messages."""
  mass_default: Boolean
  """Whether or not signature is default for triggered messages."""
  triggered_default: Boolean
  """Body of an SMS signature."""
  sms_signature: SmsContactPrefix
  """A note about this entity."""
  note: NoteMutationInput
}
```
