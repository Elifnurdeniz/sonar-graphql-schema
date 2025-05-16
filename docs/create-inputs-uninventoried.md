```graphql
"""
The input object that defines the fields for the createUninventoriedMacAddress mutation.
"""
input CreateUninventoriedMacAddressMutationInput {
  """A MAC address."""
  mac_address: MacAddress!
  """The ID of an Account."""
  account_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}
```
