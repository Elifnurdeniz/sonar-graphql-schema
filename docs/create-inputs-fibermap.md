```graphql
"""
The input object that defines the fields for the createFibermapIntegration mutation.
"""
input CreateFibermapIntegrationMutationInput {
  """A descriptive name."""
  name: String!
  """An API token."""
  api_token: String!
  """Import serviceable addresses"""
  import_serviceable_addresses: Boolean!
  """Import plans and contacts"""
  import_accounts_and_contacts: Boolean!
  """Always create new network sites"""
  always_create_new_network_sites: Boolean!
  """Allow serviceability status to be read from map features"""
  read_serviceability_from_features: Boolean = false
  """Update service locations in Vetro Fibermap"""
  update_service_locations: Boolean
  """Whether or not this is enabled."""
  enabled: Boolean!
  """Whether or not this is enabled."""
  company_id: Int64Bit
  """Whether or not this is enabled."""
  account_status_id: Int64Bit
  """Whether or not this is enabled."""
  account_type_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
