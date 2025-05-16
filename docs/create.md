```graphql
"""
The linked address details for each item processed in createLinkedAddresses mutation.
"""
type CreateLinkedAddresses {
  """The ID of the serviceable address to use for this account."""
  serviceable_address_id: Int64Bit
  """The name of the serviceable address to use for this account."""
  serviceable_address_name: String
  """The status of each specific linked address during bulk creation."""
  status: LinkedAddressesStatus
  """The ID of an Account."""
  account_id: Int64Bit
}

"""The results from the createLinkedAddresses mutation."""
type CreateLinkedAddressesResponse {
  """The total number of address(es) in the range provided."""
  addresses_total: Int64Bit
  """The number of address(es) created in the range provided."""
  addresses_created: Int64Bit
  """
  The list of address(es) processed in the range provided and details on each.
  """
  linked_addresses: [CreateLinkedAddresses]
}
```
