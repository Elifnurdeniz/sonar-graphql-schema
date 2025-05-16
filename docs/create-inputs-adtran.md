```graphql
"""
The input object that defines the fields for the createAdtranMosaicSetting mutation.
"""
input CreateAdtranMosaicSettingMutationInput {
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The base API URL."""
  api_url: String!
  """A username, used for authentication."""
  username: String!
  """A password."""
  password: String!
  """Whether or not to run audit after creation."""
  run_audit_after_creation: Boolean!
  """Whether or not to suspend unattached services."""
  auto_suspend_unattached_services: Boolean!
  """Controls if Sonar should add SMx device alarms to inventory item logs"""
  alarms_create_logs: Boolean!
  """Controls if Sonar updates the ICMP device status from SMx alarms"""
  alarms_change_device_status: Boolean!
  """The name of the default Adtran Mosaic content provider."""
  default_uplink_content_provider_name: String!
  """The name of the default Adtran Mosaic uplink inner tag vlan."""
  default_uplink_inner_tag_vlan: String!
  """The name of the default Adtran Mosaic uplink outer tag vlan."""
  default_uplink_outer_tag_vlan: String!
  """The name of the default Adtran Mosaic downlink interface."""
  default_downlink_interface_name: String!
  """The name of the default Adtran Mosaic downlink inner tag vlan."""
  default_downlink_inner_tag_vlan: String!
  """The name of the default Adtran Mosaic downlink outer tag vlan."""
  default_downlink_outer_tag_vlan: String!
  """Whether or not commercial account type suspends."""
  commercial_delinquency_suspends: Boolean!
  """Whether or not government account type suspends."""
  government_delinquency_suspends: Boolean!
  """Whether or not residential account type suspends."""
  residential_delinquency_suspends: Boolean!
  """Whether or not senior citizen account type suspends."""
  senior_citizen_delinquency_suspends: Boolean!
  """Whether or not industrial account type suspends."""
  industrial_delinquency_suspends: Boolean!
  """Commercial account type delinquency profile vector."""
  commercial_delinquency_profile_vector: String
  """Government account type delinquency profile vector."""
  government_delinquency_profile_vector: String
  """Residential account type delinquency profile vector."""
  residential_delinquency_profile_vector: String
  """Senior citizen account type delinquency profile vector."""
  senior_citizen_delinquency_profile_vector: String
  """Industrial account type delinquency profile vector."""
  industrial_delinquency_profile_vector: String
  """Bounce ports enable profile."""
  bounce_ports_enable_profile: String!
  """Bounce ports disable profile."""
  bounce_ports_disable_profile: String!
  """
  An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
  """
  integration_field_mappings: [IntegrationFieldMappingInput]!
  """An entity which maps a service to Adtran Mosaic specific items."""
  integration_service_mappings: [IntegrationServiceMappingAdtranMosaicInput]!
  """A note about this entity."""
  note: NoteMutationInput
}
```
