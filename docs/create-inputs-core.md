```graphql
"""
The input object that defines the fields for the createCoreCreditCard mutation.
"""
input CreateCoreCreditCardMutationInput {
  """The name on the credit card."""
  name_on_card: String!
  """The credit card number."""
  card_number: Numeric!
  """
  The CVV2 number (also called CVV, CSV, and CID, depending on the card issuer.)
  """
  cvv2: Numeric!
  """The month the credit card expires."""
  expiration_month: Int!
  """The year the credit card expires."""
  expiration_year: Int!
  """The billing address for the payment method."""
  address: CreateAddressMutationInput!
}

"""
The input object that defines the fields for the createCorePayment mutation.
"""
input CreateCorePaymentMutationInput {
  """The ID of a CreditCard."""
  credit_card_id: Int64Bit!
  """The amount of the payment, in the smallest currency value."""
  amount: Int!
  """A description of the payment, used for internal reference."""
  description: String
  """Apply this payment to any open invoices."""
  apply_to_open_invoices: Boolean!
  """The unique tracking ID for this payment."""
  payment_tracker_id: String
  """Email payment receipt to account holder"""
  email_payment_receipt: Boolean
}
```
