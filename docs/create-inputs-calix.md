```graphql
"""
The input object that defines the fields for the createCalixCloudSetting mutation.
"""
input CreateCalixCloudSettingMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The Auth0 client ID."""
  client_id: String!
  """The Auth0 client secret."""
  client_secret: String!
  """A username, used for authentication."""
  username: String!
  """A password."""
  password: String!
  """The ID of a `CustomField` that will map to Calix subscriber field1."""
  subscriber_field1_id: Int64Bit
  """The ID of a `CustomField` that will map to Calix subscriber field2."""
  subscriber_field2_id: Int64Bit
  """The ID of a `CustomField` that will map to Calix subscriber field3."""
  subscriber_field3_id: Int64Bit
  """The ID of a `CustomField` that will map to Calix subscriber field4."""
  subscriber_field4_id: Int64Bit
  """The ID of a `CustomField` that will map to Calix subscriber field5."""
  subscriber_field5_id: Int64Bit
  """The area type to be used for the region."""
  subscriber_region: CalixSubscriberAreaType
  """The area type to be used for the location."""
  subscriber_location: CalixSubscriberAreaType
  """An array of Calix service group definitions."""
  service_group_tiers: Text
  """
  An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
  """
  integration_field_mappings: [IntegrationFieldMappingInput]!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createCalixIntegration mutation.
"""
input CreateCalixIntegrationMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """Subscriber organization ID to use for integration"""
  org_id: String!
  """
  The URL of the SMx server including the SMx API port, eg. mysmx.org:18443 (SMx uses 18443 as the default API port)
  """
  smx_url: String!
  """The basic auth credentials to use with SMx, username:password"""
  smx_credentials: String!
  """The software version of SMx that will be used in integration"""
  smx_version: CalixIntegrationVersion!
  """An entity which maps a service to a vendor specific service name"""
  integration_service_mappings: [IntegrationServiceMappingInput]
  """
  An entity which maps an inventory model field to a vendor specific integration field type (ie serial number)
  """
  integration_field_mappings: [IntegrationFieldMappingInput]
  """Controls if Sonar should add SMx device alarms to inventory item logs"""
  alarms_create_logs: Boolean!
  """Controls if Sonar updates the ICMP device status from SMx alarms"""
  alarms_change_device_status: Boolean!
  """
  Controls if Sonar updates the inventory item's soft IP address from SMx DHCP lease alarms.
  """
  alarms_update_ip_assignment: Boolean!
  """
  Controls whether to turn on synchronization of Calix ONTs and Subscribers, from Sonar Inventory Items and Accounts.
  """
  enable_ont_synchronization: Boolean!
  """
  Disable, pause, then re-enable Calix ONT ports after creating or removing
  service.  Recommended for deployments using DHCP within SMx.
  """
  bounce_ports: Boolean!
  """
  The Calix service template name to use when a residential account becomes delinquent.
  """
  residential_delinquency_service_template: String
  """
  The Calix service template name to use when a commercial account becomes delinquent.
  """
  commercial_delinquency_service_template: String
  """
  The Calix service template name to use when a government account becomes delinquent.
  """
  government_delinquency_service_template: String
  """
  The Calix policy map name to use when a residential account becomes delinquent.
  """
  residential_delinquency_policy_map: String
  """
  The Calix policy map name to use when a commercial account becomes delinquent.
  """
  commercial_delinquency_policy_map: String
  """
  The Calix policy map name to use when a government account becomes delinquent.
  """
  government_delinquency_policy_map: String
  """
  The Calix service template name to use when an industrial account becomes delinquent.
  """
  industrial_delinquency_service_template: String
  """
  The Calix policy map name to use when an industrial account becomes delinquent.
  """
  industrial_delinquency_policy_map: String
  """
  The Calix service template name to use when a senior citizen account becomes delinquent.
  """
  senior_citizen_delinquency_service_template: String
  """
  The Calix policy map name to use when a senior citizen account becomes delinquent.
  """
  senior_citizen_delinquency_policy_map: String
  """
  Whether or not a default Calix service detail record is created when integration service added.
  """
  create_default_service_detail: Boolean = false
  """A note about this entity."""
  note: NoteMutationInput
}
```
