```graphql
"""
The input object that defines the fields for the updateCreditCard mutation.
"""
input UpdateCreditCardMutationInput {
  """The name on the credit card."""
  name_on_card: String
  """The month the credit card expires."""
  expiration_month: Int
  """The year the credit card expires."""
  expiration_year: Int
  """Whether or not this payment method is enabled for automatic payments."""
  auto: Boolean
  """The billing address for the payment method."""
  address: CreateAddressMutationInput
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateCreditCardProcessor mutation.
"""
input UpdateCreditCardProcessorMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """Whether or not this is the primary type of entity."""
  primary: Boolean
  """
  A list of credentials for the provider. Check the enum
  `CreditCardProviderCredential` - all values that begin with the same string as
  the `CreditCardProvider` entered in the `provider` field must be included.
  """
  credit_card_processor_credentials: [CreditCardProcessorCredentialInput]
  """Enable VISA Electron transactions."""
  visaelectron: Boolean
  """Enable Maestro transactions."""
  maestro: Boolean
  """Enable Forbrugsforeningen transactions."""
  forbrugsforeningen: Boolean
  """Enable Dankort transactions."""
  dankort: Boolean
  """Enable VISA transactions."""
  visa: Boolean = true
  """Enable Mastercard transactions."""
  mastercard: Boolean
  """Enable American Express transactions."""
  amex: Boolean
  """Enable Diners Club transactions."""
  dinersclub: Boolean
  """Enable Discover transactions."""
  discover: Boolean
  """Enable UnionPay transactions."""
  unionpay: Boolean
  """Enable JCB transactions."""
  jcb: Boolean
  """
  Enables processor specific `Mail Or Telephone Order` functionality. Currently only applicable for `Stripe`.
  """
  moto_enabled: Boolean
  """IDs of `Companies`."""
  company_ids: [Int64Bit]
}
```
