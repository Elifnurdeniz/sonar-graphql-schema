```graphql
"""
The input object that defines the fields for the createBankAccount mutation.
"""
input CreateBankAccountMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The name on the account."""
  name_on_account: String!
  """The type of bank account this is."""
  bank_account_type: BankAccountType!
  """The bank account number."""
  account_number: Numeric!
  """The bank routing number."""
  routing_number: Numeric!
  """Whether or not this payment method is enabled for automatic payments."""
  auto: Boolean!
  """The billing address for the payment method."""
  address: CreateAddressMutationInput!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createBankAccountPayment mutation.
"""
input CreateBankAccountPaymentMutationInput {
  """The ID of a BankAccount."""
  bank_account_id: Int64Bit!
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
The input object that defines the fields for the createBankAccountProcessor mutation.
"""
input CreateBankAccountProcessorMutationInput {
  """The provider to use when transacting against bank accounts."""
  provider: BankAccountProvider!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """
  Whether or not this is the primary provider to use when transacting against newly added bank accounts.
  """
  primary: Boolean!
  """
  The credentials to use to authenticate against the bank account provider.
  """
  bank_account_processor_credentials: [BankAccountProcessorCredentialInput]!
  """IDs of `Companies`."""
  company_ids: [Int64Bit]
}
```
