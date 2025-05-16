```graphql
"""
The input object that defines the fields for the updatePayment mutation.
"""
input UpdatePaymentMutationInput {
  """A descriptive name."""
  reference: String
  """Setting this value to `true` will set `reference` to null."""
  unset_reference: Boolean
}
```
