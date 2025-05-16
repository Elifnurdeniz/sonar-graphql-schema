```graphql
"""Calix provisioning values for the associated service."""
input AccountCalixServiceDetailMutationInput {
  """Calix Inegartion ID."""
  calix_integration_id: Int64Bit!
  """VLAN."""
  vlan: String
  """C-VLAN."""
  cvlan: Int64Bit
  """Global VLAN."""
  global_vlan: String
  """Policy Map."""
  policy_map: String
  """ONT Port ID."""
  ont_port_id: String
  """Custom JSON."""
  custom_json: String
  """Use Custom JSON."""
  use_custom_json: Boolean
}

"""Metadata values for the metadata fields on the associated service."""
input AccountServiceMetadataMutationInput {
  """The ID of a ServiceMetadata field."""
  service_metadata_id: Int64Bit!
  """The contents of a service metadata field."""
  value: String!
}

"""Metadata values for the metadata fields on the associated service."""
input AccountVoiceServiceDetailMutationInput {
  """The ID of a voice service configuration parameter."""
  voice_service_generic_parameter_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int!
  """
  The amount that this service price has been overridden to. If this is null, then the service price is used.
  """
  price_override: Int
  """The reason that the price of a service has been overridden."""
  price_override_reason: String
}
```
