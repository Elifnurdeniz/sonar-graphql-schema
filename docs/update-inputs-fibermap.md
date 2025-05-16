```graphql
"""
The input object that defines the fields for the updateFibermapIntegration mutation.
"""
input UpdateFibermapIntegrationMutationInput {
  """A descriptive name."""
  name: String
  """An API token."""
  api_token: String
  """Import serviceable addresses"""
  import_serviceable_addresses: Boolean
  """Import plans and contacts"""
  import_accounts_and_contacts: Boolean
  """Always create new network sites"""
  always_create_new_network_sites: Boolean
  """Allow serviceability status to be read from map features"""
  read_serviceability_from_features: Boolean
  """Update service locations in Vetro Fibermap"""
  update_service_locations: Boolean
  """Whether or not this is enabled."""
  enabled: Boolean
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The ID of an AccountStatus."""
  account_status_id: Int64Bit
  """The ID of an AccountType."""
  account_type_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateFibermapPlan mutation.
"""
input UpdateFibermapPlanMutationInput {
  """is_visible of the information"""
  is_visible: Boolean
  """Network site id."""
  unset_network_site_id: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateFibermapServiceLocation mutation.
"""
input UpdateFibermapServiceLocationMutationInput {
  """is_visible of the information"""
  is_visible: Boolean
  """The ID of the address."""
  unset_address_id: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}
```
