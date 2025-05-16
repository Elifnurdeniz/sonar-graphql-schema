```graphql
"""The input object that defines the fields for the voidPayment mutation."""
input VoidPaymentMutationInput {
  """The amount to void."""
  amount: Int!
  """Why this void was performed."""
  description: String
  """The unique tracking ID for this payment."""
  payment_tracker_id: String
}
```
