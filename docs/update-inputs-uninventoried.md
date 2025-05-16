```graphql
"""
The input object that defines the fields for the updateUninventoriedMacAddress mutation.
"""
input UpdateUninventoriedMacAddressMutationInput {
  """A MAC address."""
  mac_address: MacAddress!
  """A note about this entity."""
  note: NoteMutationInput
}
```
