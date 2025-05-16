```graphql
"""
The input object that defines the fields for the createPayment mutation.
"""
input CreatePaymentMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The amount of the payment, in the smallest currency value."""
  amount: Int!
  """A `Payment` type made without a payment method."""
  payment_type: NonPaymentMethodPaymentType!
  """
  A payment reference like a check number, or wire transfer confirmation number.
  """
  reference: String
  """A description of the payment, used for internal reference."""
  description: String
  """The date and time the payment was made."""
  payment_datetime: Datetime
  """Apply this payment to any open invoices."""
  apply_to_open_invoices: Boolean = false
  """A list of applicable `Invoice` IDs."""
  invoice_ids: [Int64Bit!]
  """The unique tracking ID for this payment."""
  payment_tracker_id: String
  """The transaction ID from the credit card provider."""
  transaction_id: String
  """Email payment receipt to account holder"""
  email_payment_receipt: Boolean
}
```
