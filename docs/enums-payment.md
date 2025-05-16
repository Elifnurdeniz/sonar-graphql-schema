```graphql
"""The type of payment made by the `CreditCard`."""
enum CardPaymentType {
  """NONE"""
  NONE
  """CREDIT"""
  CREDIT
  """DEBIT"""
  DEBIT
  """CHARGE"""
  CHARGE
  """PREPAID"""
  PREPAID
  """DEBIT_CREDIT"""
  DEBIT_CREDIT
}

"""
A type of `Payment` that can only be made without using a payment method (like a credit card, or bank account.)
"""
enum NonPaymentMethodPaymentType {
  """Cash"""
  CASH
  """Wire"""
  WIRE
  """Check"""
  CHECK
  """Other"""
  OTHER
  """PayPal"""
  PAYPAL
}
```
