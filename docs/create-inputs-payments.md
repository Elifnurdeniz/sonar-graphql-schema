```graphql
"""
The input object that defines the fields for the createPayments mutation.
"""
input CreatePaymentsMutationInput {
  """A payment."""
  payments: [CreatePaymentMutationInput]!
}
```
