```graphql
"""
The input object that defines the fields for the createSignature mutation.
"""
input CreateSignatureMutationInput {
  """A descriptive name."""
  name: String!
  """The ID of a department."""
  department_id: Int64Bit!
  """Whether or not signature is default for mass messages."""
  mass_default: Boolean! = false
  """Whether or not signature is default for triggered messages."""
  triggered_default: Boolean! = false
  """Body of an SMS signature."""
  sms_signature: SmsContactPrefix
  """A note about this entity."""
  note: NoteMutationInput
}
```
