```graphql
"""
The input object that defines the fields for the refundPayment mutation.
"""
input RefundPaymentMutationInput {
  """The amount to refund."""
  amount: Int!
  """Why this refund was provided."""
  description: String
  """The unique tracking ID for this payment."""
  payment_tracker_id: String
}
```
