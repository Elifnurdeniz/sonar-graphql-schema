```graphql
"""
The input object that defines the fields for the updateBankAccount mutation.
"""
input UpdateBankAccountMutationInput {
  """The name on the account."""
  name_on_account: String
  """The type of bank account this is."""
  bank_account_type: BankAccountType
  """Whether or not this payment method is enabled for automatic payments."""
  auto: Boolean
  """The billing address for the payment method."""
  address: CreateAddressMutationInput
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateBankAccountProcessor mutation.
"""
input UpdateBankAccountProcessorMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """
  Whether or not this is the primary provider to use when transacting against newly added bank accounts.
  """
  primary: Boolean
  """
  The credentials to use to authenticate against the bank account provider.
  """
  bank_account_processor_credentials: [BankAccountProcessorCredentialInput]
  """IDs of `Companies`."""
  company_ids: [Int64Bit]
}
```
