```graphql
"""
The input object that defines the fields for the createNetworkMonitoringGraph mutation.
"""
input CreateNetworkMonitoringGraphMutationInput {
  """A descriptive name."""
  name: String!
  """The type."""
  type: NetworkMonitoringGraphType = LINE
  """Stacked"""
  stacked: Boolean = false
  """The ID of a `NetworkMonitoringTemplate`."""
  network_monitoring_template_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createNetworkMonitoringTemplate mutation.
"""
input CreateNetworkMonitoringTemplateMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not to collect interface statistics."""
  collect_interface_statistics: Boolean = false
  """Whether or not ICMP monitoring is enabled."""
  icmp_monitoring: Boolean = false
  """ICMP latency threshold (ms)."""
  icmp_latency_threshold: Int
  """ICMP loss threshold (%)."""
  icmp_loss_threshold: Int
  """SNMP version"""
  snmp_version: SnmpVersion
  """SNMP community/securityName"""
  snmp_community: String
  """SNMPv3 security level"""
  snmp3_sec_level: Snmp3SecurityLevel
  """SNMPv3 auth protocol"""
  snmp3_auth_protocol: Snmp3AuthProtocol
  """SNMPv3 auth passphrase"""
  snmp3_auth_passphrase: String
  """SNMPv3 privacy protocol"""
  snmp3_priv_protocol: Snmp3PrivProtocol
  """SNMPv3 privacy passphrase"""
  snmp3_priv_passphrase: String
  """SNMPv3 context name"""
  snmp3_context_name: String
  """SNMPv3 context engine ID"""
  snmp3_context_engineid: String
  """A note about this entity."""
  note: NoteMutationInput
}

"""Provides address details for a network site."""
input CreateNetworkSiteAddressMutationInput {
  """Address line 1."""
  line1: String
  """Address line 2."""
  line2: String
  """A city."""
  city: String
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String
  """A two character country code."""
  country: Country!
  """A decimal latitude."""
  latitude: Latitude!
  """A decimal longitude."""
  longitude: Longitude!
  """The timezone you want times in the system displayed in."""
  timezone: Timezone
}

"""
The input object that defines the fields for the createNetworkSite mutation.
"""
input CreateNetworkSiteMutationInput {
  """A descriptive name."""
  name: String!
  """Height in meters."""
  height_in_meters: Float!
  """The address for the network site."""
  address: CreateNetworkSiteAddressMutationInput!
  """Data to insert into custom fields."""
  custom_field_data: [CustomFieldDataMutationInput]
  """
  If IDs of `CustomField` objects that are associated with this entity are
  provided here, they will be unset and removed. You cannot unset data where the
  `CustomField` property `required` is set to `true`.
  """
  unset_custom_field_data: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
  """The task to be performed."""
  tasks: [TaskMutationInput]
}
```
