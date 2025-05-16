```graphql
"""
The input object that defines the fields for the createCreditCard mutation.
"""
input CreateCreditCardMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
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
  """Whether or not this payment method is enabled for automatic payments."""
  auto: Boolean!
  """The billing address for the payment method."""
  address: CreateAddressMutationInput!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createCreditCardPayment mutation.
"""
input CreateCreditCardPaymentMutationInput {
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

"""
The input object that defines the fields for the createCreditCardProcessor mutation.
"""
input CreateCreditCardProcessorMutationInput {
  """The company that provides credit card processing services."""
  provider: CreditCardProvider!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """Whether or not this is the primary type of entity."""
  primary: Boolean!
  """
  A list of credentials for the provider. Check the enum
  `CreditCardProviderCredential` - all values that begin with the same string as
  the `CreditCardProvider` entered in the `provider` field must be included.
  """
  credit_card_processor_credentials: [CreditCardProcessorCredentialInput]!
  """Enable VISA Electron transactions."""
  visaelectron: Boolean = true
  """Enable Maestro transactions."""
  maestro: Boolean = true
  """Enable Forbrugsforeningen transactions."""
  forbrugsforeningen: Boolean = true
  """Enable Dankort transactions."""
  dankort: Boolean = true
  """Enable VISA transactions."""
  visa: Boolean = true
  """Enable Mastercard transactions."""
  mastercard: Boolean = true
  """Enable American Express transactions."""
  amex: Boolean = true
  """Enable Diners Club transactions."""
  dinersclub: Boolean = true
  """Enable Discover transactions."""
  discover: Boolean = true
  """Enable UnionPay transactions."""
  unionpay: Boolean = true
  """Enable JCB transactions."""
  jcb: Boolean = true
  """
  Enables processor specific `Mail Or Telephone Order` functionality. Currently only applicable for `Stripe`.
  """
  moto_enabled: Boolean = false
  """IDs of `Companies`."""
  company_ids: [Int64Bit]
}
```
