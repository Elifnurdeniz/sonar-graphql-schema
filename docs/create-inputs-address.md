```graphql
"""
The input object that defines the fields for the createAddressList mutation.
"""
input CreateAddressListMutationInput {
  """A descriptive name."""
  name: String!
  """
  The types of account statuses for accounts that are part of this grouping.
  """
  account_status: AddressListAccountStatus!
  """The delinquency state for accounts that are part of this grouping."""
  delinquency: AddressListDelinquency!
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

"""The fields necessary to create an address."""
input CreateAddressMutationInput {
  """Address line 1."""
  line1: String!
  """Address line 2."""
  line2: String
  """A city."""
  city: String!
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String!
  """A two character country code."""
  country: Country!
  """Address status ID."""
  address_status_id: Int64Bit
}

"""
The input object that defines the fields for the createAddressStatus mutation.
"""
input CreateAddressStatusMutationInput {
  """A descriptive name."""
  name: String!
  """A 6 character hexadecimal string, representing a color used in HTML."""
  color: HtmlHexColor!
  """An icon."""
  icon: Icon!
  """A note about this entity."""
  note: NoteMutationInput
}
```
