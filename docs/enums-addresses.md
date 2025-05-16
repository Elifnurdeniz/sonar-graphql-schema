```graphql
"""
The status for each of the linked addresses created during the createLinkedAddresses mutation.
"""
enum LinkedAddressesStatus {
  """Linked address created"""
  CREATED
  """Serviceable address exists"""
  EXISTS
  """Address already linked to anchor"""
  ANCHORED
}
```
