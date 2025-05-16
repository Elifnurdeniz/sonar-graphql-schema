```graphql
"""
The input object that defines the fields for the createTokenizedBankAccount mutation.
"""
input CreateTokenizedBankAccountMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of a BankProcessor."""
  bank_account_processor_id: Int64Bit!
  """The profile ID provided by a credit card processing service."""
  customer_profile_id: String
  """The name on the account."""
  name_on_account: String!
  """The type of bank account this is."""
  bank_account_type: BankAccountType!
  """
  The tokenized value that represents a credit card, provided by a credit card processing service.
  """
  token: String!
  """A partial account number that can be used for identification."""
  masked_account_number: String!
  """Whether or not this payment method is enabled for automatic payments."""
  auto: Boolean!
  """The bank routing number."""
  routing_number: Numeric
  """The billing address for the payment method."""
  address: CreateAddressMutationInput
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createTokenizedCreditCard mutation.
"""
input CreateTokenizedCreditCardMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of a CreditCardProcessor."""
  credit_card_processor_id: Int64Bit!
  """The profile ID provided by a credit card processing service."""
  customer_profile_id: String
  """The type of a credit card (e.g. Visa, Mastercard.)"""
  credit_card_type: CreditCardType!
  """The name on the credit card."""
  name_on_card: String!
  """
  The tokenized value that represents a credit card, provided by a credit card processing service.
  """
  token: String!
  """The month the credit card expires."""
  expiration_month: Int!
  """The year the credit card expires."""
  expiration_year: Int!
  """Whether or not this payment method is enabled for automatic payments."""
  auto: Boolean!
  """A partial credit card number that can be used for identification."""
  masked_number: String!
  """The billing address for the payment method."""
  address: CreateAddressMutationInput!
  """A note about this entity."""
  note: NoteMutationInput
}
```
