```graphql
"""
The input object that defines the fields for the updateAddressList mutation.
"""
input UpdateAddressListMutationInput {
  """A descriptive name."""
  name: String
  """
  The types of account statuses for accounts that are part of this grouping.
  """
  account_status: AddressListAccountStatus
  """The delinquency state for accounts that are part of this grouping."""
  delinquency: AddressListDelinquency
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """IDs of `AccountStatus`es."""
  account_status_ids: [Int64Bit]
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """IDs of data `Service`s."""
  data_service_ids: [Int64Bit]
  """A list of IDs of `UsageBasedBillingPolicy` objects."""
  usage_based_billing_policy_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateAddressStatus mutation.
"""
input UpdateAddressStatusMutationInput {
  """A descriptive name."""
  name: String
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor
  """An icon."""
  icon: Icon
  """A note about this entity."""
  note: NoteMutationInput
}
```
